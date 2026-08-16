
import os
import json
import re  # Modulo per la ricerca con Regex
import requests
from dotenv import load_dotenv

def analyze_stackoverflow_user(search_query):
    load_dotenv()

    print("=== STRUMENTO OSINT STACK OVERFLOW & DATA ANALYSIS ===")

    if not search_query:
        print("Errore: Non hai inserito alcun nome utente o ID!")
        return

    selected_user = None

    # Se l'input contiene solo cifre, proviamo l'accesso diretto per ID
    if search_query.isdigit():
        url_id = f"https://api.stackexchange.com/2.3/users/{search_query}?site=stackoverflow"
        res_id = requests.get(url_id)
        if res_id.status_code == 200:
            items = res_id.json().get("items", [])
            if items:
                selected_user = items[0]

    # Se non è un ID numerico o l'ID non è stato trovato, effettuiamo la ricerca per NOME UTENTE
    if not selected_user:
        url_search = f"https://api.stackexchange.com/2.3/users?inname={search_query}&site=stackoverflow"
        res_search = requests.get(url_search)

        if res_search.status_code == 200:
            items = res_search.json().get("items", [])
            if not items:
                print(f"[-] Errore: Nessun utente trovato con il nome/query '{search_query}' su Stack Overflow.")
                return

            if len(items) == 1:
                selected_user = items[0]
            else:
                # Se troviamo più utenti con quel nome, mostriamo una lista di selezione
                print(f"\n[!] Trovati {len(items)} utenti per '{search_query}':\n")
                for index, u in enumerate(items[:5], 1): # Mostriamo i primi 5 risultati più rilevanti
                    name = u.get('display_name', 'N/D')
                    rep = u.get('reputation', 0)
                    loc = u.get('location', 'Luogo non specificato')
                    print(f"   {index}. {name} | Reputazione: {rep} | Luogo: {loc}")

                choice = input("\nInserisci il numero dell'utente che vuoi analizzare (es. 1): ").strip()
                if choice.isdigit() and 1 <= int(choice) <= min(len(items), 5):
                    selected_user = items[int(choice) - 1]
                else:
                    print("[-] Scelta non valida. Operazione annullata.")
                    return
        else:
            print(f"[-] Errore nella richiesta HTTP: {res_search.status_code}")
            return

    # Ora che l'utente è stato selezionato, estraiamo i dati completi
    user_id = selected_user.get('user_id')
    website_url = selected_user.get('website_url') or ""
    about_me = selected_user.get('about_me') or ""

    report_data = {
        "target_id": user_id,
        "profilo": {
            "display_name": selected_user.get('display_name'),
            "reputation": selected_user.get('reputation'),
            "location": selected_user.get('location'),
            "website_url": website_url,
            "about_me": about_me,
            "badge_counts": selected_user.get('badge_counts'),
            "created_at": selected_user.get('creation_date')
        },
        "social_links_rilevati": [],  # RADAR OSINT
        "metriche": {}
    }

    print(f"\n[+] Analisi in corso per: {selected_user.get('display_name')} (ID: {user_id})")
    print(f"🏆 Reputazione: {selected_user.get('reputation')}")

    # --- RADAR OSINT: Estrazione automatica Link ---
    found_links = []

    if website_url:
        found_links.append(website_url)

    urls_in_about = re.findall(r'https?://[^\s<>"]+', about_me)
    for url_item in urls_in_about:
        if url_item not in found_links:
            found_links.append(url_item)

    report_data["social_links_rilevati"] = found_links

    if found_links:
        print("\n🔗 LINK E PROFILI RILEVATI SU STACK OVERFLOW:")
        for link in found_links:
            print(f"   👉 {link}")
            if "github.com" in link:
                print("   💡 [HINT OSINT] Trovato un profilo GitHub collegato in questo account!")
    else:
        print("\n[-] Nessun link esterno rilevato nel profilo o nella bio di Stack Overflow.")

    # --- METRICHE DI ATTIVITÀ ---
    badges = selected_user.get('badge_counts', {})
    report_data["metriche"] = {
        "gold_badges": badges.get('gold', 0),
        "silver_badges": badges.get('silver', 0),
        "bronze_badges": badges.get('bronze', 0)
    }

    # --- Salvataggio nel file JSON ---
    filename = f"data/report_stackoverflow_{user_id}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(report_data, f, ensure_ascii=False, indent=4)

    print(f"\n[✓] ANALISI STACK OVERFLOW COMPLETATA: Report salvato in '{filename}'")