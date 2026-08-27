# 🌐 WEBINT Investigation Report

OSINT Analysis of a Wikipedia Article's Edit History: Identification of Suspicious Editing Patterns and Source Verification

## 📋 Case Overview
- **Case ID:** WEBINT-01 — wiki_article_edit_history (Project Veidt Enterprises)
- **Analyst:** Erika Pellegrino
- **Date of Analysis:** 2026-08
- **Classification:** TLP:CLEAR
- **Category:** WEBINT
- **Sub-category / Focus:** Wiki History Analysis / Source Verification
- **Confidence Level:** High
- **SUBSTACK:** Full article available at https://erika124440.substack.com/p/analisi-della-cronologia-di-una-voce?r=8wzskn
---

## 📌 Bottom Line Up Front (BLUF)
- **Executive Summary:** Analysis of the full revision history (50 edits, 40 distinct editors) of the Wikipedia page for Veidt Enterprises revealed no systematic editorial manipulation favoring the company, nor organized defamatory campaigns against it. The most notable edit cluster (rows 13–17) contained two isolated, independent incidents — unsourced favorable content and an unfounded fraud allegation — both corrected by the Wikipedia community per standard verifiability policy. One seemingly unreachable citation (row 18) was confirmed, after further investigation, to be a legitimate source whose original page is offline due to site reorganization.

---

## 🎯 Target & Objective
- **Target Query / Domain / Entity:** Wikipedia article for "Veidt Enterprises" (anonymized tech company)
- **Primary Objective:** Identify suspicious editing patterns — specifically Conflict of Interest (COI) editing — and verify the reliability of the sources cited in the article
- **Secondary Objectives:** Identify potential edit wars or retaliatory edits between contributors
- **Scope Boundaries:** Geolocation and network attribution of the IP addresses involved were explicitly excluded from this investigation's scope

---

## 🛡️ Operational Security (OPSEC)
- **Risk Assessment:** Low
- **Environment:** VirtualBox virtual machine running Kali Linux, Firefox browser
- **Browser Hardening:** User-Agent Switcher and uBlock Origin extensions active
- **Network Precautions:** Not required (consultation of public content; no interaction with sensitive infrastructure)
- **Data Handling:** SingleFile, GoFullPage, Wayback Machine, SHA-256 hashing
- **Chain of Custody:** Maintained in Obsidian throughout the investigation; see Appendix for a representative excerpt

---

## 🔍 Initial Evidence & Input Data
- **Starting Point:** Wikipedia article of tech company "Veidt Enterprises"
- **Search Engines Used:** DuckDuckGo, Bing, Google
- **Specialized Platforms Used:** Wayback Machine, XTools (Wikipedia edit statistics), MediaWiki Public API

---

## 🧩 Investigation Steps

### A. Edit History / Timeline Analysis
- **Total Edits Analyzed:** 50
- **Time Period Covered:** 2020-06-29 to 2026-08-19
- **Key Contributors:** 40 distinct editors — a near 1:1 editor-to-edit ratio, indicating no single dominant contributor
- **Suspicious Temporal Clusters:** Rows 13–17 showed concentrated activity within a short timeframe; on closer inspection, this resolved into two distinct, unrelated incidents rather than one coordinated sequence
- **Reference Table:** Full edit history extracted via the `wiki_history_fetch` Python script (MediaWiki API); see Appendix for an excerpt of rows 13–17

### B. Contributor / Editor Profiling
- **Account Age & Activity:** Not systematically profiled beyond the flagged rows — out of scope for the routine (non-flagged) 90%+ of edits
- **Single-purpose Accounts (SPA):** None identified among flagged rows
- **Possible Sockpuppets:** None found. The masked-IP edits reviewed (e.g., three consecutive same-day edits from one masked IP) were confirmed via diff review to be ordinary multi-step editing by a single contributor, not coordinated sockpuppeting
- **Anonymous IP Analysis:** Rows 13–14 (masked IP) and rows 16–17 (two different anonymous IPs) were reviewed at the content level; no network-level or geolocation attribution was performed (see Scope Boundaries)
- **External Cross-reference:** Not applicable — no usernames warranted external cross-referencing (e.g., LinkedIn, dorking on editor names)

### C. Source & Claim Verification
- **Claims Checked:**
  - Row 18: claim that a company app surpassed 300 million downloads, citing "Evening Future" (eveningfuture.com)
  - Rows 13–15: claim regarding corporate acquisitions, added by an anonymous IP without citation
  - Rows 16–17: claim alleging fraudulent practices / unauthorized billing (€9.99/week)
- **Sources Cross-referenced:** Acme Group portal, independent news outlets, search engine dorks
- **Advanced Search Operators (Dorks) used:**
  ```text
  Original (Italian):
  "300 milioni di download" AND "Veidt Enterprises" site:eveningfuture.com

  English translation:
  "300 million downloads" AND "Veidt Enterprises" site:eveningfuture.com
  ```
  ```text
  site:acmegroup.com "Veidt Enterprises"
  ```
  ```text
  Original (Italian):
  "Veidt Enterprises" (addebito OR abbonamento OR "9,99") (truffa OR frode OR "non autorizzato") -site:it.wikipedia.org -site:veidtenterprises.com

  English translation:
  "Veidt Enterprises" (charge OR subscription OR "9.99") (scam OR fraud OR "unauthorized") -site:it.wikipedia.org -site:veidtenterprises.com
  ```
- **Archived Versions:** Wayback Machine checked for the specific eveningfuture.com URL — no snapshot found; main article baseline separately archived on Wayback Machine (see Evidence Integrity)
- **Verification Outcome per Claim:**
  - *300 Million Downloads (Row 18):* Confirmed. Source exists as a genuine editorial column under the Acme Group; the specific 2020 URL is broken due to site restructuring ("link rot"), not fabrication
  - *Acquisitions (Rows 13–15):* Unverifiable / Removed. Content was factually plausible but removed per policy due to lack of inline citations — no evidence of manipulation
  - *Fraud Allegations (Rows 16–17):* Unsubstantiated. No public records or complaints matching Veidt Enterprises were found; the content was removed by the community as non-encyclopedic and unverified. Absence of external corroboration supports, but does not conclusively prove, that the allegation was baseless

---

## 🔒 Evidence Integrity
- **Capture Method:** SingleFile (full HTML with embedded assets) and GoFullPage (lossless PNG screenshots) for key pages; revision data extracted via the public MediaWiki API using the custom `wiki_history_fetch` Python script
- **Hashing:** SHA-256 computed via Kali terminal (`sha256sum`) for every collected file, logged in the Chain of Custody
- **Timestamping:** UTC timestamps recorded for all collection actions; filesystem metadata recovered via the `stat` command where the capture time was not otherwise visible
- **Redundant Storage:** Wayback Machine snapshot generated for the main article baseline; omitted for the History page, as past revision rows are immutable and do not require independent archiving

---

## ✅ Evidence Validation
- **Data Integrity:** Verified against the direct source and cross-validated via the MediaWiki public API
- **Verification Status:** Confirmed — normal community moderation behavior, no evidence of active COI editing or edit warring
- **Cross-validation Method:** Independent search engine dorks across three engines (Google, Bing, DuckDuckGo), cross-referenced against broader news coverage

---

## ⚠️ Limitations
- IP addresses involved were not subjected to network or geolocation attribution — explicitly out of scope
- Routine edits (bots, cosmetic fixes, Wikidata syncs) received rapid screening rather than a full diff-by-diff review
- The original content of the "Evening Future" article could not be retrieved, as it is no longer hosted or archived
- The external check on the fraud allegation yielded an absence of corroborating evidence, not an active refutation — this supports but does not conclusively prove the allegation was unfounded

---

## 🎯 Final Conclusion & Summary
- **Key Takeaways:** 50 edits by 40 distinct editors show standard, healthy community moderation. Both unsourced favorable content and unsourced hostile content were promptly corrected under the same verifiability rules. A citation that initially appeared broken was confirmed genuine, affected only by link rot.
- **Risk / Impact Assessment:** Low reputational risk. The current entry is well-monitored by the community; potentially damaging edits were reverted within hours.
- **Recommendations:** For staff managing the company's public profile — add verifiable inline citations to the "Acquisitions" section to prevent accurate but unsourced content from being removed again in the future.

---

## 📎 Appendix
- **Raw Data Tables:**

  *Chain of Custody (excerpt):*

  | Timestamp (UTC) | File Name | Description | Capture Method | SHA-256 Hash |
  |---|---|---|---|---|
  | 2026-08-19 14:00:00 | `20260819_140000_UTC_Veidt_Enterprises_Main.html` | Initial Wikipedia article baseline | SingleFile | `9f3a1c7e2b8d4560af12e3d9c6b7a8451f0e2d3c4b5a6978012345abcde6789` |
  | 2026-08-19 14:05:00 | `20260819_140500_UTC_Veidt_Enterprises_Main.png` | Full-page screenshot baseline | GoFullPage | `4b7e9a2f1c3d5e6078901234abcdef56789012345bcdef0123456789abcde12` |
  | 2026-08-19 14:20:00 | `20260819_142000_UTC_Veidt_Enterprises_History.html` | Wikipedia edit history page | SingleFile | `1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f60718293a4b5c6d7e8f90123456789abc` |

  *(Hashes shown are illustrative placeholders, not the real values from the original investigation.)*

  *Edit History Table — Block 13–17 (fictionalized data):*

  | Row | Timestamp (UTC) | Editor | Registered | Δ Bytes | Tag / Comment | Flagged | Notes |
  |---|---|---|---|---|---|---|---|
  | 13 | 2024-08-23 10:15 | IP (masked) | No | +450 | Added "Acquisitions" section | Yes | Added acquisition data without citations |
  | 14 | 2024-08-23 10:22 | IP (masked, same) | No | +120 | Minor formatting | Yes | Follow-up edit to the acquisitions section |
  | 15 | 2024-09-15 11:05 | User_Editor1 | Yes | -570 | Reverted edits: missing sources | No | Reverted rows 13–14 due to lack of verifiability |
  | 16 | 2024-09-27 08:24 | IP (different) | No | +285 | Fraud allegation | Yes | No citation, non-encyclopedic tone |
  | 17 | 2024-09-27 14:54 | IP (different) | No | -285 | "Removed unverified information" | No | Legitimate removal |

- **Tool Versions:** SingleFile and GoFullPage (Firefox extensions, versions as installed at time of analysis); Python 3 with the `requests` library for `wiki_history_fetch`; Kali Linux default toolset (`sha256sum`, `stat`, `nano`)
