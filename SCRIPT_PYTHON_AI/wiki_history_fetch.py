"""
Script per estrarre la cronologia edit di una voce Wikipedia tramite l'API pubblica.

⚠️⚠️ Questo script è stato generato da Claude per l'esercizio WEBINT-01


Uso:
    python3 wiki_history_fetch.py

Modifica le variabili LANG e TITLE qui sotto per puntare a un'altra voce/lingua.

Cosa fa:
- Chiama l'API ufficiale di Wikipedia (MediaWiki API), lo stesso sistema usato
  da strumenti come XTools.
- Scarica TUTTI gli edit della voce (gestisce la paginazione automaticamente,
  utile se in futuro analizzi voci con centinaia/migliaia di edit).
- Per ogni edit estrae: data/ora (UTC nativo, nessuna conversione necessaria),
  editor, se l'editor è anonimo/IP mascherato o registrato, dimensione byte,
  variazione byte rispetto all'edit precedente, e il commento (edit summary).
- Genera una tabella Markdown pronta da incollare in Obsidian (01_tabella_edit.md)
  e un file CSV per chi preferisce aprirlo in un foglio di calcolo.

Note metodologiche:
- I dati vengono presi direttamente dalla fonte ufficiale (api.wikipedia.org),
  la stessa che alimenta la pagina Cronologia che vedi nel browser: nessuna
  interpretazione o modifica dei dati grezzi.
- La colonna "Registrato" è calcolata dal campo "anon" restituito dall'API,
  oppure riconoscendo il pattern "~YYYY-xxxxx-xx" degli IP mascherati.
- Questo script NON valuta se un edit è "sospetto": quella è la parte di
  analisi che resta compito tuo, qui prepariamo solo i dati puliti.
"""

import requests
import csv
import sys
from datetime import datetime

# ---- Configurazione: modifica qui per un'altra voce/lingua ----
LANG = "it"
TITLE = "Veidt Enterprises"
OUTPUT_MD = "/mnt/user-data/outputs/01_tabella_edit_generata.md"
OUTPUT_CSV = "/mnt/user-data/outputs/01_tabella_edit_generata.csv"
# -----------------------------------------------------------------

API_URL = f"https://{LANG}.wikipedia.org/w/api.php"


def is_registered(revision: dict) -> str:
    """Determina se l'editor è un account registrato, un IP nudo, o un IP mascherato."""
    if revision.get("anon", False):
        user = revision.get("user", "")
        if user.startswith("~"):
            return "No (IP mascherato)"
        return "No (IP)"
    return "Sì"


def fetch_all_revisions(lang: str, title: str) -> list:
    """Scarica tutte le revisioni di una voce, gestendo la paginazione dell'API."""
    revisions = []
    params = {
        "action": "query",
        "prop": "revisions",
        "titles": title,
        "rvlimit": "max",  # fino a 500 per chiamata per utenti non autenticati
        "rvprop": "timestamp|user|comment|size|ids|flags|tags",
        "format": "json",
        "formatversion": "2",
    }

    headers = {
        # L'API di Wikipedia chiede di identificare il client (buona prassi,
        # non obbligatorio ma consigliato dalle policy MediaWiki)
        "User-Agent": "OSINT-Portfolio-Research-Script/1.0 (uso didattico/portfolio personale)"
    }

    while True:
        resp = requests.get(API_URL, params=params, headers=headers, timeout=30)
        resp.raise_for_status()
        data = resp.json()

        pages = data.get("query", {}).get("pages", [])
        if not pages:
            print("Nessuna pagina trovata. Controlla il titolo della voce.")
            sys.exit(1)

        page = pages[0]
        if "missing" in page:
            print(f"La voce '{title}' non esiste su {lang}.wikipedia.org.")
            sys.exit(1)

        revisions.extend(page.get("revisions", []))

        if "continue" in data:
            params.update(data["continue"])
        else:
            break

    return revisions


def build_rows(revisions: list) -> list:
    """Trasforma le revisioni grezze dell'API in righe pronte per la tabella."""
    rows = []
    # L'API restituisce le revisioni dalla più recente alla più vecchia.
    # Calcoliamo il delta byte confrontando ogni edit con quello successivo
    # nell'elenco (che è cronologicamente precedente).
    for i, rev in enumerate(revisions):
        size = rev.get("size", 0)
        if i + 1 < len(revisions):
            prev_size = revisions[i + 1].get("size", 0)
            delta = size - prev_size
        else:
            delta = size  # primo edit in assoluto (creazione voce)

        ts = rev.get("timestamp", "")  # formato ISO 8601, es. 2026-08-06T13:42:00Z
        try:
            dt = datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ")
            date_str = dt.strftime("%Y-%m-%d")
            time_str = dt.strftime("%H:%M") + " UTC"
        except ValueError:
            date_str, time_str = ts, ""

        user = rev.get("user", "sconosciuto")
        registered = is_registered(rev)
        comment = rev.get("comment", "").strip() or "(nessuno)"
        tags = ", ".join(rev.get("tags", [])) or "-"
        revid = rev.get("revid", "")
        diff_url = f"https://{LANG}.wikipedia.org/w/index.php?title={TITLE.replace(' ', '_')}&diff=prev&oldid={revid}"

        rows.append({
            "data": date_str,
            "ora_utc": time_str,
            "editor": user,
            "registrato": registered,
            "delta_byte": f"{delta:+d}",
            "commento": comment,
            "tags": tags,
            "diff_url": diff_url,
        })

    # Ordiniamo dal più vecchio al più recente, più naturale da leggere in tabella
    rows.reverse()
    return rows


def write_markdown(rows: list, path: str):
    lines = [
        "# Tabella Cronologia Edit — Generata automaticamente via API Wikipedia",
        "",
        f"> Fonte: api.wikipedia.org — {len(rows)} edit totali estratti il "
        f"{datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "| # | Data | Ora (UTC) | Editor | Registrato? | Δ byte | Commento edit | Tag | Sospetto? (S/N) | Note | Link diff |",
        "|---|------|-----------|--------|-------------|--------|----------------|-----|-------------------|------|-----------|",
    ]
    for i, r in enumerate(rows, start=1):
        lines.append(
            f"| {i} | {r['data']} | {r['ora_utc']} | {r['editor']} | {r['registrato']} | "
            f"{r['delta_byte']} | {r['commento']} | {r['tags']} |  |  | [diff]({r['diff_url']}) |"
        )
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_csv(rows: list, path: str):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "data", "ora_utc", "editor", "registrato", "delta_byte",
            "commento", "tags", "diff_url"
        ])
        writer.writeheader()
        for r in rows:
            writer.writerow(r)


def main():
    print(f"Scarico la cronologia di '{TITLE}' ({LANG}.wikipedia.org)...")
    revisions = fetch_all_revisions(LANG, TITLE)
    print(f"Trovati {len(revisions)} edit totali.")

    rows = build_rows(revisions)

    write_markdown(rows, OUTPUT_MD)
    write_csv(rows, OUTPUT_CSV)

    print(f"Tabella Markdown salvata in: {OUTPUT_MD}")
    print(f"File CSV salvato in: {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
