
import os
import json
import re  # Importiamo la libreria per la ricerca di pattern di testo (Regex)
import requests
from collections import Counter
from dotenv import load_dotenv

def analyze_github_user(target_user):
    load_dotenv()
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    print("=== STRUMENTO OSINT GITHUB & DATA ANALYSIS ===")

    if not target_user:
        print("Errore: Non hai inserito alcun nome utente!")
        return

    report_data = {
        "target": target_user,
        "profilo": {},
        "social_links_rilevati": [], # NUOVO CAMPO
        "analisi_statistica": {},
        "repositories": []
    }

    # --- PARTE 1: Estrazione dati generali del profilo ---
    url_user = f"https://api.github.com/users/{target_user}"
    response_user = requests.get(url_user, headers=headers)

    if response_user.status_code == 200:
        data_user = response_user.json()
        
        bio = data_user.get('bio') or ""
        blog = data_user.get('blog') or ""
        
        report_data["profilo"] = {
            "username": data_user.get('login'),
            "nome": data_user.get('name'),
            "azienda": data_user.get('company'),
            "luogo": data_user.get('location'),
            "bio": bio,
            "sito_web": blog,
            "public_repos": data_user.get('public_repos'),
            "followers": data_user.get('followers'),
            "creato_il": data_user.get('created_at')
        }
        print(f"\n[+] Profilo trovato: {data_user.get('name') or target_user}")
        
        # --- NUOVA SEZIONE OSINT: Estrazione automatica Link & Social ---
        found_links = []
        
        # 1. Controlliamo se c'è un sito nel campo blog
        if blog:
            found_links.append(blog)
            
        # 2. Cerchiamo qualsiasi altro URL (http/https) presente nella Bio tramite Regex
        urls_in_bio = re.findall(r'https?://[^\s]+', bio)
        for url in urls_in_bio:
            if url not in found_links:
                found_links.append(url)
                
        report_data["social_links_rilevati"] = found_links
        
        if found_links:
            print("\n🔗 LINK E PROFILI RILEVATI SUL TARGET:")
            for link in found_links:
                print(f"   👉 {link}")
                # Messaggio visivo speciale se troviamo Stack Overflow!
                if "stackoverflow.com" in link:
                    print("   💡 [HINT OSINT] Trovato profilo Stack Overflow! Puoi usare questo ID per il modulo 2.")
        else:
            print("\n[-] Nessun link esterno rilevato nella Bio o nel Sito Web.")

    elif response_user.status_code == 404:
        print(f"[-] Errore: L'utente '{target_user}' non esiste su GitHub.")
        return
    else:
        print(f"[-] Errore nella richiesta HTTP: {response_user.status_code}")
        return

    # --- PARTE 2: Estrazione Repository & Analisi Linguaggi ---
    url_repos = f"https://api.github.com/users/{target_user}/repos"
    response_repos = requests.get(url_repos, headers=headers)

    linguaggi_usati = []

    if response_repos.status_code == 200:
        repos_list = response_repos.json()

        for repo in repos_list:
            lang = repo.get('language')
            if lang:
                linguaggi_usati.append(lang)

            report_data["repositories"].append({
                "nome": repo.get('name'),
                "linguaggio": lang or "Non specificato",
                "descrizione": repo.get('description') or "Nessuna descrizione",
                "ultimo_aggiornamento": repo.get('updated_at')
            })

        print(f"[+] Scaricate ed esaminate {len(repos_list)} repository.")

    # --- PARTE 3: Calcolo Statistico ---
    if linguaggi_usati:
        conteggio_linguaggi = Counter(linguaggi_usati)
        linguaggio_dominante = conteggio_linguaggi.most_common(1)[0][0]

        report_data["analisi_statistica"] = {
            "linguaggio_principale": linguaggio_dominante,
            "distribuzione_linguaggi": dict(conteggio_linguaggi)
        }

        print("\n--- STATISTICHE TECNICHE TARGET ---")
        print(f"🏆 Linguaggio Principale: {linguaggio_dominante}")
        print("📊 Distribuzione Tecnologie:")
        for lang, count in conteggio_linguaggi.items():
            print(f"   - {lang}: {count} repository")
    else:
        report_data["analisi_statistica"] = {
            "linguaggio_principale": "Nessuno (progetti privi di codice rilevato)",
            "distribuzione_linguaggi": {}
        }

    # --- PARTE 4: Salvataggio nel file JSON ---
    filename = f"data/report_{target_user}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(report_data, f, ensure_ascii=False, indent=4)

    print(f"\n[✓] ANALISI COMPLETATA: Report salvato in '{filename}'")