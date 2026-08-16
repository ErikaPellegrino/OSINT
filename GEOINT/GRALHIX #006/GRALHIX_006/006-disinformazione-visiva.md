# Verifica OSINT: Disinformazione Visiva — Attacco TTP a Khyber (Gralhix Exercise #006)

> 🔴 **VERDETTO: FALSO — Decontestualizzazione confermata.** L'immagine non ritrae un attacco TTP a Khyber (Pakistan, 2023), ma un attentato con autobomba a Baghdad (Iraq, 2006).

**Livello di confidenza:** ALTO
**Tipo di esercizio:** Training exercise (Gralhix.com) — non un'indagine operativa reale.

---

## Sommario

- [TL;DR](#tldr)
- [Metadati e Sintesi Esecutiva](#metadati-e-sintesi-esecutiva)
- [Task Originale](#1-exercise-006-gralhixcom)
- [Metodologia e Tools](#tools--skills-used)
- [Workflow dell'Indagine](#2-cronologia-ed-esecuzione-dellindagine-workflow)
- [Conclusioni](#3-conclusioni-finali)
- [Limitazioni](#limitations--disclaimer)
- [Fonti](#fonti)

---

## TL;DR

Il 19 gennaio 2023 un account Twitter/X verificato ha attribuito un'immagine di distruzione a un presunto attacco suicida della TTP a Khyber, Pakistan. La verifica tramite reverse image search e Google Dorking ha dimostrato che la foto risale al **27 agosto 2006** e documenta un'autobomba (VBIED) contro la sede del quotidiano *Al Sabah* a Baghdad, Iraq — un caso di **media out-of-context**.

---

## Metadati e Sintesi Esecutiva

| Campo | Dettaglio |
|---|---|
| **Oggetto dell'Analisi** | Verifica di autenticità e contesto di un'immagine condivisa su Twitter/X (19 gennaio 2023). |
| **Affermazione Analizzata** | Attacco suicida del gruppo TTP ad una postazione di polizia a Khyber (Pakistan), con 3 vittime. |
| **Esito dell'Indagine** | FALSO. L'immagine risale al 27 agosto 2006 e documenta un attacco con autobomba (VBIED) contro la sede del quotidiano Al Sabah a Baghdad, Iraq. |
| **Livello di Confidenza** | ALTO |
| **Metodologia Applicata** | Reverse Image Search (Tineye, Google), Google Dorking, Comparazione fotografica (geolocation - visual matching) |

---

## 1. Exercise #006, Gralhix.com

**TASK:**

On January 19, 2023, a journalist with almost 140k followers on Twitter shared an image of a destroyed vehicle amidst a large cloud of smoke and fire. The tweet said: *"#BREAKING: TTP carried out a suicide attack on a police post in Khyber city of Pakistan that killed three Pakistani police officers."*

The photo is not of the event described by the journalist.

a) Verify the statement above.

### Affermazione Iniziale

Il 19 gennaio 2023, un account Twitter/X verificato ha pubblicato una fotografia raffigurante alcune carcasse di automobili avvolte tra le fiamme e il fumo. Intorno si possono vedere edifici distrutti e la strada sterrata è piena di detriti.

> *Task image. Credit: Gralhix*

L'immagine twittata è accompagnata dal seguente testo:

> "#BREAKING: TTP carried out a suicide attack on a police post in Khyber city of Pakistan that killed three Pakistani police officers."

**TRADUZIONE** > "#BREAKING: La TTP ha condotto un attacco suicida contro una postazione della polizia nella città di Khyber, in Pakistan, uccidendo tre agenti di polizia pakistani."

L'uso del tag "#BREAKING" e la spunta di verifica dell'account hanno conferito al post un'elevata viralità, attribuendo l'evento al gruppo Tehrik-e Taliban Pakistan (TTP) in territorio pakistano.

Lo scopo dell'esercizio è verificare i fatti esposti nel tweet.

---

## Tools & Skills Used

- **TinEye** — reverse image search
- **Google Images / Google Lens** — reverse image search e validazione documentale
- **Google Dorking** — ricerca mirata con query avanzate
- **Comparazione fotografica (visual matching)** — analisi di elementi architettonici/strutturali per la geolocalizzazione
- **Cross-referencing fonti aperte** — Wikimedia Commons, archivi governativi (NDU/WMD Center), agenzie fotografiche (Getty Images, Alamy)

---

## 2. Cronologia ed Esecuzione dell'Indagine (Workflow)

### Fase 1: Reverse Image Search Iniziale (TinEye)

La ricerca inversa condotta tramite il motore TinEye ha restituito 435 risultati. L'indicizzazione più remota registrata dal sistema risale al 4 novembre 2009, ma tra i risultati è emerso un link sponsorizzato del catalogo stock Alamy contenente il file dal titolo "WaziriyaAutobombeIrak", con data di scatto dichiarata: 27 agosto 2006. *(vedi [Fonti](#fonti) [1])*

Per capire il motivo dell'incongruenza, con una veloce ricerca si è risaliti alla fondazione di TinEye che risulta essere maggio 2008, perciò non risultano scansioni prima di questa data.

### Fase 2: Validazione Documentale e Fonti Primarie (Google Lens)

Per confermare la data del 2006 e fugare ogni dubbio sull'origine dell'immagine, sono state interrogate banche dati aperte e archivi governativi ufficiali risultate dalla reverse image search tramite google:

Trovo il tweet originale dell'esercizio con il nome del giornalista visibile; per questione di privacy non verrà menzionato.

**Risultati rilevanti:**

- **Wikimedia Commons:** Conferma la presenza del file WaziriyaAutobombeIrak.jpg con data di creazione 27 agosto 2006. La descrizione riporta un'esplosione VBIED davanti all'ufficio del quotidiano Al Sabah nel distretto di Waziriya a Baghdad, Iraq. *(vedi [Fonti](#fonti) [2])*

  Credit ufficiale: U.S. Navy photo by Mass Communication Specialist 2nd Class Eli J. Medellin.

- **WMD Center / NDU (National Defense University):** Ripropone il medesimo scatto con ID identificativo VIRIN: 160303-D-BD341-008.JPG, attribuito allo stesso fotografo militare (MC2 Eli J. Medellin), confermando il contesto operativo iracheno (Al-Qaeda in Iraq). *(vedi [Fonti](#fonti) [3])*

### Fase 3: Google Dorking e Visual Matching

Utilizzando una semplice stringa di ricerca:

```
"al sabah bomb" iraq
```

Sono state individuate molteplici fotografie di reportage scattate il 27 agosto 2006 dal fotoreporter Wathiq Khuzaie (Getty Images) nello stesso luogo dell'evento. *(vedi [Fonti](#fonti) [4])*

Si riporta la conferma visiva della corrispondenza tra la foto del tweet e gli scatti d'archivio (Task image credit: Gralhix; immagini dal luogo raffigurato credit: Wathiq Khuzaie/Getty Images).

L'analisi comparativa tra la foto del tweet e gli scatti d'archivio di Getty Images conferma l'identità del luogo attraverso la sovrapposizione di elementi architettonici e strutturali unici:

| Elemento Identificato | Foto Tweet (19/01/2023) | Foto d'Archivio Getty (27/08/2006) | Esito Match |
|---|---|---|---|
| Autoveicolo distrutto | Carcassa bruciata in primo piano. | Telaio metallico deformato dall'esplosione. | Coincidente |
| Travi strutturali | Trave obliqua pendente sul lato destro. | Stessa inclinazione e struttura di supporto dell'edificio. | Coincidente |
| Muro edificio circostante | Particolare di muratura a blocchi con apertura. | Facciata dell'edificio del quotidiano | Coincidente |

I dettagli strutturali non lasciano alcun margine di dubbio: la scena ritratta nel tweet del 2023 è esattamente la stessa ripresa dai fotografi militari e dai reporter di guerra a Baghdad nel 2006.

---

## 3. Conclusioni Finali

1. **Falsità del Contenuto:** La notizia diffusa il 19 gennaio 2023 sul presunto attacco a Khyber (Pakistan) è corredata da un'immagine priva di pertinenza temporale e geografica.
2. **Classificazione dell'Inganno:** Si tratta di un'operazione di media out-of-context (decontestualizzazione visiva), in cui materiale d'archivio reale del conflitto iracheno del 2006 è stato riciclato per simulare un evento recente nel subcontinente indiano.
3. **Valutazione Fonti:** L'account Twitter/X, pur essendo verificato e seguito da un vasto pubblico, ha pubblicato materiale non verificato, contribuendo alla diffusione di disinformazione.

---

## Limitations / Disclaimer

- Questo report è basato su un **training exercise** (Gralhix #006), non su un'indagine professionale commissionata.
- La verifica si basa esclusivamente su **fonti pubbliche aperte** (reverse image search, archivi web, agenzie fotografiche); non è stato possibile analizzare i metadati EXIF originali del file caricato dall'account Twitter/X.
- Il nome dell'account/giornalista che ha pubblicato il tweet è stato omesso per tutela della privacy.
- Il livello di confidenza "ALTO" riflette la coerenza tra più fonti indipendenti (Wikimedia, NDU, Getty), non una verifica forense certificata.

---

## Fonti

1. Alamy — *WaziriyaAutobombeIrak*: https://www.alamy.com/waziriyaautobombeirak-image574866988.html
2. Wikimedia Commons — *File:WaziriyaAutobombeIrak.jpg*: https://commons.wikimedia.org/wiki/File:WaziriyaAutobombeIrak.jp
3. WMD Center / NDU — VIRIN 160303-D-BD341-008: https://wmdcenter.ndu.edu/Media/Images/igphoto/2002493919/
4. Getty Images — *Car bomb targets Iraqi state-run newspaper in Baghdad*: https://www.gettyimages.it/immagine/car-bomb-targets-iraqi-state-run-newspaper-in-baghdad

---

*Report basato sull'esercizio Gralhix #006 (gralhix.com).*
