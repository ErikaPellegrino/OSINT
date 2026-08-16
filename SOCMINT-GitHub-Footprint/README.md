
# 🔍 GitHub OSINT & Technical Profiling Tool

Un'applicazione Python per la raccolta dati automatizzata (OSINT) e l'analisi tecnica dei profili pubblici di GitHub tramite le API REST ufficiali.

---

## 📌 Descrizione del Progetto

Questo strumento consente di analizzare un qualsiasi profilo pubblico di GitHub estraendo informazioni generali, dettagli tecnici sui suoi progetti e fornendo un'**analisi statistica automatizzata** sulle tecnologie e i linguaggi di programmazione maggiormente utilizzati dal target.

I dati estratti e analizzati vengono esportati automaticamente in un file `.json` strutturato in locale.

---

## 🛠️ Tecnologie Utilizzate

* **Linguaggio:** Python 3
* **Librerie:**
  * `requests`: per la gestione delle chiamate HTTP alle API REST di GitHub.
  * `python-dotenv`: per la gestione sicura delle chiavi d'accesso.
  * `collections (Counter)`: per l'analisi statistica dei linguaggi di programmazione.
  * `json`: per l'esportazione dei report strutturati.

---

## 🔒 Sicurezza & Best Practices

In linea con gli standard di sicurezza dello sviluppo software e dell'ambito OSINT:
* **Token Management:** Le chiavi d'accesso personali (`GITHUB_TOKEN`) sono archiviate nel file `.env` locale e mai esposte nel codice sorgente.
* **Git Hygiene:** Utilizzo del file `.gitignore` per escludere credenziali sensibili e i report generati (`*.json`) dal tracciamento di Git.

---

## 🚀 Come Eseguire il Progetto

1. **Clona il repository:**
   ```bash
   git clone https://github.com/TUO_USERNAME/SOCMINT-GitHub-Footprint.git