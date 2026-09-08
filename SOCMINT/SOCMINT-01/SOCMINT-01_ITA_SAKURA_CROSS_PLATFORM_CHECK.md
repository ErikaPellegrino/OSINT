# 👤 Report di Investigazione SOCMINT — SakuraSnowAngelAiko

## 📋 Panoramica del Caso
- **ID Caso:** SOCMINT-01_SAKURA_CROSS_PLATFORM_CHECK
- **Analista:** Erika Pellegrino
- **Data dell'Analisi:** 28/08/2026 - 30/08/2026
- **Classificazione:** TLP:CLEAR 
- **Categoria:** SOCMINT
- **Sotto-categoria / Focus:** Username Enumeration, Cross-Platform Correlation, Manual Verification
- **Livello di Confidenza:** Medio-Alto *(varia per piattaforma — vedi verdetti per singolo account più sotto)*
- **Substack:** https://erika124440.substack.com/p/username-enumeration-cross-platform

---

## 📌 Bottom Line Up Front (BLUF)
> **Risultato Chiave:** Su 6 elementi analizzati (4 hit diretti di Sherlock più 2 scoperte accidentali), 2 sono stati confermati con triplice validazione indipendente (GitHub, X/Twitter — entrambi riconducibili allo scenario CTF TryHackMe), mentre Telegram, TikTok, YouTube e Instagram hanno prodotto rispettivamente esiti non verificabile, inconcludente, falso positivo e rumore da omonimia. Log hash completo, output grezzi degli strumenti e materiale di evidenza sono disponibili in questo repository.

---

## 🎯 Target e Obiettivo
- **Account / Handle Target:** SakuraSnowAngelAiko (handle su GitHub, Telegram, TikTok, YouTube); @SakuraLovesAiko (X — handle diverso, trovato per corrispondenza di contenuto); Instagram "Sakurasnowangelaiko" (rumore da omonimia)
- **Obiettivo Primario:** Verificare, tramite tecniche di username enumeration e correlazione cross-platform, la presenza e l'autenticità di account collegati all'username target SakuraSnowAngelAiko
- **Piattaforme Coinvolte:** GitHub, Telegram, TikTok, YouTube, X/Twitter, Instagram
- **Confini dell'Ambito:** Nessuna decodifica della chiave pubblica trovata nel repository GitHub; nessuna verifica approfondita dei 6 hit aggiuntivi rilevati solo da Maigret (Teletype, ChaturBate, xHamster, fixya, Pling, GitHub Gist) oltre alla classificazione per tipologia; nessuna tecnica sockpuppet o intrusiva; l'account sospetto probabilmente generato con IA collegato ad X non è stato approfondito

---

## 🛡️ Sicurezza Operativa (OPSEC)
- **Valutazione del Rischio:** Basso
- **Account Sock Utilizzato:** No — escluso deliberatamente dallo scope
- **Strumenti e Ambiente:** Macchina virtuale isolata (VirtualBox, Kali Linux); Firefox con estensioni UA Switcher e uBlock Origin; hotspot cellulare (evita l'esposizione dell'IP domestico)
- **Politica di Interazione:** Nessun login, nessuna interazione con alcuna piattaforma target — solo OSINT passivo
- **Gestione dei Dati:** Screenshot e hash conservati in cartella dedicata; contenuti visivi di terze parti non pertinenti all'indagine oscurati prima della pubblicazione

---

## 🔍 Evidenze Iniziali e Dati di Partenza
- **Punto di Partenza:** Username "SakuraSnowAngelAiko"
- **Panoramica Account:** Vedi risultati per piattaforma più sotto (Fasi dell'Indagine)
- **Presenza Cross-platform:** Confermata su GitHub e X/Twitter; inconcludente/non verificabile su TikTok e Telegram; falso positivo su YouTube; rumore da omonimia su Instagram
- **Motori di Ricerca Utilizzati:** DuckDuckGo
- **Piattaforme Specializzate / Strumenti Utilizzati:** Sherlock, Maigret, GoFullPage, Wayback Machine

---

## 🧩 Fasi dell'Indagine

### A. Verifica Autenticità Profilo

**A.1 GitHub — Verdetto: Confermato (profilo per CTF TryHackMe)**
- Età account vs livello di attività: creato il 23/01/2021 (dato Maigret); nessun contributo attivo nell'ultimo anno
- Verifica foto profilo: non sottoposta a reverse image search (non necessario — corroborato da tre fonti indipendenti)
- Analisi bio e username: display name "Aiko", distinto dall'handle completo "SakuraSnowAngelAiko" — comportamento tipico di GitHub, nessuna anomalia; bio assente; 274 follower; 0 following; 9 repository pubblici (5 in evidenza), alcuni a tema criptovalute
- Pattern di pubblicazione: N/A (repository di codice, non un feed social)
- Scoperta aggiuntiva: un repository contiene una stringa di configurazione mining Stratum (`stratum://ethwallet.workerid:password@miningpool:port`) — sintassi da template standard, non una credenziale funzionante; un altro repository contiene una chiave pubblica (non decodificata, fuori scope)
- Validazione incrociata: hit Sherlock + verifica manuale + dati estesi Maigret (UID 77871458, data creazione, follower/following, fullname) — tutte e tre convergono

**A.2 YouTube — Verdetto: Falso positivo**
- La navigazione diretta restituisce 404 Not Found
- La ricerca dork ("SakuraSnowAngelAiko" Youtube) non ha restituito versioni cache/archiviate né menzioni esterne
- Valutato come probabile falso positivo di Sherlock (errata interpretazione di un codice di risposta HTTP), comportamento documentato per alcune piattaforme
- Ha condotto alla scoperta accidentale dell'account Instagram (A.6) tramite un errore di digitazione nella query di ricerca

**A.3 TikTok — Verdetto: Inconcludente**
- La navigazione diretta è bloccata da un muro di login
- Dork `site:tiktok.com SakuraSnowAngelAiko`: solo username simili ma non identici
- Dork più ampio `SakuraSnowAngelAiko "tiktok"`: nessun risultato rilevante
- Distinto da un falso positivo dello strumento: qui è la piattaforma stessa a negare l'accesso a utenti non autenticati indipendentemente dall'esistenza reale del profilo; ulteriormente limitato dalla scelta consapevole di non utilizzare sockpuppet

**A.4 Telegram — Verdetto: Non verificabile**
- Canale creato il 17 novembre 2025 (anni dopo l'account GitHub)
- Fullname: "?"; 15 iscritti; immagine profilo assente (Maigret conferma un SVG placeholder generato automaticamente)
- Tre messaggi, tutti dallo stesso mittente ("?"): un'immagine (screenshot di una conversazione con un interlocutore "Deleted Account") con didascalia in russo "скучаю" ("mi manca"/"sento la mancanza"), più altri due commenti in russo
- L'immagine mostra 396 visualizzazioni e 4 reazioni con emoji fragola, numero sproporzionato rispetto ai 15 iscritti del canale
- Nota: solo l'assenza di una foto profilo reale è un dato Maigret specifico su Telegram; il dato "country: ru" e il tag "porn" sono cifre aggregate sull'intera ricerca Maigret, non specifiche di Telegram — riportati come elementi di corroborazione, non come conferma
- Indicatori convergenti aggiuntivi: Teletype (piattaforma russa) tra gli hit di Maigret; altri due hit Maigret collegati al tag "porn" (ChaturBate, xHamster)
- Non si può affermare con certezza la natura del contenuto del canale

**A.5 X/Twitter — Verdetto: Confermato (profilo per CTF TryHackMe) — Scoperta accidentale**
- Trovato per caso: un errore nell'inserimento dell'URL (l'URL di GitHub incollato nel motore di ricerca invece che nella barra degli indirizzi) ha fatto emergere questo account tra i primi risultati DuckDuckGo
- Handle: @SakuraLovesAiko — diverso dallo username target; trovato per corrispondenza di contenuto sul nome "Aiko", non per hit esatto sullo username
- Confermato tramite dork `site:x.com SakuraSnowAngelAiko`, poiché il profilo GitHub non conteneva riferimenti diretti a X
- Il contenuto presenta indizi per il CTF TryHackMe, coerente con il ruolo del profilo GitHub
- Nessun link diretto verso GitHub trovato sul profilo
- Un link presente sul profilo rimanda a un account "cinese" con alta probabilità generato con IA — non approfondito, giudicato fuori scope
- Nota sugli strumenti: né Sherlock (~400 siti noti) né Maigret (oltre 3.000 siti) hanno rilevato questo account nonostante X sia una piattaforma di primo piano — spiegabile con un probabile blocco delle verifiche automatiche imposto da X stessa, limite superabile solo con ricerca manuale

**A.6 Instagram — Verdetto: Rumore da omonimia — Scoperta accidentale**
- Trovato tramite una ricerca dork relativa alla verifica YouTube (query su motore di ricerca, non intenzionale)
- Username identico al target; nessuna foto profilo visibile
- Contenuto della bio copiato integralmente dalla voce Wikipedia in inglese su **Sakura Miko**, VTuber giapponese reale affiliata a Hololive Production — persona pubblica non correlata al target didattico
- Fonte archiviata su Wayback Machine (29/08/2026) come riferimento bibliografico: https://web.archive.org/web/20260829085050/https://en.wikipedia.org/wiki/Sakura_Miko. 
- Valutato come coincidenza di username, non identità condivisa — pattern OSINT documentato (account fan/tributo, generazione di traffico sfruttando un nome noto)
- **Considerazione etica:** poiché l'account è verosimilmente riconducibile a una persona reale e privata (a differenza del personaggio pubblico Sakura Miko), i contenuti visivi potenzialmente identificativi (anteprime dei reel) sono stati oscurati prima della pubblicazione

---

## 🔒 Integrità delle Prove
- **Metodo di Acquisizione:** Screenshot a pagina intera tramite l'estensione browser GoFullPage (formato PNG)
- **Impronta Hash:** SHA-256, calcolato con `sha256sum`, registrato cumulativamente in `hash_log.txt`
- **Marcatura Temporale:** Non è stato impiegato un servizio di timestamping certificato; i riferimenti temporali si basano sui metadata di sistema dei file e sulle date riportate nei log
- **Archiviazione Ridondante:** Applicata solo alla fonte esterna citata (pagina Wikipedia, via Wayback Machine); le evidenze primarie non hanno backup ridondante oltre alla copia locale

---

## ✅ Validazione delle Evidenze
- **Integrità dei Dati:** Fonte diretta verificata per tutte le piattaforme navigate direttamente (barra indirizzi, non risultati di ricerca)
- **Stato della Verifica:** Confermato (GitHub, X/Twitter) / Falso Positivo (YouTube) / Inconcludente (TikTok) / Non verificabile (Telegram) / Rumore da omonimia (Instagram)
- **Metodo di Validazione Incrociata:** Confronto Sherlock + Maigret; tre fonti indipendenti convergono su GitHub (hit strumento, verifica manuale, dati estesi Maigret)

---

## ⚠️ Limitazioni
- Tasso di falsi positivi dello strumento primario: 1 hit su 4 di Sherlock (25%), coerente con il comportamento documentato di Sherlock su piattaforme come YouTube
- Limiti imposti dalle piattaforme: il muro di login di TikTok ha reso impossibile una verifica passiva completa, costo diretto della scelta deliberata di non impiegare sockpuppet
- Limiti tecnici dello strumento secondario: Maigret ha riportato un tasso di errore combinato del 9,82% ("bot protection" + "request failed"), a indicare che una quota di risultati automatici resta non verificabile anche con un secondo strumento
- Probabile blocco delle verifiche automatiche imposto da X, che ha impedito a entrambi gli strumenti di rilevare l'account X confermato
- Deliberatamente esclusi dallo scope: decodifica della chiave pubblica su GitHub; verifica approfondita dei 6 hit rilevati solo da Maigret oltre alla tipologia; l'account sospetto generato con IA collegato da X

---

## 🎯 Conclusione Finale e Sintesi
- **Punti Chiave:** Il profilo GitHub rappresenta l'evidenza più solida raccolta, beneficiando di triplice validazione indipendente e di un elemento comportamentale aggiuntivo (configurazione di mining crittovalutario). Il profilo Telegram, pur non pienamente confermabile, ha prodotto l'indicatore geografico/linguistico più significativo dell'indagine (lingua russa), corroborato indipendentemente dal dato aggregato di Maigret. L'indagine conferma un principio centrale del SOCMINT: la coincidenza di username tra piattaforme non costituisce prova di identità condivisa (caso Instagram). Emerge inoltre una distinzione metodologicamente rilevante tra falso positivo dello strumento (YouTube) ed esito inconcludente per limite esterno della piattaforma (TikTok).
- **Valutazione Rischio / Impatto:** Non applicabile — target didattico e fittizio; nessun rischio o impatto nel mondo reale.
- **Raccomandazioni:** Nessuna necessaria — scope dell'esercizio pienamente rispettato entro i confini definiti.

---

## 📎 Appendice
- **Tabelle Dati Grezzi:** Log hash completo (`hash_log.txt`), output grezzi degli strumenti (`risultati_grezzi.txt`, `maigret_risultati_grezzi.txt`) e screenshot delle evidenze disponibili in questo repository: [https://github.com/ErikaPellegrino/OSINT/tree/main/SOCMINT/SOCMINT-01_Results_EVIDENCE]
- **Versioni Strumenti:** Sherlock 0.16.0; Maigret 0.6.4;
