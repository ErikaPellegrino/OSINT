
# 🌐 Report di Indagine WEBINT

Analisi della cronologia di una voce Wikipedia: Progetto Veidt Enterprises

Individuazione di pattern di editing sospetti e verifica delle fonti.

## 📋 Panoramica del Caso (Case Overview)
- **ID Caso:** WEBINT-01 — analisi_wiki_veidt_enterprises 
- **Analista:** Erika Pellegrino
- **Data Analisi:** Agosto 2026
- **Classificazione:** TLP:CLEAR
- **Categoria:** WEBINT
- **Sottocategoria / Focus:** Analisi Cronologia Wiki / Verifica Fonti
- **Livello di Confidenza:** Alto
- **SUBSTACK**: https://substack.com/@erika124440/note/p-212973860?r=8wzskn&utm_source=notes-share-action&utm_medium=web

---

## 📌 Sintesi Esecutiva (BLUF - Bottom Line Up Front)
- **Sintesi Esecutiva:** L’analisi della cronologia completa (50 modifiche, 40 editori distinti) della voce Wikipedia di Veidt Enterprises non ha rilevato pattern sistematici di manipolazione editoriale a favore dell’azienda, né campagne diffamatorie organizzate contro di essa. Il blocco di modifiche più rilevante (righe 13-17) mostra due episodi isolati e indipendenti: un contenuto favorevole ma privo di fonti e un’accusa infondata di frode, entrambi corretti in autonomia dalla comunità Wikipedia secondo le proprie policy di verificabilità. Un solo caso di fonte apparentemente irraggiungibile (riga 18) si è rivelato, dopo approfondimento, una fonte reale la cui pagina originale non è più online per riorganizzazione del sito ospitante.

---

## 🎯 Target e Obiettivi (Target & Objective)
- **Target Query / Dominio / Entità:** Voce Wikipedia "Veidt Enterprises" (azienda tech anonimizzata)
- **Obiettivo Primario:** Individuare pattern di modifica sospetti — nello specifico modifiche con Conflitto di Interessi (COI) — e verificare l'affidabilità delle fonti citate nell'articolo
- **Obiettivi Secondari:** Individuare potenziali edit war o modifiche ritorsive tra i contributori
- **Perimetro d'Indagine (Scope Boundaries):** La geolocalizzazione e l'attribuzione di rete degli indirizzi IP coinvolti sono state esplicitamente escluse dal perimetro di questa indagine

---

## 🛡️ Sicurezza Operativa (OPSEC)
- **Valutazione del Rischio (Risk Assessment):** Basso
- **Ambiente Operativo:** Macchina virtuale VirtualBox con Kali Linux, browser Firefox
- **Hardening del Browser:** Estensioni User-Agent Switcher e uBlock Origin attive
- **Precauzioni di Rete:** Non richieste (consultazione di contenuti pubblici; nessuna interazione con infrastrutture sensibili)
- **Gestione Dati (Data Handling):** SingleFile, GoFullPage, Wayback Machine, hashing SHA-256
- **Catena di Custodia (Chain of Custody):** Mantenuta su Obsidian per tutta la durata dell'indagine; vedere l'Appendice per un estratto esemplificativo

---

## 🔍 Dati di Input ed Evidenze Iniziali (Initial Evidence & Input Data)
- **Punto di Partenza (Starting Point):** Voce Wikipedia dell'azienda tech "Veidt Enterprises"
- **Motori di Ricerca Utilizzati:** DuckDuckGo, Bing, Google
- **Piattaforme Specializzate Utilizzate:** Wayback Machine, XTools (statistiche sulle modifiche di Wikipedia), API Pubblica di MediaWiki

---

## 🧩 Fasi dell'Indagine (Investigation Steps)

### A. Cronologia Modifiche / Analisi Temporale (Edit History / Timeline Analysis)
- **Totale Modifiche Analizzate:** 50
- **Arco Temporale Coperto:** 29-06-2020 / 19-08-2026
- **Contributori Chiave (Key Contributors):** 40 contributori distinti — un rapporto quasi 1:1 tra contributori e modifiche, che indica l'assenza di un singolo editor dominante
- **Cluster Temporali Sospetti:** Le righe 13–17 hanno mostrato un'attività concentrata in un breve arco temporale; a un'analisi più approfondita, si è trattato di due episodi distinti e non correlati anziché di una sequenza coordinata
- **Tabella di Riferimento:** Cronologia completa estratta tramite lo script Python `wiki_history_fetch` (API MediaWiki); vedere l'Appendice per un estratto delle righe 13–17

### B. Profilazione dei Contributori / Editor (Contributor / Editor Profiling)
- **Età e Attività dell'Account:** Non profilati sistematicamente oltre le righe segnalate 
- **Single-purpose Accounts - SPA:** Nessuno individuato tra le righe segnalate
- **Possibili Sockpuppet:** Nessuno individuato. Le modifiche da IP mascherato analizzate (es. tre modifiche consecutive nello stesso giorno da un unico IP mascherato) sono risultate, dopo la revisione del diff, normali modifiche sequenziali di un singolo contributore e non un'attività coordinata di sockpuppeting
- **Analisi IP Anonimi:** Le righe 13–14 (IP mascherato) e le righe 16–17 (due IP anonimi differenti) sono state analizzate a livello di contenuto; non è stata effettuata alcuna attribuzione di rete o geolocalizzazione (vedere Perimetro d'Indagine - Scope Boundaries)
- **Cross-reference:** Non applicabile — nessun username richiedeva ricerche esterne incrociate 

### C. Verifica Fonti e Informazioni (Source & Claim Verification)
**Affermazioni Sottoposte a Verifica (Claims Checked):**
  - Riga 18: affermazione secondo cui un'app aziendale avrebbe superato i 300 milioni di download, citando "Evening Future" (eveningfuture.com)
  - Righe 13–15: affermazione relativa ad acquisizioni aziendali, aggiunta da un IP anonimo senza fonti
  - Righe 16–17: affermazione che allegava presunte pratiche fraudolente / addebiti non autorizzati (€9,99/settimana)
- **Fonti Incrociate (Cross-referenced):** Portale Acme Group, testate giornalistiche indipendenti, dork sui motori di ricerca
- **Operatori di Ricerca Avanzata (Dorks):**
  ```text
  "300 milioni di download" AND "Veidt Enterprises" site:eveningfuture.com
  ```

  ```text
  site:acmegroup.com "Veidt Enterprises"
  ```

  ```text
  "Veidt Enterprises" (addebito OR abbonamento OR "9,99") (truffa OR frode OR "non autorizzato") -site:it.wikipedia.org -site:veidtenterprises.com
  ```
- **Versioni Archiviate:** Verificato Wayback Machine per l'URL specifico di eveningfuture.com — nessuna istantanea trovata; la pagina principale della voce è stata archiviata separatamente su Wayback Machine (vedere Integrità delle Prove)
- **Esito della Verifica per Singola Affermazione:** 
  - 300 Milioni di Download (Riga 18): Confermata. La fonte esiste come rubrica editoriale autentica all'interno di Acme Group; l'URL specifico del 2020 non è raggiungibile a causa della ristrutturazione del sito e non per una falsificazione
  - Acquisizioni (Righe 13–15): Non verificabile / Rimosso. Il contenuto era verosimile ma è stato rimosso secondo le linee guida per mancanza di citazioni nel testo — nessuna evidenza di manipolazione
  - Accuse di Frode (Righe 16–17): Infondate. Non sono stati trovati riscontri pubblici o reclami riferiti a Veidt Enterprises; il contenuto è stato rimosso dalla community poiché non enciclopedico e non verificato. L'assenza di conferme esterne avvalora, pur senza provarlo in modo definitivo, che l'accusa fosse priva di fondamento

---

## 🔒 Integrità delle Prove (Evidence Integrity)
- **Metodo di Acquisizione (Capture Method):** SingleFile (HTML completo con risorse incorporate) e GoFullPage (screenshot PNG senza perdita di qualità) per le pagine chiave; dati di revisione estratti tramite l'API pubblica di MediaWiki utilizzando lo script Python personalizzato wiki_history_fetch
- **Hashing:** SHA-256 calcolato tramite terminale Kali (sha256sum) per ogni file raccolto, registrato nella Chain of custody
- **Marcatura Temporale (Timestamping):** Timestamp UTC registrati per tutte le attività di raccolta; metadata del file system recuperati tramite il comando stat nei casi in cui l'ora di acquisizione non fosse altrimenti visibile
- **Archiviazione Ridondante:** Istantanea generata su Wayback Machine per la voce principale; omessa per la pagina della Cronologia, in quanto le righe delle revisioni passate sono immutabili e non richiedono archiviazione indipendente

---

## ✅ Validazione delle Evidenze (Evidence Validation)
- **Integrità dei Dati:** Verificata rispetto alla fonte diretta e convalidata incrociando i dati tramite l'API pubblica di MediaWiki
- **Stato della Verifica:** confermato — normale comportamento di moderazione della community, nessuna evidenza di modifiche in Conflitto di Interessi (COI) o di edit war
- **Metodo di Validazione Incrociata (Cross-validation Method):** Dork indipendenti su tre motori di ricerca (Google, Bing, DuckDuckGo), incrociati con la copertura giornalistica generale

---

## ⚠️ Limitazioni dell'Analisi (Limitations)
- Gli indirizzi IP coinvolti non sono stati sottoposti ad attribuzione di rete o geolocalizzazione — esplicitamente fuori dal perimetro d'indagine
- Le modifiche ordinarie (bot, correzioni formali, sincronizzazioni Wikidata) sono state sottoposte a un controllo rapido anziché a una revisione completa diff-per-diff
- Il contenuto originale dell'articolo di "Evening Future" non è stato possibile recuperarlo, in quanto non è più ospitato online né archiviato
- La verifica esterna sull'accusa di frode ha evidenziato un'assenza di prove a supporto, e non una smentita attiva — questo avvalora, ma non prova in modo definitivo, che l'accusa fosse infondata

---

## 🎯 Conclusioni e Sintesi Finale (Final Conclusion & Summary)
- **Punti Chiave (Key Takeaways):** 50 modifiche effettuate da 40 contributori distinti mostrano una normale e sana moderazione da parte della community. Sia i contenuti favorevoli senza fonti sia quelli ostili senza fonti sono stati tempestivamente corretti applicando le medesime regole di verificabilità. 
- **Valutazione Rischio / Impatto (Risk / Impact Assessment):** Basso rischio reputazionale. La voce attuale è ben monitorata dalla community; le modifiche potenzialmente dannose sono state annullate nel giro di poche ore.
- **Raccomandazioni (Recommendations):** Per il personale che gestisce il profilo pubblico dell'azienda — aggiungere citazioni verificabili nella sezione "Acquisizioni" per evitare che contenuti accurati ma privi di fonte vengano nuovamente rimossi in futuro.

---

## 📎 Appendice (Appendix)
- **Tabelle Dati Grezzi (Raw Data):** 
  *Chain of Custody (estratto esemplificativo):*

  | Timestamp (UTC) | File Name | Description | Capture Method | SHA-256 Hash |
  |---|---|---|---|---|
  | 2026-08-19 14:00:00 | `20260819_140000_UTC_Veidt_Enterprises_Main.html` | Pagina principale Wikipedia di partenza | SingleFile | `9f3a1c7e2b8d4560af12e3d9c6b7a8451f0e2d3c4b5a6978012345abcde6789` |
  | 2026-08-19 14:05:00 | `20260819_140500_UTC_Veidt_Enterprises_Main.png` | Screenshot a pagina intera di partenza | GoFullPage | `4b7e9a2f1c3d5e6078901234abcdef56789012345bcdef0123456789abcde12` |
  | 2026-08-19 14:20:00 | `20260819_142000_UTC_Veidt_Enterprises_History.html` | Pagina cronologia modifiche di Wikipedia | SingleFile | `1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f60718293a4b5c6d7e8f90123456789abc` |

  *(Gli hash mostrati sono valori indicativi e illustrativi, non i valori reali dell'indagine originale.)*

  *Tabella Cronologia Modifiche — Blocco 13–17 (dati fittizi)::*

  | Row | Timestamp (UTC) | Editor | Registrato | Δ Bytes | Tag / Comment | Flagged/segnalato | Notes |
  |---|---|---|---|---|---|---|---|
  | 13 | 2024-08-23 10:15 | IP (masked) | No | +450 | Aggiunta sezione "Acquisizioni" | SI | Aggiunti dati sulle acquisizioni senza fonti |
  | 14 | 2024-08-23 10:22 | IP (masked, same) | No | +120 | Formattazione minore | SI | Modifica successiva alla sezione acquisizioni|
  | 15 | 2024-09-15 11:05 | User_Editor1 | Yes | -570 | Annullate modifiche: fonti mancanti | NO | Annullate righe 13–14 per mancanza di verificabilità |
  | 16 | 2024-09-27 08:24 | IP (different) | No | +285 | Accusa di frode  | SI | Nessuna citazione, tono non enciclopedico |
  | 17 | 2024-09-27 14:54 | IP (different) | No | -285 | "Rimosse informazioni non verificate" | NO | Rimozione legittima |


- **Versioni degli Strumenti:** SingleFile e GoFullPage (estensioni Firefox, versioni installate al momento dell'analisi); Python 3 con libreria `requests` per `wiki_history_fetch`; set di strumenti predefinito di Kali Linux (`sha256sum, stat, nano`)


