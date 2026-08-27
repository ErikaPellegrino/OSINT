
# 👤 SOCMINT Investigation Report — Template Completo

> Template guida generico. Cancellare le sezioni/voci non pertinenti al caso specifico, non lasciarle vuote nel report finale.

## 📋 Case Overview
- **Case ID:** [e.g., SOCMINT-2026-001]
- **Analyst:** [Your Name / Alias]
- **Date of Analysis:** [YYYY-MM-DD]
- **Classification:** [TLP:CLEAR / TLP:AMBER / TLP:RED]
- **Category:** SOCMINT
- **Sub-category / Focus:** [Profile Verification / Network Analysis / Sockpuppet Detection / Sentiment & Narrative Tracking / Impersonation Check]
- **Confidence Level:** [High / Medium / Low]

---

## 📌 Bottom Line Up Front (BLUF)
> **Key Finding:** [1-2 frasi con l'esito principale — es. profilo autentico/falso, identità collegata, rete di account correlati]

---

## 🎯 Target & Objective
- **Target Account(s) / Handle(s):** [username, piattaforma, link profilo]
- **Primary Objective:** [es. "verificare l'autenticità del profilo" / "mappare la rete di account collegati" / "individuare possibili sockpuppet"]
- **Platform(s) Involved:** [Twitter/X, Instagram, Facebook, TikTok, LinkedIn, Telegram, Reddit, ecc.]
- **Scope Boundaries:** [cosa è escluso — es. non si analizzano i contenuti privati/DM, solo dati pubblici]

---

## 🛡️ Operational Security (OPSEC)
- **Risk Assessment:** [Low / Medium / High]
- **Sock Account Used:** [S/N — account dedicato per la ricerca, mai il proprio profilo reale]
- **Tools & Environment:** [VM isolata, browser dedicato, VPN/Tor se necessario]
- **Interaction Policy:** [nessuna interazione con il target — no like, follow, commenti — per non rivelare l'osservazione]
- **Data Handling:** [gestione di dati personali/sensibili trovati, minimizzazione]

---

## 🔍 Initial Evidence & Input Data
- **Starting Point:** [username, link diretto, post segnalato]
- **Account Overview:** [data creazione, numero follower/following, bio, foto profilo]
- **Cross-platform Presence:** [lo stesso username/persona è presente su altre piattaforme?]

---

## 🧩 Investigation Steps

### A. Profile Authenticity Check *(quasi sempre applicabile)*
- **Account Age vs Activity Level:** [account recente con attività sproporzionata? indicatore comune di fake]
- **Profile Picture Verification:** [reverse image search — foto rubata da altro profilo/stock?]
- **Bio & Username Analysis:** [pattern generico, username con numeri random, bio copiata]
- **Posting Pattern:** [frequenza, orari, coerenza con fuso orario dichiarato]
- **Verdict:** [Probabile account autentico / Probabile fake / Inconclusivo]

### B. Network & Connections Analysis *(se rilevante mappare relazioni)*
- **Followers/Following Analysis:** [presenza di bot, account correlati, community di riferimento]
- **Mutual Connections:** [contatti in comune con altri target/account noti]
- **Interaction Graph:** [con chi interagisce di più — like, commenti, retweet/repost]
- **Group / Page Memberships:** [gruppi, pagine seguite rilevanti per il caso]

### C. Sockpuppet / Multiple Accounts Detection *(se si sospettano account multipli della stessa persona/entità)*
- **Accounts Compared:** [elenco account sospettati collegati]
- **Shared Indicators:** [stile di scrittura, orari di pubblicazione, foto riciclate, errori grammaticali ricorrenti, stessi link condivisi]
- **Technical Correlation:** [se disponibile: metadati simili, stesse fonti di immagini]
- **Confidence Level per Collegamento:** [Alta/Media/Bassa per ogni coppia di account]

### D. Content & Narrative Analysis *(se l'obiettivo riguarda cosa viene detto, non solo chi lo dice)*
- **Recurring Themes/Narratives:** [argomenti principali trattati]
- **Coordinated Messaging Indicators:** [stesso testo/hashtag postato da più account in finestra temporale ravvicinata]
- **Sentiment Overview:** [tono generale — informativo, polarizzante, promozionale]
- **Amplification Patterns:** [il contenuto è amplificato artificialmente — bot, account nuovi?]

### E. Impersonation / Brand Abuse Check *(se il caso riguarda un profilo che finge di essere qualcun altro/un'azienda)*
- **Legitimate Account Reference:** [link al profilo ufficiale/verificato, se esiste]
- **Discrepancies Found:** [differenze in bio, contenuti, link esterni rispetto all'originale]
- **Reported Elsewhere?:** [il profilo è già stato segnalato/documentato da altri]

### F. Timeline Reconstruction *(se serve ricostruire l'evoluzione dell'account nel tempo)*
- **Account History:** [cambi di username, foto profilo, bio nel tempo — via Wayback Machine se disponibile]
- **Key Events:** [picchi di attività, cambi di narrativa, sospensioni/riattivazioni]

---

## 🔒 Evidence Integrity
- **Capture Method:** [SingleFile, screenshot, download post/media]
- **Hashing:** [SHA-256 per ogni file salvato]
- **Timestamping:** [UTC, riferimento chain of custody separata]
- **Archived Versions:** [Wayback Machine / archive.today per post che potrebbero essere cancellati]

---

## ✅ Evidence Validation
- **Data Integrity:** [Verified direct source / Unverified third-party]
- **Verification Status:** [Confirmed / Inconclusive / False Positive]
- **Cross-validation Method:** [più indicatori indipendenti concordano sulla stessa conclusione?]

---

## ⚠️ Limitations
- [cosa non è stato possibile verificare — profilo privato, dati insufficienti, piattaforma con API limitate, ecc.]

---

## 🎯 Final Conclusion & Summary
- **Key Takeaways:** [sintesi di cosa è emerso e perché conta]
- **Risk / Impact Assessment:** [se pertinente — es. rischio disinformazione, rischio reputazionale]
- **Recommendations:** [eventuali azioni suggerite, se il contesto lo richiede]

---

## 📎 Appendix
- **Raw Data Tables:** [link a tabelle separate — es. elenco account correlati, timeline completa]
- **Tool Versions:** [versioni esatte degli strumenti usati]