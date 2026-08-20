
# 📍 GEOINT / OSINT Investigation Report

## 📋 Case Overview
- **Case ID:** OSINT-2023-006 (Gralhix - Sofia Santos Challenge)
- **Analyst:** Erika Pellegrino
- **Date of Analysis:** 2026-08-19
- **Classification:** TLP:CLEAR
- **Category:** GEOINT / Fact-Checking
- **Sub-category / Focus:** Image Verification & Misinformation Debunking
- **Confidence Level:** High

---

## 📌 Bottom Line Up Front (BLUF)
> **Key Finding:** The image shared on Twitter/X on January 19, 2023, claiming to show a recent TTP suicide attack in Khyber, Pakistan, is completely **fake and misleading**. The photo actually depicts a VBIED (car bomb) attack outside the *Al Sabah* newspaper office in the Waziriya district of Baghdad, Iraq, on **August 27, 2006**.

---

## 🎯 Target & Objective
- **Target Query / Domain:** Twitter post dated January 19, 2023, by a verified journalist (~140k followers) claiming a TTP attack in Pakistan.
- **Primary Objective:** Verify the authenticity, original source, timestamp, and geolocation of the image used in the tweet.

---

## 🛡️ Operational Security (OPSEC)
- **Risk Assessment:** Low
- **Tools & Environment:** Open-source search engines, browser-based reverse image tools, isolated research environment.
- **Data Handling:** Publicly available image analysis, metadata cross-referencing, sanitized search queries.

---

## 🔍 Initial Evidence & Input Data
- **Source Material:** [Sofia Santos OSINT Exercise #006 - Gralhix](https://gralhix.com/list-of-osint-exercises/osint-exercise-006/)
- **Target Image:** [Full visual analysis & side-by-side comparison available on Substack](https://erika124440.substack.com/p/geoint-case-study-debunking-misinformation?r=8wzskn&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true)
- **Archived Evidence:** N/A (Original tweet unavailable; image documentation included in Substack report)
- **Target Image Description:** Photo depicting a burning vehicle surrounded by heavy smoke and debris in front of a damaged concrete structure.
- **Metadata (EXIF) Analysis:**
  - **Camera Model:** N/A (Stripped via social media platform)
  - **Timestamp:** N/A (Stripped)
  - **GPS Data:** Stripped

---

## 🧩 Investigation Steps & Visual Analysis

### Step 1: Visual Clues Identification
- **Landmarks & Architecture:** Damaged concrete building structure, exposed support beams/pillars on the right, specific brick patterns, damaged street curb.
- **Environmental Factors:** Heavy smoke, burning vehicle frame, urban debris field.
- **Text & Signage:** No legible text in the primary target image.

### Step 2: Cross-Referencing & Geolocation
- **Reverse Image Search (TinEye & Google Images):**
  - TinEye yielded over 400 results. The earliest indexed stock image was found on **Alamy** titled `WaziriyaAutobombIrak`, with an original photo date of **August 27, 2006**.
  - **Wikimedia Commons** confirmed the identical image titled [`File:WaziriyaAutobombIrak.jpg`](https://commons.wikimedia.org/wiki/File:WaziriyaAutobombeIrak.jpg ), taken on **August 27, 2006**, by *U.S. Navy Mass Communication Specialist 2nd Class Eli J. Medellin*.
  - **WMD Center (NDU)** hosted the same photo attributed to an Al-Qaeda car bomb in Iraq.
- **Media Archives & Visual Correlation (Getty Images):**
  - Search query used: `"al sabah bomb" iraq`
  - Found multiple [Getty Images coverage](https://www.gettyimages.it/immagine/car-bomb-targets-iraqi-state-run-newspaper-in-baghdad) (photographed by *Wathiq Khuzaie*) documenting the scene of the car bomb outside the *Al Sabah* newspaper office in Baghdad, Iraq.
  - **Visual Match:** Cross-matched structural elements (concrete pillar, window frame alignment, wall texture) between the target image and Getty Images archive photos.

```text
Target Image Match Log:
--------------------------------------------------
Location:        Waziriya District, Baghdad, Iraq
Incident:        VBIED outside Al Sabah newspaper office
Date:            August 27, 2006
Photographer:    MC2 Eli J. Medellin (U.S. Navy)
False Claim Date: January 19, 2023 (TTP Attack, Khyber, Pakistan)
--------------------------------------------------
```
---

## ✅ Evidence Validation
- **Primary Proof:** Exact visual feature match with official U.S. Navy archive photos and historical Getty Images coverage from August 27, 2006.
- **Verification Method:** Direct visual correlation of 3+ static structural landmarks (concrete support beam, window cutout layout, adjacent wall structure).
- **Verification Status:** **Debunked** (The tweet used recycled 2006 media out of context).

---

## 🎯 Final Conclusion & Coordinates
- **Exact Location / Coordinates:** `33.3562, 44.3811` *(Waziriya District, Baghdad, Iraq - Approximate)*
- **Google Maps Link:** [Waziriya, Baghdad, Iraq](https://maps.google.com/?q=Waziriya+Baghdad+Iraq)
- **Summary Verdict:** 
  The claim made in the January 19, 2023 tweet is **false**. The photograph was taken over 16 years earlier, on August 27, 2006, in Baghdad, Iraq, following an Al-Qaeda VBIED attack on the *Al Sabah* newspaper office that destroyed over 20 vehicles. It has no connection to Pakistan or the TTP.
 

📖 Full Visual Walkthrough & Article:

Read the complete breakdown with detailed side-by-side image comparison on my Substack Article: https://erika124440.substack.com/p/geoint-case-study-debunking-misinformation?r=8wzskn&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true