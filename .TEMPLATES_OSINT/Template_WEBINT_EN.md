
# 🌐 WEBINT Investigation Report 

> Template guida generico. Cancellare le sezioni/voci non pertinenti al caso specifico, non lasciarle vuote nel report finale.

## 📋 Case Overview
- **Case ID:** [e.g., WEBINT-2026-001]
- **Analyst:** [Your Name / Alias]
- **Date of Analysis:** [YYYY-MM-DD]
- **Classification:** [TLP:CLEAR / TLP:AMBER / TLP:RED]
- **Category:** WEBINT
- **Sub-category / Focus:** [Footprinting / Dorking / Wiki History Analysis / Document Metadata / Source Verification / Brand Monitoring / Due Diligence / Threat Intel]
- **Confidence Level:** [High / Medium / Low]
- **SUBSTACK:** [link]

---

## 📌 Bottom Line Up Front (BLUF)
- **Executive Summary:** [1-2 frasi con il finding più critico e il suo impatto/rischio]

---

## 🎯 Target & Objective
- **Target Query / Domain / Entity:** [URL, dominio, nome azienda/persona, voce Wikipedia]
- **Primary Objective:** [Descrizione specifica, non generica — es. "individuare pattern di editing sospetti e verificare l'affidabilità delle fonti citate"]
- **Secondary Objectives:** [eventuali obiettivi collaterali]
- **Scope Boundaries:** [cosa è esplicitamente escluso dall'indagine]

---

## 🛡️ Operational Security (OPSEC)
- **Risk Assessment:** [Low / Medium / High]
- **Environment:** [VM isolata / browser dedicato / profilo pulito]
- **Browser Hardening:** [estensioni usate — ad-blocker, user agent switcher, ecc.]
- **Network Precautions:** [VPN / Tor / IP reale — indicare se non applicabile]
- **Data Handling:** [come vengono salvate e protette le prove raccolte]
- **Chain of Custody:** [riferimento al file/log separato con timestamp e hash — vedi sezione Evidence Integrity]

---

## 🔍 Initial Evidence & Input Data
- **Starting Point:** [URL, keyword, documento, username]
- **Search Engines Used:** [Google, DuckDuckGo, Bing, Yandex]
- **Specialized Platforms Used:** [Shodan, Wayback Machine, WikiBlame, XTools, ecc.]

---

## 🧩 Investigation Steps

### A. Dorking & Footprinting *(se applicabile)*
- **Advanced Search Operators (Dorks):**
  ```text
  [dork utilizzati]
  ```
- **Subdomains / Exposed Endpoints Found:** [elenco]
- **Exposed Files / Documents:** [elenco file, tipo, link]

### B. Edit History / Timeline Analysis *(se applicabile — es. Wikipedia, forum, wiki aziendali)*
- **Total Edits Analyzed:** [numero]
- **Time Period Covered:** [dal — al]
- **Key Contributors:** [tabella o elenco username/IP principali]
- **Suspicious Temporal Clusters:** [picchi di edit ravvicinati, edit war, ecc.]
- **Reference Table:** [link alla tabella dettagliata separata, se usata]

### C. Contributor / Editor Profiling *(se applicabile)*
- **Account Age & Activity:** [data creazione, numero contributi totali]
- **Single-purpose Accounts (SPA):** [account che editano solo il target]
- **Possible Sockpuppets:** [pattern sospetti tra account diversi]
- **Anonymous IP Analysis:** [range, ASN, geolocalizzazione approssimativa]
- **Cross-reference esterno:** [LinkedIn, Google dork su username, ecc.]

### D. Document & Media Metadata Analysis *(se applicabile)*
- **Files Analyzed:** [elenco]
- **Metadata Extracted:** [autore, software, data creazione, coordinate GPS]
- **Tooling:** [ExifTool, exifviewer, ecc.]

### E. Reverse Image / Video Verification *(se applicabile)*
- **Media Analyzed:** [elenco immagini/video]
- **Tools Used:** [InVID-WeVerify, RevEye, TinEye]
- **Original Source Found:** [S/N — link]
- **Context Match:** [l'immagine/video corrisponde al contesto dichiarato? S/N/Parziale]

### F. Source & Claim Verification *(se applicabile)*
- **Claims Checked:** [elenco affermazioni verificate]
- **Sources Cross-referenced:** [elenco fonti]
- **Archived Versions:** [Wayback Machine, Google Cache]
- **Verification Outcome per Claim:** [Confirmed / Partially Confirmed / False / Unverifiable]

### G. Brand / Reputation Monitoring *(se applicabile)*
- **Mentions Found:** [forum, social, review site]
- **Impersonation / Phishing Indicators:** [domini clone, profili fake]

### H. Due Diligence *(se applicabile)*
- **Corporate Records Checked:** [registri camerali, VAT, filings pubblici]
- **Key People Identified:** [ruoli, collegamenti]
- **Red Flags:** [incoerenze, controparti sospette]

---

## 🔒 Evidence Integrity
- **Capture Method:** [SingleFile, GoFullPage, screenshot manuale]
- **Hashing:** [SHA-256 per ogni file — riferimento al log hash]
- **Timestamping:** [UTC, riferimento chain of custody]
- **Redundant Storage:** [Wayback Machine save, backup locale]

---

## ✅ Evidence Validation
- **Data Integrity:** [Verified direct source / Unverified third-party]
- **Verification Status:** [Confirmed / Inconclusive / False Positive]
- **Cross-validation Method:** [più fonti indipendenti concordano?]

---

## ⚠️ Limitations
- [Cosa non è stato possibile verificare — IP non tracciabili, fonti offline, dati non pubblici, ecc.]

---

## 🎯 Final Conclusion & Summary
- **Key Takeaways:** [breakdown conciso di cosa è emerso e perché conta]
- **Risk / Impact Assessment:** [se pertinente]
- **Recommendations:** [eventuali azioni suggerite, se il contesto lo richiede]

---

## 📎 Appendix
- **Raw Data Tables:** [link a tabelle separate — es. cronologia edit completa]
- **Tool Versions:** [versioni esatte degli strumenti usati, utile per riproducibilità]