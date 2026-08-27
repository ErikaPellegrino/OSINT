
# 📍 GEOINT Investigation Report — Template Completo

> Template guida generico. Cancellare le sezioni/voci non pertinenti al caso specifico, non lasciarle vuote nel report finale.

## 📋 Case Overview
- **Case ID:** [e.g., GEOINT-2026-001]
- **Analyst:** [Your Name / Alias]
- **Date of Analysis:** [YYYY-MM-DD]
- **Classification:** [TLP:CLEAR / TLP:AMBER / TLP:RED]
- **Category:** GEOINT
- **Sub-category / Focus:** [Geolocation from scratch / Location Verification / Fact-checking / Chronolocation / Multi-source Correlation]
- **Confidence Level:** [High / Medium / Low]

---

## 📌 Bottom Line Up Front (BLUF)
> **Key Finding:** [1-2 frasi con la risposta finale — location, coordinate, esito verifica. Il finding principale subito, senza girarci intorno.]

---

## 🎯 Target & Objective
- **Target Media / Claim:** [immagine, video, post social, affermazione da verificare]
- **Primary Objective:** [es. "geolocalizzare da zero l'evento raffigurato" oppure "verificare se la posizione dichiarata nel post corrisponde alla realtà"]
- **Investigation Type:** [Geolocation from scratch / Verification of a claimed location]
- **Scope Boundaries:** [cosa è escluso — es. non si verifica l'autenticità dell'account che ha pubblicato, solo il contenuto visivo]

---

## 🛡️ Operational Security (OPSEC)
- **Risk Assessment:** [Low / Medium / High]
- **Tools & Environment:** [VPN/Tor, browser isolato, VM dedicata, sock account]
- **Data Handling:** [sanificazione metadati/tracking prima dell'analisi, gestione di volti/dati personali visibili nel materiale]

---

## 🔍 Initial Evidence & Input Data
- **Source Material:** [URL, post social, nome file — indicare se singola immagine, video o set multiplo]
- **Original Media:** ![Target Image](./media/target_image.png)
- **Number of Items Analyzed:** [1 / più immagini / video — elencare se multipli]
- **Metadata (EXIF) Analysis:**
  - **Camera Model:** [N/A o dettagli]
  - **Timestamp:** [N/A o dettagli]
  - **GPS Data:** [Found / Stripped / Spoofed]
  - **Software Signature:** [eventuali tracce di editing/manipolazione]

---

## 🧩 Investigation Steps & Visual Analysis

### A. Visual Clues Identification *(quasi sempre applicabile)*
- **Landmarks & Architecture:** [edifici chiave, infrastrutture, insegne]
- **Environmental Factors:** [vegetazione, terreno, condizioni meteo, stagione apparente]
- **Text & Signage:** [lingue, loghi, targhe, cartelli stradali]
- **Human Elements:** [abbigliamento, comportamento, elementi culturali — solo se rilevanti e senza identificare persone reali]

### B. Cross-Referencing & Geolocation *(se geolocalizzazione da zero)*
- **Search Engines / Reverse Search:** [Yandex, Google Lens, TinEye — risultati]
- **Mapping & Satellite Imagery:** [Google Maps, OpenStreetMap, Overpass Turbo — query usate]
- **Candidate Locations:** [elenco ipotesi valutate, non solo quella finale — mostra il processo]
- **Elimination Reasoning:** [perché le ipotesi scartate non corrispondono]

```text
[Incollare coordinate, query, log dei tool]
```

### C. Location Verification *(se si parte da una posizione dichiarata da verificare)*
- **Claimed Location:** [posizione dichiarata dalla fonte originale]
- **Matching Landmarks Found:** [quanti e quali elementi confermano la posizione]
- **Discrepancies Found:** [eventuali elementi che NON corrispondono]
- **Verdict:** [Confermata / Smentita / Parzialmente confermata]

### D. Chronolocation & Temporal Analysis *(se rilevante determinare quando, non solo dove)*
- **Shadow Analysis:** [angolo ombra osservato vs atteso — SunCalc]
- **Sun Position Data:** [PeakFinder o simili, data/ora stimata]
- **Seasonal Indicators:** [vegetazione, neve, luce — coerenti con la data dichiarata?]
- **Estimated Date/Time Range:** [risultato finale della stima]

### E. Multi-Source / Multi-Image Correlation *(se più immagini/video dello stesso evento)*
- **Sources Compared:** [elenco fonti/media analizzati]
- **Consistency Check:** [le fonti raccontano la stessa scena/location/momento?]
- **Divergent Elements:** [differenze rilevate tra le fonti]
- **Most Reliable Source:** [quale fonte è più attendibile e perché]

### F. Confidence per Indizio *(consigliato per casi con più indizi di peso diverso)*
| Indizio | Tipo | Affidabilità (Alta/Media/Bassa) | Note |
|---|---|---|---|
| [es. cartello leggibile] | Testuale | Alta | |
| [es. tipo di vegetazione] | Ambientale | Media | |
| [es. nuvola/cielo generico] | Ambientale | Bassa | |

---

## 🔒 Evidence Integrity
- **Capture Method:** [screenshot, download diretto, SingleFile per post social]
- **Hashing:** [SHA-256 per ogni file originale analizzato]
- **Timestamping:** [UTC, riferimento a chain of custody separata]
- **Original Source Preservation:** [Wayback Machine / archive.today se contenuto social]

---

## ✅ Evidence Validation
- **Primary Proof:** [es. corrispondenza esatta Street View / immagine satellitare]
- **Verification Method:** [correlazione visiva diretta su 3+ landmark statici]
- **Verification Status:** [Verified / Inconclusive / Debunked]
- **Independent Cross-check:** [una seconda fonte/metodo conferma lo stesso risultato?]

---

## ⚠️ Limitations
- [cosa non è stato possibile determinare — risoluzione immagine insufficiente, nessun landmark univoco, metadati assenti, ecc.]

---

## 🎯 Final Conclusion & Coordinates
- **Exact Location / Coordinates:** `DD.DDDDD, DD.DDDDD` *(o N/A)*
- **Google Maps Link:** [Link](https://maps.google.com) *(o N/A)*
- **Estimated Date/Time:** [se applicabile, da sezione D]
- **Summary Verdict:** [sintesi finale, esito e livello di confidenza complessivo]

---

## 📎 Appendix
- **Raw Data / Tool Logs:** [link a note separate con log completi]
- **Tool Versions:** [versioni esatte usate, per riproducibilità]