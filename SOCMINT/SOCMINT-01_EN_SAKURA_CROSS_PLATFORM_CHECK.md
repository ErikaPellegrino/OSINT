# 👤 SOCMINT Investigation Report — SakuraSnowAngelAiko

## 📋 Case Overview
- **Case ID:** SOCMINT-01_SAKURA_CROSS_PLATFORM_CHECK
- **Analyst:** Erika Pellegrino
- **Date of Analysis:** 28/08/2026 - 30/08/2026
- **Classification:** TLP:CLEAR 
- **Category:** SOCMINT
- **Sub-category / Focus:** Username Enumeration, Cross-Platform Correlation, Manual Verification
- **Confidence Level:** Medium-High *(varies by platform — see verdicts by individual account below)*
- **Substack:** [link]

---

## 📌 Bottom Line Up Front (BLUF)
> **Key Finding:** Of 6 elements analyzed (4 direct Sherlock hits + 2 accidental discoveries), 2 were confirmed with triple independent validation (GitHub, X/Twitter — both traceable to the TryHackMe CTF scenario), while Telegram, TikTok, YouTube and Instagram produced, respectively, unverifiable, inconclusive, false positive and homonymy noise outcomes. Full hash log, raw tool output and evidence material are available in this repository.

---

## 🎯 Target & Objective
- **Target Account(s) / Handle(s):** SakuraSnowAngelAiko (GitHub, Telegram, TikTok, YouTube handle); @SakuraLovesAiko (X — different handle, found via content match); Instagram "Sakurasnowangelaiko" (homonymy noise)
- **Primary Objective:** Verify, through username enumeration and cross-platform correlation techniques, the presence and authenticity of accounts linked to the target username SakuraSnowAngelAiko
- **Platform(s) Involved:** GitHub, Telegram, TikTok, YouTube, X/Twitter, Instagram
- **Scope Boundaries:** No decoding of the public key found in the GitHub repository; no in-depth verification of the 6 additional Maigret-only hits (Teletype, ChaturBate, xHamster, fixya, Pling, GitHub Gist) beyond typology classification; no sockpuppet or intrusive techniques; the suspected AI-generated "Chinese" account linked from X was not investigated further

---

## 🛡️ Operational Security (OPSEC)
- **Risk Assessment:** Low
- **Sock Account Used:** No — deliberately excluded from scope
- **Tools & Environment:** Isolated virtual machine (VirtualBox, Kali Linux); Firefox with UA Switcher and uBlock Origin extensions; mobile hotspot (avoids exposing home IP)
- **Interaction Policy:** No login, no interaction with any target platform — passive OSINT only
- **Data Handling:** Screenshots and hashes stored in a dedicated folder; third-party visual content not pertinent to the investigation blurred before publication

---

## 🔍 Initial Evidence & Input Data
- **Starting Point:** Username "SakuraSnowAngelAiko"
- **Account Overview:** See per-platform findings below (Investigation Steps)
- **Cross-platform Presence:** Confirmed on GitHub and X/Twitter; inconclusive/unverifiable on TikTok and Telegram; false positive on YouTube; homonymy noise on Instagram
- **Search Engines Used:** DuckDuckGo
- **Specialized Platforms / Tools Used:** Sherlock, Maigret, GoFullPage, Wayback Machine

---

## 🧩 Investigation Steps

### A. Profile Authenticity Check

**A.1 GitHub — Verdict: Confirmed (profile for TryHackMe CTF)**
- Account Age vs Activity Level: created 2021-01-23 (Maigret data); no active contributions in the last year
- Profile Picture Verification: not reverse-searched (not needed — corroborated by three independent sources)
- Bio & Username Analysis: display name "Aiko", distinct from full handle "SakuraSnowAngelAiko" — normal GitHub behavior, no anomaly; bio absent; 274 followers; 0 following; 9 public repositories (5 pinned); several with cryptocurrency-related content
- Posting Pattern: N/A (code repository, not a social feed)
- Additional finding: a repository contains a Stratum mining configuration string (`stratum://ethwallet.workerid:password@miningpool:port`) — standard template syntax, not a functioning credential; another repository contains a public key (not decoded, out of scope)
- Cross-validation: Sherlock hit + manual verification + Maigret extended data (UID 77871458, creation date, follower/following counts, fullname) — all three converge

**A.2 YouTube — Verdict: False positive**
- Direct navigation returns 404 Not Found
- Dork search ("SakuraSnowAngelAiko" Youtube) returned no cache/archived version or external mentions
- Assessed as a likely Sherlock false positive (HTTP response code misinterpretation), a documented behavior for some platforms
- Led to the accidental discovery of the Instagram account (A.6) via a search-engine query typo

**A.3 TikTok — Verdict: Inconclusive**
- Direct navigation blocked by a login wall
- `site:tiktok.com SakuraSnowAngelAiko` dork: similar but non-identical usernames only
- Broader dork `SakuraSnowAngelAiko "tiktok"`: no relevant results
- Distinguished from a tool false positive: here the platform itself denies access to unauthenticated users regardless of actual profile existence; further limited by the deliberate choice not to use sockpuppets

**A.4 Telegram — Verdict: Unverifiable**
- Channel created 17 November 2025 (years after the GitHub account)
- Fullname: "?"; 15 subscribers; profile image absent (Maigret confirms an auto-generated SVG placeholder)
- Three messages, all from the same sender ("?"): one image (screenshot of a conversation with a "Deleted Account" interlocutor) captioned in Russian "скучаю" ("I miss [you/something]"), plus two further Russian-language comments
- The image shows 396 views and 4 strawberry-emoji reactions, disproportionate to the channel's 15 subscribers
- Note: only the absence of a real profile picture is a Telegram-specific Maigret data point; the "country: ru" and "porn" tag are aggregate figures across the full Maigret search, not Telegram-specific — reported as corroborating but not conclusive
- Additional convergent indicators: Teletype (a Russian platform) among the Maigret hits; two further Maigret hits linked to the "porn" tag (ChaturBate, xHamster)
- No certainty can be claimed on the nature of the channel's content

**A.5 X/Twitter — Verdict: Confirmed (profile for TryHackMe CTF) — Accidental discovery**
- Found by chance: a URL entry error (GitHub's URL was pasted into the search engine instead of the address bar) surfaced this account among the top DuckDuckGo results
- Handle: @SakuraLovesAiko — different from the target username; found through content match on the name "Aiko", not an exact username hit
- Confirmed via `site:x.com SakuraSnowAngelAiko` dork, since the GitHub profile carried no direct reference to X
- Content contains clues for the TryHackMe CTF, consistent with the GitHub profile's role
- No direct link back to GitHub found on the profile
- One link on the profile leads to a likely AI-generated "Chinese" account — not investigated further, judged out of scope
- Tooling note: neither Sherlock (~400 known sites) nor Maigret (3,000+ sites) surfaced this account despite X being a major platform — most likely explained by automated verification being blocked by X itself, a limit only manual search could overcome

**A.6 Instagram — Verdict: Homonymy noise — Accidental discovery**
- Found via a dork search related to the YouTube verification (search engine query, not intended)
- Username identical to the target; no visible profile picture
- Bio content copied verbatim from the English Wikipedia article on **Sakura Miko**, a real Japanese VTuber affiliated with Hololive Production — a public figure unrelated to the didactic target
- Source archived via Wayback Machine (29/08/2026) as a citation reference: https://web.archive.org/web/20260829085050/https://en.wikipedia.org/wiki/Sakura_Miko. 
- Assessed as username coincidence, not shared identity — a documented OSINT pattern (fan/tribute accounts, traffic-generation via a well-known name)
- **Ethical note:** as the account is plausibly linked to a real, private individual (unlike the public figure Sakura Miko), potentially identifying visual content (reel thumbnails) was blurred prior to publication

---

## 🔒 Evidence Integrity
- **Capture Method:** Full-page screenshots via the GoFullPage browser extension (PNG)
- **Hashing:** SHA-256, computed with `sha256sum`, logged cumulatively in `hash_log.txt`
- **Timestamping:** No certified timestamping service was used; temporal references rely on file system metadata and log-recorded dates
- **Archived Versions:** Applied only to the external cited source (Wikipedia page, via Wayback Machine); primary evidence has no redundant backup beyond the local copy

---

## ✅ Evidence Validation
- **Data Integrity:** Verified direct source for all platforms navigated directly (address bar, not search results)
- **Verification Status:** Confirmed (GitHub, X/Twitter) / False Positive (YouTube) / Inconclusive (TikTok) / Unverifiable (Telegram) / Homonymy noise (Instagram)
- **Cross-validation Method:** Sherlock + Maigret comparison; three independent sources converge on GitHub (tool hit, manual verification, Maigret extended data)

---

## ⚠️ Limitations
- Primary tool false positive rate: 1 of 4 Sherlock hits (25%), consistent with documented Sherlock behavior on platforms like YouTube
- Platform-imposed limits: TikTok's login wall made full passive verification impossible, a direct cost of the deliberate choice not to use sockpuppets
- Secondary tool technical limits: Maigret reported a combined error rate of 9.82% ("bot protection" + "request failed"), meaning a share of automated results remains unverifiable even with a second tool
- Likely automated-verification blocking imposed by X, preventing either tool from surfacing the confirmed X account
- Deliberately excluded from scope: decoding of the GitHub public key; deep verification of the 6 Maigret-only hits beyond typology; the suspected AI-generated account linked from X

---

## 🎯 Final Conclusion & Summary
- **Key Takeaways:** The GitHub profile is the strongest evidence collected, benefiting from triple independent validation and an additional behavioral finding (cryptocurrency mining configuration). The Telegram profile, while not fully confirmable, produced the investigation's most significant geographic/linguistic indicator (Russian language), independently corroborated by Maigret's aggregate data. The investigation confirms a core SOCMINT principle: username coincidence across platforms is not proof of shared identity (Instagram case). It also surfaces a methodologically relevant distinction between a tool false positive (YouTube) and an inconclusive result due to an external platform limit (TikTok).
- **Risk / Impact Assessment:** Not applicable — didactic, fictional target; no real-world risk or impact.
- **Recommendations:** None required — exercise scope fully addressed within the defined boundaries.

---

## 📎 Appendix
- **Raw Data Tables:** Full hash log (`hash_log.txt`), raw tool output (`risultati_grezzi.txt`, `maigret_risultati_grezzi.txt`) and evidence screenshots available in this repository: [link]
- **Tool Versions:** Sherlock 0.16.0; Maigret 0.6.4;
