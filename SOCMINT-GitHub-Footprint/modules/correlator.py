
import os
import json

def correlate_target_data(target_name):
    data_dir = "data"
    
    if not os.path.exists(data_dir):
        print("[-] Errore: La cartella 'data/' non esiste ancora.")
        return

    # Trova tutti i file JSON che appartengono al target
    all_files = os.listdir(data_dir)
    target_files = [f for f in all_files if f.endswith(".json") and target_name.lower() in f.lower()]

    if not target_files:
        print(f"[-] Nessun report trovato nella cartella 'data/' contenente la parola '{target_name}'.")
        print("💡 Assicurati di aver eseguito prima le analisi con il modulo 1 o 2!")
        return

    print(f"\n==================================================")
    print(f" 🔗 ANALISI CORRELATA IMPRONTA DIGITALE: '{target_name}'")
    print(f"==================================================")
    print(f"[+] Report trovati ed esaminati ({len(target_files)}):")
    for tf in target_files:
        print(f"   📄 {tf}")

    all_links = {} # Dizionario per tracciare i link e dove sono stati trovati

    # Leggiamo ciascun file JSON identificato
    for file_name in target_files:
        filepath = os.path.join(data_dir, file_name)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                
                # Identifichiamo la fonte (GitHub, StackOverflow, ecc.) dal nome del file
                source = "Generico"
                if "stackoverflow" in file_name.lower():
                    source = "Stack Overflow"
                elif "github" in file_name.lower() or "report_" in file_name.lower():
                    source = "GitHub"

                links = data.get("social_links_rilevati", [])
                
                for link in links:
                    if link not in all_links:
                        all_links[link] = []
                    if source not in all_links[link]:
                        all_links[link].append(source)

        except Exception as e:
            print(f"[-] Errore nella lettura di {file_name}: {e}")

    # Visualizzazione dei risultati della correlazione
    print("\n--------------------------------------------------")
    if all_links:
        print(f"📊 RISULTATO CORRELAZIONE LINK ({len(all_links)} unici trovati):")
        for link, sources in all_links.items():
            sources_str = ", ".join(sources)
            if len(sources) > 1:
                print(f"   🔥 [DATO INCROCIATO] {link} ➔ (Trovato in: {sources_str})")
            else:
                print(f"   👉 {link} ➔ (Trovato in: {sources_str})")
    else:
        print("[-] Nessun link esterno o profilo rilevato nei report di questo target.")
    print("==================================================\n")