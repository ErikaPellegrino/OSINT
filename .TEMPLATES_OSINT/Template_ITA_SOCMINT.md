# 👤 Report di Investigazione SOCMINT (SOCMINT Investigation Report) — Template Completo

> Template guida generico. Cancellare le sezioni/voci non pertinenti al caso specifico, non lasciarle vuote nel report finale.

## 📋 Panoramica del Caso (Case Overview)
- **ID Caso (Case ID):** [es. SOCMINT-2026-001]
- **Analista (Analyst):** [Nome / Alias]
- **Data dell'Analisi (Date of Analysis):** [AAAA-MM-GG]
- **Classificazione (Classification):** [TLP:CLEAR / TLP:AMBER / TLP:RED]
- **Categoria (Category):** SOCMINT
- **Sotto-categoria / Focus (Sub-category / Focus):** [Profile Verification / Network Analysis / Sockpuppet Detection / Sentiment & Narrative Tracking / Impersonation Check]
- **Livello di Confidenza (Confidence Level):** [Alto / Medio / Basso]

---

## 📌 Bottom Line Up Front (BLUF)
> **Risultato Chiave (Key Finding):** [1-2 frasi con l'esito principale — es. profilo autentico/falso, identità collegata, rete di account correlati]

---

## 🎯 Target e Obiettivo (Target & Objective)
- **Account / Handle Target (Target Account(s) / Handle(s)):** [username, piattaforma, link profilo]
- **Obiettivo Principale (Primary Objective):** [es. "verificare l'autenticità del profilo" / "mappare la rete di account collegati" / "individuare possibili sockpuppet"]
- **Piattaforme Coinvolte (Platform(s) Involved):** [Twitter/X, Instagram, Facebook, TikTok, LinkedIn, Telegram, Reddit, ecc.]
- **Confini dell'Ambito (Scope Boundaries):** [cosa è escluso — es. non si analizzano i contenuti privati/DM, solo dati pubblici]

---

## 🛡️ Sicurezza Operativa (Operational Security / OPSEC)
- **Valutazione del Rischio (Risk Assessment):** [Basso / Medio / Alto]
- **Account Sock Utilizzato (Sock Account Used):** [S/N — account dedicato per la ricerca, mai il proprio profilo reale]
- **Strumenti e Ambiente (Tools & Environment):** [VM isolata, browser dedicato, VPN/Tor se necessario]
- **Politica di Interazione (Interaction Policy):** [nessuna interazione con il target — no like, follow, commenti — per non rivelare l'osservazione]
- **Gestione dei Dati (Data Handling):** [gestione di dati personali/sensibili trovati, minimizzazione]

---

## 🔍 Evidenze Iniziali e Dati di Partenza (Initial Evidence & Input Data)
- **Punto di Partenza (Starting Point):** [username, link diretto, post segnalato]
- **Panoramica Account (Account Overview):** [data creazione, numero follower/following, bio, foto profilo]
- **Presenza Cross-platform (Cross-platform Presence):** [lo stesso username/persona è presente su altre piattaforme?]

---

## 🧩 Fasi dell'Investigazione (Investigation Steps)

### A. Verifica Autenticità Profilo (Profile Authenticity Check) *(quasi sempre applicabile)*
- **Età Account vs Livello di Attività (Account Age vs Activity Level):** [account recente con attività sproporzionata? indicatore comune di fake]
- **Verifica Foto Profilo (Profile Picture Verification):** [reverse image search — foto rubata da altro profilo/stock?]
- **Analisi Bio e Username (Bio & Username Analysis):** [pattern generico, username con numeri random, bio copiata]
- **Pattern di Pubblicazione (Posting Pattern):** [frequenza, orari, coerenza con fuso orario dichiarato]
- **Verdetto (Verdict):** [Probabile account autentico / Probabile fake / Inconcludente]

### B. Analisi Rete e Connessioni (Network & Connections Analysis) *(se rilevante mappare relazioni)*
- **Analisi Follower/Following (Followers/Following Analysis):** [presenza di bot, account correlati, community di riferimento]
- **Connessioni in Comune (Mutual Connections):** [contatti in comune con altri target/account noti]
- **Grafo delle Interazioni (Interaction Graph):** [con chi interagisce di più — like, commenti, retweet/repost]
- **Appartenenza a Gruppi / Pagine (Group / Page Memberships):** [gruppi, pagine seguite rilevanti per il caso]

### C. Rilevamento Sockpuppet / Account Multipli (Sockpuppet / Multiple Accounts Detection) *(se si sospettano account multipli della stessa persona/entità)*
- **Account Confrontati (Accounts Compared):** [elenco account sospettati collegati]
- **Indicatori Condivisi (Shared Indicators):** [stile di scrittura, orari di pubblicazione, foto riciclate, errori grammaticali ricorrenti, stessi link condivisi]
- **Correlazione Tecnica (Technical Correlation):** [se disponibile: metadati simili, stesse fonti di immagini]
- **Livello di Confidenza per Collegamento (Confidence Level per Collegamento):** [Alta/Media/Bassa per ogni coppia di account]

### D. Analisi Contenuti e Narrativa (Content & Narrative Analysis) *(se l'obiettivo riguarda cosa viene detto, non solo chi lo dice)*
- **Temi/Narrative Ricorrenti (Recurring Themes/Narratives):** [argomenti principali trattati]
- **Indicatori di Messaggistica Coordinata (Coordinated Messaging Indicators):** [stesso testo/hashtag postato da più account in finestra temporale ravvicinata]
- **Panoramica Sentiment (Sentiment Overview):** [tono generale — informativo, polarizzante, promozionale]
- **Pattern di Amplificazione (Amplification Patterns):** [il contenuto è amplificato artificialmente — bot, account nuovi?]

### E. Verifica Impersonificazione / Abuso di Brand (Impersonation / Brand Abuse Check) *(se il caso riguarda un profilo che finge di essere qualcun altro/un'azienda)*
- **Riferimento Account Legittimo (Legitimate Account Reference):** [link al profilo ufficiale/verificato, se esiste]
- **Discrepanze Riscontrate (Discrepancies Found):** [differenze in bio, contenuti, link esterni rispetto all'originale]
- **Già Segnalato Altrove? (Reported Elsewhere?):** [il profilo è già stato segnalato/documentato da altri]

### F. Ricostruzione Timeline (Timeline Reconstruction) *(se serve ricostruire l'evoluzione dell'account nel tempo)*
- **Storico Account (Account History):** [cambi di username, foto profilo, bio nel tempo — via Wayback Machine se disponibile]
- **Eventi Chiave (Key Events):** [picchi di attività, cambi di narrativa, sospensioni/riattivazioni]

---

## 🔒 Integrità delle Evidenze (Evidence Integrity)
- **Metodo di Acquisizione (Capture Method):** [SingleFile, screenshot, download post/media]
- **Hashing:** [SHA-256 per ogni file salvato]
- **Timestamping:** [UTC, riferimento chain of custody separata]
- **Versioni Archiviate (Archived Versions):** [Wayback Machine / archive.today per post che potrebbero essere cancellati]

---

## ✅ Validazione delle Evidenze (Evidence Validation)
- **Integrità dei Dati (Data Integrity):** [Verified direct source / Unverified third-party]
- **Stato di Verifica (Verification Status):** [Confirmed / Inconclusive / False Positive]
- **Metodo di Cross-validazione (Cross-validation Method):** [più indicatori indipendenti concordano sulla stessa conclusione?]

---

## ⚠️ Limitazioni (Limitations)
- [cosa non è stato possibile verificare — profilo privato, dati insufficienti, piattaforma con API limitate, ecc.]

---

## 🎯 Conclusione Finale e Sintesi (Final Conclusion & Summary)
- **Punti Chiave (Key Takeaways):** [sintesi di cosa è emerso e perché conta]
- **Valutazione Rischio / Impatto (Risk / Impact Assessment):** [se pertinente — es. rischio disinformazione, rischio reputazionale]
- **Raccomandazioni (Recommendations):** [eventuali azioni suggerite, se il contesto lo richiede]

---

## 📎 Appendice (Appendix)
- **Tabelle Dati Grezzi (Raw Data Tables):** [link a tabelle separate — es. elenco account correlati, timeline completa]
- **Versioni Strumenti (Tool Versions):** [versioni esatte degli strumenti usati]
