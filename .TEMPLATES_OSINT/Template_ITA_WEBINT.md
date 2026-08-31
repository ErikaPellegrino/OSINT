# 🌐 Report di Indagine WEBINT (WEBINT Investigation Report)

> Template guida generico. Cancellare le sezioni/voci non pertinenti al caso specifico, non lasciarle vuote nel report finale.

## 📋 Panoramica del Caso (Case Overview)
- **ID Caso (Case ID):** [es. WEBINT-2026-001]
- **Analista (Analyst):** [Nome / Alias]
- **Data Analisi (Date of Analysis):** [AAAA-MM-GG]
- **Classificazione (Classification):** [TLP:CLEAR / TLP:AMBER / TLP:RED]
- **Categoria (Category):** WEBINT
- **Sottocategoria / Focus (Sub-category / Focus):** [Footprinting / Dorking / Analisi Cronologia Wiki / Metadata Documentali / Verifica Fonti / Monitoraggio Brand / Due Diligence / Threat Intel]
- **Livello di Confidenza (Confidence Level):** [Alto / Medio / Basso]
- **SUBSTACK:** [link]

---

## 📌 Sintesi Esecutiva (BLUF - Bottom Line Up Front)
- **Sintesi Esecutiva (Key Finding):** [1-2 frasi con l'evidenza/finding più critico e il suo impatto/rischio]

---

## 🎯 Target e Obiettivi (Target & Objective)
- **Target Query / Dominio / Entità (Target Query / Domain / Entity):** [URL, dominio, nome azienda/persona, voce Wikipedia]
- **Obiettivo Primario (Primary Objective):** [Descrizione specifica, non generica — es. "Individuare pattern di editing sospetti e verificare l'affidabilità delle fonti citate"]
- **Obiettivi Secondari (Secondary Objectives):** [Eventuali obiettivi collaterali]
- **Perimetro d'Indagine (Scope Boundaries):** [Cosa è esplicitamente escluso dall'analisi]

---

## 🛡️ Sicurezza Operativa (Operational Security / OPSEC)
- **Valutazione del Rischio (Risk Assessment):** [Basso / Medio / Alto]
- **Ambiente Operativo (Operating Environment):** [VM isolata / browser dedicato / profilo pulito]
- **Hardening del Browser (Browser Hardening):** [Estensioni usate — ad-blocker, user agent switcher, ecc.]
- **Precauzioni di Rete (Network Precautions):** [VPN / Tor / IP reale — indicare se non applicabile]
- **Gestione Dati (Data Handling):** [Come vengono salvate e protette le prove raccolte]
- **Catena di Custodia (Chain of Custody):** [Riferimento al file/log separato con timestamp e hash — vedi sezione Integrità delle Prove]

---

## 🔍 Dati di Input ed Evidenze Iniziali (Initial Evidence & Input Data)
- **Punto di Partenza (Starting Point):** [URL, keyword, documento, username]
- **Motori di Ricerca Utilizzati (Search Engines Used):** [Google, DuckDuckGo, Bing, Yandex]
- **Piattaforme Specializzate Utilizzate (Specialized Platforms Used):** [Shodan, Wayback Machine, WikiBlame, XTools, ecc.]

---

## 🧩 Fasi dell'Indagine (Investigation Steps)

### A. Dorking & Footprinting *(se applicabile)*
- **Operatori di Ricerca Avanzata (Dorks):**
  ```text
  [dork utilizzati]
  ```
- **Sottodomini / Endpoint Esposti Individuati (Subdomains / Exposed Endpoints Identified):** [elenco]
- **File / Documenti Esposti (Exposed Files / Documents):** [elenco file, tipologia, link]

### B. Cronologia Modifiche / Analisi Temporale (Edit History / Timeline Analysis) *(se applicabile — es. Wikipedia, forum, wiki aziendali)*
- **Totale Modifiche Analizzate (Total Edits Analyzed):** [numero]
- **Arco Temporale Coperto (Time Period Covered):** [dal — al]
- **Contributori Chiave (Key Contributors):** [tabella o elenco username/IP principali]
- **Cluster Temporali Sospetti (Suspicious Temporal Clusters):** [picchi di modifica ravvicinati, edit war, ecc.]
- **Tabella di Riferimento (Reference Table):** [link alla tabella dettagliata separata, se utilizzata]

### C. Profilazione dei Contributori / Editor (Contributor / Editor Profiling) *(se applicabile)*
- **Età e Attività dell'Account (Account Age & Activity):** [data creazione, numero contributi totali]
- **Account Mono-Obiettivo (Single-purpose Accounts - SPA):** [account che modificano solo il target]
- **Possibili Sockpuppet (Possible Sockpuppets):** [pattern sospetti tra account diversi]
- **Analisi IP Anonimi (Anonymous IP Analysis):** [range, ASN, geolocalizzazione approssimativa]
- **Incrocio Dati Esterno (Cross-reference):** [LinkedIn, Google dork su username, ecc.]

### D. Analisi Metadata di Documenti e File Multimediali (Document & Media Metadata Analysis) *(se applicabile)*
- **File Analizzati (Files Analyzed):** [elenco]
- **Metadata Estratti (Extracted Metadata):** [autore, software, data creazione, coordinate GPS]
- **Strumenti Utilizzati (Tooling):** [ExifTool, exifviewer, ecc.]

### E. Ricerca Inversa Immagini / Analisi Video (Reverse Image Search / Video Analysis) *(se applicabile)*
- **Elementi Multimediali Analizzati (Media Elements Analyzed):** [elenco immagini/video]
- **Strumenti Utilizzati (Tools Used):** [InVID-WeVerify, RevEye, TinEye]
- **Fonte Originale Individuata (Original Source Identified):** [Sì/No — link]
- **Coerenza Contestuale (Context Match):** [L'immagine/video corrisponde al contesto dichiarato? Sì/No/Parziale]

### F. Verifica delle Fonti e delle Affermazioni (Source & Claims Verification) *(se applicabile)*
- **Affermazioni Sottoposte a Verifica (Claims Checked):** [elenco affermazioni verificate]
- **Fonti Incrociate (Cross-referenced):** [elenco fonti]
- **Versioni Archiviate (Archived Versions):** [Wayback Machine, Google Cache]
- **Esito della Verifica per Singola Affermazione (Verification Outcome per Claim):** [Confermata / Parzialmente Confermata / Falsa / Non Verificabile]

### G. Monitoraggio Brand e Reputazione (Brand & Reputation Monitoring) *(se applicabile)*
- **Menzioni Individuate (Mentions Identified):** [forum, social network, siti di recensione]
- **Indicatori di Impersonificazione / Phishing (Impersonation / Phishing Indicators):** [domini clone, profili fake]

### H. Due Diligence *(se applicabile)*
- **Registro Imprese e Atti Consultati (Business Registry & Filings Consulted):** [registri camerali, Partita IVA, atti pubblici]
- **Figure Chiave Individuate (Key People):** [ruoli, collegamenti]
- **Anomalie e Segnali d'Allarme (Red Flags):** [incoerenze, controparti sospette]

---

## 🔒 Integrità delle Prove (Evidence Integrity)
- **Metodo di Acquisizione (Capture Method):** [SingleFile, GoFullPage, screenshot manuale]
- **Hashing:** [SHA-256 per ogni file — riferimento al log hash]
- **Marcatura Temporale (Timestamping):** [UTC, riferimento alla catena di custodia]
- **Archiviazione Ridondante (Redundant Archiving):** [Salvataggio su Wayback Machine, backup locale]

---

## ✅ Validazione delle Evidenze (Evidence Validation)
- **Integrità dei Dati (Data Integrity):** [Fonte diretta verificata / Terza parte non verificata]
- **Stato della Verifica (Verification Status):** [Confermato / Inconcludente / Falso Positivo]
- **Metodo di Validazione Incrociata (Cross-validation Method):** [Più fonti indipendenti concordano?]

---

## ⚠️ Limitazioni dell'Analisi (Limitations)
- [Cosa non è stato possibile verificare — IP non tracciabili, fonti offline, dati non pubblici, ecc.]

---

## 🎯 Conclusioni e Sintesi Finale (Final Conclusion & Summary)
- **Punti Chiave (Key Takeaways):** [Sintesi concisa di cosa è emerso e della sua rilevanza]
- **Valutazione Rischio / Impatto (Risk / Impact Assessment):** [Se pertinente al contesto dell'indagine]
- **Raccomandazioni (Recommendations):** [Eventuali azioni o approfondimenti suggeriti]

---

## 📎 Appendice (Appendix)
- **Tabelle Dati Grezzi (Raw Data Tables):** [Link a tabelle separate — es. cronologia completa delle modifiche]
- **Versioni degli Strumenti (Tool Versions):** [Versioni esatte degli strumenti usati, necessarie per la riproducibilità]
