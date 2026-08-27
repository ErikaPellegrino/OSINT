
# 💰 FININT Investigation Report — Template Completo

> Template guida generico. Cancellare le sezioni/voci non pertinenti al caso specifico, non lasciarle vuote nel report finale.

## 📋 Case Overview
- **Case ID:** [e.g., FININT-2026-001]
- **Analyst:** [Your Name / Alias]
- **Date of Analysis:** [YYYY-MM-DD]
- **Classification:** [TLP:CLEAR / TLP:AMBER / TLP:RED]
- **Category:** FININT
- **Sub-category / Focus:** [Corporate Financial Research / Crypto Wallet Tracing / Scam & Fraud Investigation / Sanctions Screening / Shell Company Analysis]
- **Confidence Level:** [High / Medium / Low]

---

## 📌 Bottom Line Up Front (BLUF)
> **Key Finding:** [1-2 frasi con l'esito principale — es. flusso fondi ricostruito, entità collegata identificata, esito verifica legittimità]

---

## 🎯 Target & Objective
- **Target Entity / Wallet / Transaction:** [nome azienda, indirizzo wallet, hash transazione, persona]
- **Primary Objective:** [es. "tracciare il flusso di fondi da un address poisoning scam" / "verificare la legittimità societaria di un'azienda" / "identificare collegamenti tra wallet"]
- **Investigation Type:** [Traditional Finance / Cryptocurrency / Hybrid]
- **Scope Boundaries:** [cosa è escluso — es. non si tenta l'identificazione reale del proprietario del wallet, solo il tracciamento dei fondi]

---

## 🛡️ Operational Security (OPSEC)
- **Risk Assessment:** [Low / Medium / High]
- **Tools & Environment:** [VM isolata, browser dedicato, VPN/Tor se necessario]
- **Wallet Interaction Policy:** [nessuna transazione/interazione con i wallet analizzati — solo osservazione]
- **Data Handling:** [gestione di dati finanziari sensibili, minimizzazione]

---

## 🔍 Initial Evidence & Input Data
- **Starting Point:** [indirizzo wallet, hash transazione, nome azienda, articolo di partenza]
- **Source of Lead:** [notizia, segnalazione pubblica, blockchain explorer, database aziendale]
- **Blockchain/Network Involved:** [Ethereum, Bitcoin, ecc. — o N/A se finanza tradizionale]

---

## 🧩 Investigation Steps

### A. Corporate & Registry Research *(se target è un'azienda/entità legale)*
- **Company Registration Data:** [registro camerale, VAT, data costituzione, sede legale]
- **Key People Identified:** [amministratori, soci, beneficiari effettivi — da fonti pubbliche]
- **Filings & Public Documents:** [bilanci pubblici, comunicati, filing SEC/Consob se applicabile]
- **Shell Company Indicators:** [sede in paradiso fiscale, nessuna attività reale visibile, amministratori "di comodo" ricorrenti su più aziende]

### B. Crypto Wallet & Transaction Tracing *(se target è un wallet/transazione)*
- **Wallet Address(es):** [elenco indirizzi coinvolti]
- **Explorer Used:** [Etherscan, Blockchain.com, Blockchair, ecc.]
- **Transaction Flow:** [ricostruzione del percorso dei fondi, hop per hop]
- **Mixing / Obfuscation Detected:** [tumbler, cross-chain bridge, exchange usati per confondere le tracce]
- **Endpoint Identified:** [exchange centralizzato, wallet finale, ancora in movimento]

```text
[Incollare indirizzi, hash transazione, query explorer usate]
```

### C. Wallet Clustering & Attribution *(se serve collegare più wallet alla stessa entità)*
- **Clustering Method:** [co-spending, pattern temporali, importi ricorrenti]
- **Related Wallets Found:** [elenco con motivazione del collegamento]
- **Known Entity Tags:** [se l'explorer/tool identifica già il wallet come noto — exchange, scam noto, ecc.]
- **Confidence Level per Collegamento:** [Alta/Media/Bassa]

### D. Scam / Fraud Pattern Analysis *(se il caso riguarda una truffa specifica)*
- **Scam Type:** [address poisoning, rug pull, phishing, Ponzi, romance scam, ecc.]
- **Victim Reports:** [segnalazioni pubbliche trovate — forum, Reddit, Twitter/X]
- **Modus Operandi:** [descrizione del meccanismo della truffa]
- **Estimated Financial Impact:** [importo totale stimato, se disponibile da fonti pubbliche]

### E. Sanctions & Watchlist Screening *(se rilevante per due diligence)*
- **Lists Checked:** [OFAC, EU Sanctions List, altre liste pubbliche]
- **Match Found:** [S/N — dettagli se sì]
- **Adjacent Risk Indicators:** [collegamenti indiretti con entità sanzionate]

### F. Source & Document Verification *(quasi sempre applicabile)*
- **Documents/Claims Checked:** [bilanci, comunicati, articoli citati come fonte]
- **Cross-referenced With:** [fonti indipendenti che confermano/smentiscono]
- **Verification Outcome:** [Confirmed / Partially Confirmed / False / Unverifiable]

---

## 🔒 Evidence Integrity
- **Capture Method:** [screenshot explorer, SingleFile per pagine registro/articoli]
- **Hashing:** [SHA-256 per ogni file/screenshot salvato]
- **Timestamping:** [UTC, riferimento a chain of custody separata — nota: per crypto, annotare anche il block height al momento dell'analisi, dato che i saldi possono cambiare]
- **Archived Versions:** [Wayback Machine per pagine web, nessun equivalente per dati blockchain — la blockchain stessa è il record immutabile]

---

## ✅ Evidence Validation
- **Data Integrity:** [dati on-chain sono verificabili direttamente/pubblicamente immutabili; dati off-chain necessitano verifica fonte]
- **Verification Status:** [Confirmed / Inconclusive / False Positive]
- **Cross-validation Method:** [più explorer/fonti indipendenti concordano?]

---

## ⚠️ Limitations
- [cosa non è stato possibile determinare — identità reale dietro wallet non attribuibile solo con OSINT, dati societari non pubblici in alcune giurisdizioni, ecc.]

---

## 🎯 Final Conclusion & Summary
- **Key Takeaways:** [sintesi di cosa è emerso e perché conta]
- **Financial Flow Summary:** [se applicabile — riepilogo sintetico del percorso dei fondi]
- **Risk / Impact Assessment:** [rischio finanziario, reputazionale, legale]
- **Recommendations:** [eventuali azioni suggerite, se il contesto lo richiede]

---

## 📎 Appendix
- **Raw Data Tables:** [link a tabelle separate — es. elenco completo transazioni, wallet correlati]
- **Tool Versions:** [versioni esatte degli strumenti/explorer usati]