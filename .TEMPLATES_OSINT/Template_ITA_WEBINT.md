
# 🌐 Report di Indagine WEBINT

> Template guida generico. Cancellare le sezioni/voci non pertinenti al caso specifico, non lasciarle vuote nel report finale.

## 📋 Panoramica del Caso (Case Overview)
- **ID Caso:** [es. WEBINT-2026-001]
- **Analista:** [Nome / Alias]
- **Data Analisi:** [AAAA-MM-GG]
- **Classificazione:** [TLP:CLEAR / TLP:AMBER / TLP:RED]
- **Categoria:** WEBINT
- **Sottocategoria / Focus:** [Footprinting / Dorking / Analisi Cronologia Wiki / Metadata Documentali / Verifica Fonti / Monitoraggio Brand / Due Diligence / Threat Intel]
- **Livello di Confidenza:** [Alto / Medio / Basso]
- **SUBSTACK**: [link]

---

## 📌 Sintesi Esecutiva (BLUF - Bottom Line Up Front)
- **Sintesi Esecutiva:** [1-2 frasi con l'evidenza/finding più critico e il suo impatto/rischio]

---

## 🎯 Target e Obiettivi (Target & Objective)
- **Target Query / Dominio / Entità:** [URL, dominio, nome azienda/persona, voce Wikipedia]
- **Obiettivo Primario:** [Descrizione specifica, non generica — es. "Individuare pattern di editing sospetti e verificare l'affidabilità delle fonti citate"]
- **Obiettivi Secondari:** [Eventuali obiettivi collaterali]
- **Perimetro d'Indagine (Scope Boundaries):** [Cosa è esplicitamente escluso dall'analisi]

---

## 🛡️ Sicurezza Operativa (OPSEC)
- **Valutazione del Rischio (Risk Assessment):** [Basso / Medio / Alto]
- **Ambiente Operativo:** [VM isolata / browser dedicato / profilo pulito]
- **Hardening del Browser:** [Estensioni usate — ad-blocker, user agent switcher, ecc.]
- **Precauzioni di Rete:** [VPN / Tor / IP reale — indicare se non applicabile]
- **Gestione Dati (Data Handling):** [Come vengono salvate e protette le prove raccolte]
- **Catena di Custodia (Chain of Custody):** [Riferimento al file/log separato con timestamp e hash — vedi sezione Integrità delle Prove]

---

## 🔍 Dati di Input ed Evidenze Iniziali (Initial Evidence & Input Data)
- **Punto di Partenza (Starting Point):** [URL, keyword, documento, username]
- **Motori di Ricerca Utilizzati:** [Google, DuckDuckGo, Bing, Yandex]
- **Piattaforme Specializzate Utilizzate:** [Shodan, Wayback Machine, WikiBlame, XTools, ecc.]

---

## 🧩 Fasi dell'Indagine (Investigation Steps)

### A. Dorking & Footprinting *(se applicabile)*
- **Operatori di Ricerca Avanzata (Dorks):**
  ```text
  [dork utilizzati]
  ```
- **Sottodomini / Endpoint Esposti Individuati:** [elenco]
- **File / Documenti Esposti:** [elenco file, tipologia, link]

### B. Cronologia Modifiche / Analisi Temporale (se applicabile — es. Wikipedia, forum, wiki aziendali)
- **Totale Modifiche Analizzate:** [numero]
- **Arco Temporale Coperto:** [dal — al]
- **Contributori Chiave (Key Contributors):** [tabella o elenco username/IP principali]
- **Cluster Temporali Sospetti:** [picchi di modifica ravvicinati, edit war, ecc.]
- **Tabella di Riferimento:** [link alla tabella dettagliata separata, se utilizzata]

### C. Profilazione dei Contributori / Editor (se applicabile)
- **Età e Attività dell'Account:** [data creazione, numero contributi totali]
- **Account Mono-Obiettivo (Single-purpose Accounts - SPA):** [account che modificano solo il target]
- **Possibili Sockpuppet:** [pattern sospetti tra account diversi]
- **Analisi IP Anonimi:** [range, ASN, geolocalizzazione approssimativa]
- **Incrocio Dati Esterno (Cross-reference):** [LinkedIn, Google dork su username, ecc.]

### D. Analisi Metadata di Documenti e File Multimediali (se applicabile)
- **File Analizzati:** [elenco]
- **Metadata Estratti:** [autore, software, data creazione, coordinate GPS]
- **Strumenti Utilizzati (Tooling):** [ExifTool, exifviewer, ecc.]

### E. Ricerca Inversa Immagini / Analisi Video (se applicabile)
- **Elementi Multimediali Analizzati:** [elenco immagini/video]
- **Strumenti Utilizzati:** [InVID-WeVerify, RevEye, TinEye]
- **Fonte Originale Individuata:** [Sì/No — link]
- **Coerenza Contestuale (Context Match):** [L'immagine/video corrisponde al contesto dichiarato? Sì/No/Parziale]

### F. Verifica delle Fonti e delle Affermazioni (se applicabile)
- **Affermazioni Sottoposte a Verifica (Claims Checked):** [elenco affermazioni verificate]
- **Fonti Incrociate (Cross-referenced):** [elenco fonti]
- **Versioni Archiviate:** [Wayback Machine, Google Cache]
- **Esito della Verifica per Singola Affermazione:** [Confermata / Parzialmente Confermata / Falsa / Non Verificabile]

### G. Monitoraggio Brand e Reputazione (se applicabile)
- **Menzioni Individuate:** [forum, social network, siti di recensione]
- **Indicatori di Impersonificazione / Phishing:** [domini clone, profili fake]

### H. Due Diligence (se applicabile)
- **Registro Imprese e Atti Consultati:** [registri camerali, Partita IVA, atti pubblici]
- **Figure Chiave Individuate (Key People):** [ruoli, collegamenti]
- **Anomalie e Segnali d'Allarme (Red Flags):** [incoerenze, controparti sospette]

---

## 🔒 Integrità delle Prove (Evidence Integrity)
- **Metodo di Acquisizione (Capture Method):** [SingleFile, GoFullPage, screenshot manuale]
- **Hashing:** [SHA-256 per ogni file — riferimento al log hash]
- **Marcatura Temporale (Timestamping):** [UTC, riferimento alla catena di custodia]
- **Archiviazione Ridondante:** [Salvataggio su Wayback Machine, backup locale]

---

## ✅ Validazione delle Evidenze (Evidence Validation)
- **Integrità dei Dati:** [Fonte diretta verificata / Terza parte non verificata]
- **Stato della Verifica:** [Confermato / Inconcludente / Falso Positivo]
- **Metodo di Validazione Incrociata:** [Più fonti indipendenti concordano?]

---

## ⚠️ Limitazioni dell'Analisi (Limitations)
- [Cosa non è stato possibile verificare — IP non tracciabili, fonti offline, dati non pubblici, ecc.]

---

## 🎯 Conclusioni e Sintesi Finale (Final Conclusion & Summary)
- **Punti Chiave (Key Takeaways):** [Sintesi concisa di cosa è emerso e della sua rilevanza]
- **Valutazione Rischio / Impatto:** [Se pertinente al contesto dell'indagine]
- **Raccomandazioni:** [Eventuali azioni o approfondimenti suggeriti]

---

## 📎 Appendice (Appendix)
- **Tabelle Dati Grezzi (Raw Data):** [Link a tabelle separate — es. cronologia completa delle modifiche]
- **Versioni degli Strumenti:** [Versioni esatte degli strumenti usati, necessarie per la riproducibilità]


