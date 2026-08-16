
import os
import json
import re
import requests
from bs4 import BeautifulSoup

def analyze_reddit_user(username):
    print(f"\n[+] Avvio estrazione dati Reddit per l'utente: '{username}'...")

    # Puntiamo direttamente alla pagina web pubblica del profilo
    url = f"https://www.reddit.com/user/{username}/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            page_text = soup.get_text()

            # Estrazione Karma usando espressioni regolari dal testo pubblico
            karma_match = re.search(r'([\d,\.]+[kKmM]?)\s+karma', page_text, re.IGNORECASE)
            karma_val = karma_match.group(1) if karma_match else "Non rilevato"

            # Cercaiamo link esterni presenti nella pagina del profilo
            found_links = []
            for a_tag in soup.find_all("a", href=True):
                href = a_tag["href"]
                if href.startswith("http") and "reddit.com" not in href:
                    found_links.append(href)

            user_info = {
                "username": username,
                "profile_url": url,
                "karma_stimato": karma_val,
                "social_links_rilevati": list(set(found_links))
            }

            # Stampa risultati a schermo
            print("\n==================================================")
            print(f"📊 REPORT REDDIT (SCRAPING): {user_info['username']}")
            print("==================================================")
            print(f"👤 Username     : {user_info['username']}")
            print(f"🏆 Karma        : {user_info['karma_stimato']}")
            print(f"🔗 Link Trovati : {len(user_info['social_links_rilevati'])}")
            for link in user_info["social_links_rilevati"]:
                print(f"   👉 {link}")

            # Salva il report in JSON per il correlatore
            os.makedirs("data", exist_ok=True)
            filename = f"data/report_reddit_{username.lower()}.json"
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(user_info, f, indent=4, ensure_ascii=False)

            print(f"\n[✓] Report salvato con successo in: '{filename}'")
            return user_info

        elif response.status_code == 404:
            print(f"[-] Errore: L'utente Reddit '{username}' non esiste o è stato sospeso.")
        else:
            print(f"[-] Errore HTTP: {response.status_code}")

    except Exception as e:
        print(f"[-] Errore di connessione: {e}")

    return None