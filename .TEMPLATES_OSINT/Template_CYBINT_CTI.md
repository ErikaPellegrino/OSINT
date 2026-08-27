
# 🛰️ CYBINT / CTI Investigation Report — Template Completo

> Template guida generico. Cancellare le sezioni/voci non pertinenti al caso specifico, non lasciarle vuote nel report finale.

## 📋 Case Overview
- **Case ID:** [e.g., CYBINT-2026-001]
- **Analyst:** [Your Name / Alias]
- **Date of Analysis:** [YYYY-MM-DD]
- **Classification:** [TLP:CLEAR / TLP:AMBER / TLP:RED]
- **Category:** CYBINT / CTI
- **Sub-category / Focus:** [Infrastructure Footprinting / Phishing Site Analysis / Malware IOC Research / Threat Actor Profiling / Data Leak Assessment]
- **Confidence Level:** [High / Medium / Low]

---

## 📌 Bottom Line Up Front (BLUF)
> **Key Finding:** [1-2 frasi con l'esito principale — es. infrastruttura attribuita, sito di phishing confermato, IOC collegati a campagna nota]

---

## 🎯 Target & Objective
- **Target Domain / IP / Hash / Actor:** [dominio, IP, hash file, alias threat actor]
- **Primary Objective:** [es. "mappare l'infrastruttura di un dominio di phishing" / "verificare se un IOC è collegato a una campagna nota" / "profilare un threat actor da fonti pubbliche"]
- **Investigation Type:** [Passive Recon / Infrastructure Analysis / Malware-related / Leak Analysis]
- **Scope Boundaries:** [cosa è escluso — es. nessuna interazione attiva con l'infrastruttura target, solo osservazione passiva]

---

## 🛡️ Operational Security (OPSEC)
- **Risk Assessment:** [Low / Medium / High]
- **Tools & Environment:** [VM isolata, VPN/Tor, browser dedicato — fondamentale qui più che altrove, dato che si toccano infrastrutture potenzialmente malevole]
- **Passive vs Active Recon:** [dichiarare esplicitamente se la ricerca è stata solo passiva o ha coinvolto richieste dirette al target]
- **Sandboxing:** [uso di ambiente isolato/sandbox per eventuale analisi file sospetti — mai eseguire su macchina reale]
- **Data Handling:** [gestione responsabile di eventuali dati trapelati trovati — non scaricare/diffondere dati personali di terzi]

---

## 🔍 Initial Evidence & Input Data
- **Starting Point:** [dominio, IP, hash, IOC, segnalazione]
- **Source of Lead:** [feed threat intel, segnalazione, notizia, campagna nota]
- **Related Campaign (if known):** [nome campagna/famiglia malware già documentata, se applicabile]

---

## 🧩 Investigation Steps

### A. Domain & Infrastructure Footprinting *(se applicabile)*
- **WHOIS Data:** [registrar, data registrazione, contatti se non privacy-protected]
- **DNS Records:** [A, MX, NS, TXT — pattern rilevanti]
- **Subdomain Enumeration:** [sottodomini trovati]
- **Hosting Provider / ASN:** [provider, ASN, paese]
- **SSL Certificate Analysis:** [issuer, data emissione, altri domini sullo stesso certificato]
- **Tooling:** [Shodan, Censys, crt.sh, VirusTotal, urlscan.io]

### B. Phishing / Malicious Site Analysis *(se applicabile)*
- **Target Impersonated:** [brand/servizio imitato]
- **Page Similarity:** [confronto con sito legittimo — elementi copiati, differenze]
- **Hosting Pattern:** [altri siti phishing sullo stesso hosting/IP]
- **Takedown Status:** [attivo / già rimosso / segnalato a chi]

### C. IOC & Malware Research *(se applicabile — solo ricerca OSINT, non analisi dinamica del malware)*
- **Indicators Collected:** [hash file (MD5/SHA256), IP, domini C2, URL]
- **Reputation Check:** [VirusTotal, AbuseIPDB, AlienVault OTX — risultati]
- **Known Family / Campaign Match:** [se i tool identificano una famiglia malware nota]
- **First Seen / Last Seen:** [date di prima e ultima osservazione pubblica dell'IOC]

### D. Threat Actor Profiling *(se applicabile — solo da fonti pubbliche)*
- **Alias(es) Used:** [nickname noti su forum/leak site]
- **Associated Infrastructure:** [domini, wallet, email collegati]
- **Public Attribution:** [attribuzioni già fatte da fonti pubbliche/report di settore — citare la fonte, non inventare attribuzioni proprie]
- **TTPs Observed:** [tecniche, tattiche, procedure osservate — mappabili a MITRE ATT&CK se pertinente]

### E. Data Leak / Breach Assessment *(se applicabile)*
- **Leak Source:** [dove è stato trovato — forum, paste site, marketplace]
- **Data Types Exposed:** [categorie di dati, senza riportare dati personali reali nel report]
- **Scale Estimate:** [numero record stimato, se dichiarato dalla fonte del leak]
- **Legitimacy Check:** [il leak è confermato reale o potenziale bufala/dati riciclati da leak precedenti?]

### F. Source & Attribution Verification *(quasi sempre applicabile)*
- **Claims Checked:** [affermazioni su attribuzione, gravità, novità della minaccia]
- **Cross-referenced With:** [report di vendor di sicurezza indipendenti, feed pubblici]
- **Verification Outcome:** [Confirmed / Partially Confirmed / Unverifiable]

---

## 🔒 Evidence Integrity
- **Capture Method:** [screenshot, SingleFile, export da tool — mai download/esecuzione di file sospetti su macchina reale]
- **Hashing:** [SHA-256 per ogni file/screenshot di prova, e per ogni IOC file analizzato]
- **Timestamping:** [UTC, riferimento a chain of custody separata]
- **Archived Versions:** [Wayback Machine / urlscan.io per pagine che potrebbero sparire rapidamente]

---

## ✅ Evidence Validation
- **Data Integrity:** [Verified direct source / Unverified third-party]
- **Verification Status:** [Confirmed / Inconclusive / False Positive]
- **Cross-validation Method:** [più tool/feed indipendenti concordano sullo stesso IOC/attribuzione?]

---

## ⚠️ Limitations
- [cosa non è stato possibile verificare — dati WHOIS privacy-protected, attribuzione incerta, IOC troppo generico, ecc.]

---

## 🎯 Final Conclusion & Summary
- **Key Takeaways:** [sintesi di cosa è emerso e perché conta]
- **Risk / Impact Assessment:** [rischio per potenziali vittime, diffusione, gravità]
- **Recommendations:** [es. segnalazione a CERT/registrar, azioni difensive suggerite — se il contesto lo richiede]

---

## 📎 Appendix
- **IOC List (structured):** [tabella riepilogativa hash/IP/domini per import in altri tool]
- **Raw Data / Tool Logs:** [link a note separate]
- **Tool Versions:** [versioni esatte degli strumenti usati]