# Sakura Room

*My journey to complete the historic room created by OSINT Dojo on TryHackMe*

**Erika Pellegrino**
*Sep 08, 2026*

This is not meant to be yet another walkthrough of TryHackMe's Sakura Room, a room that is by now historic, solved and written about by countless people over the years. The goal of this article is different: to honestly recount the learning journey I went through with this room, task by task, including the difficulties and, above all, the concepts I learned thanks to this challenge.

> **Note:** many walkthroughs of this room can be found online. If you want to solve this room yourself without spoilers, you should stop reading here. If instead you are looking for another write-up to compare your own work with, you're in the right place.

## TASK 1 - INTRODUCTION

> **ID:** THM-01 SAKURA ROOM (CTF)
> **ANALYST:** ERIKA PELLEGRINO
> **DATE OF ANALYSIS:** 09/04/2026
> **TARGET:** SakuraSnowAngelAiko by OSINT Dojo
> **SCOPE OF ANALYSIS:** OSINT analysis of the digital identity and online traces left by a fictional attacker (SakuraSnowAngelAiko), starting from an image clue, with the goal of identifying their username, email, real name, crypto wallet, home Wi-Fi network, and probable city of residence.
> **METHODOLOGY:** SOCMINT, BLOCKINT, GEOINT — passive research, no direct interaction with the target
> **SUBSTACK:** https://substack.com/@erika124440

The first task is purely introductory: OSINT Dojo welcomes you to the Sakura Room on TryHackMe. The intro text explains that the room is designed to test a wide range of different OSINT techniques. Each section offers hints that help gather the clues needed to answer the tasks' questions. All answers must be obtained through passive research techniques.

## TASK 2 - TIP-OFF

With Task 2 the CTF truly begins.

**Scenario:** OSINT Dojo has been the victim of a cyberattack. During the forensic investigation, the team's administrators found a clue left behind by the cybercriminal: a downloadable image. The first question asks for the attacker's username.

**Procedure:**

With an image as a clue, the first thing to do to get information would be to analyze the metadata, for example with exifeditor.io. However, when saving the photo, I noticed the format wasn't a classic PNG or JPEG, but an SVG (Scalable Vector Graphics).

This image format is not based on a pixel grid but on vector graphics. Unlike traditional images, which contain a map of colored dots, an SVG file contains mathematical instructions and code in XML (eXtensible Markup Language) format. XML is a text format designed to store, organize, and transport data in a way that is understandable both by humans and by machines.

To get more information from an SVG image, it's enough to save it and open it with a text editor (Notepad, Visual Studio Code, etc.) instead of an image viewer. Doing so reveals the full source code.

![Image clue and source code](images/svg-source-code.png)
*Image clue and source code*

Reading the source code gave me the answer to the first question: the attacker's name is *SakuraSnowAngelAiko*, found in the personal directory where the picture had been saved. The format `/home/username/Desktop/…` is typical of Linux systems.

**What I learned:**
- What an SVG image is and how it differs from more traditional image formats; the analytical importance of source code in an investigation.

## TASK 3 - RECONNAISSANCE

Having a username is a good starting point for finding further information. Task 3 points out that people often reuse the same username across multiple platforms, so it's likely the same username was used to sign up for other web services, such as social networks. The room suggests searching for matching usernames on other platforms, while watching out for false positives.

There are two answers to find in this task: the attacker's email address and their full name.

**Procedure:**

There are several methods for finding social platforms linked to a username: Google Dorking, tools like Sherlock or Maigret, or web-based tools like WhatsMyName. For this exercise I chose the latter, considered one of the most reliable and actively maintained tools in the OSINT field.

Entering the username *SakuraSnowAngelAiko* into the tool's search bar, I got a series of results flagged with three colors — green, yellow, red — from most reliable to most likely false positive to not found. The only certain result turned out to be a GitHub profile.

![WhatsMyName results](images/whatsmyname-results.png)
*WhatsMyName results*

For thoroughness and learning purposes, I also quickly checked the results highlighted in yellow, i.e. the "potential" false positives. All of these pages turned out to be either nonexistent (404 error) or unrelated to the purpose of the search. Regarding false positives, it's worth knowing that when searching for a username, many sites where that username doesn't actually exist won't return a clear "404 - not found" error, but will instead show a generic page with a "200 OK" response code, which normally indicates "page found successfully." An automated tool like WhatsMyName, which relies solely on the HTTP response code, can't fully trust these specific sites, and therefore flags them as a "potential false positive" rather than "found." As I'm learning, it's good practice to leave nothing to chance, but it's equally important not to get too absorbed in every tiny detail when the evidence (in this case, empty or irrelevant pages) is already clear enough.

At this point I opened the GitHub profile. The handle on the main page matches; the displayed name is *Aiko*. There are 5 pinned repositories, 2 of which belong to the user and 3 are forks. In total there are 9 repos.

![GitHub profile overview](images/github-profile-overview.png)
*GitHub profile overview*

![Aiko's public repositories](images/github-repos.png)
*Aiko's public repositories*

I then looked for clues among the various repositories. The "IO" repo doesn't seem to contain any useful clues. I then opened the "ETH" repo, which contains the file "miningscript," inside which is the first clue: a connection URL (stratum) to a mining pool that includes, among other things, an ETH wallet address.

Once I saved this clue, I kept going through the repos. The third one is the "PGP" repository, which contains another clue: a public key encoded in Base64, a format used to represent binary data as text.

![Base64 public key in the PGP repo](images/pgp-repo-publickey.png)
*Base64 public key in the PGP repo*

Given the priority and objective of Task 3, the first step was to decode the public key. To do this I used GPG Decoder, a free web tool designed specifically to "open" a PGP (Pretty Good Privacy) key, extract its content, and display it in human-readable form. A PGP key is actually made up of a public key and a private key. The public key is a numeric value that can be shared with anyone so they can send encrypted messages or verify digital signatures. Anyone who wants to know the content must use this key to decrypt the data. The private key, on the other hand, is kept by the owner and must never be disclosed. It's used exclusively to decrypt received messages or generate digital signatures. This is asymmetric cryptography: a message sent using the recipient's public key can only be read by whoever holds the corresponding private key.

![Public key decoding](images/pgp-decode.png)
*Public key decoding*

The decoding revealed the answer to the first question of Task 3, i.e. the attacker's email address: **SakuraSnowAngel83@protonmail.com**.

Once I had this email, I tried several approaches to leverage it and find the answer to the second question of Task 3, i.e. the attacker's full name. I used various Google dorks, more or less strict, without getting useful results. Almost by chance, I tried searching Google for the full name *SakuraSnowAngelAiko* but written out in natural language: *Sakura Snow Angel Aiko*. Only this way was I able to find an X (Twitter) page belonging to Aiko.

> **NOTE:** having already carried out the self-made exercise SOCMINT-01 with this same account as the target ("Username Enumeration, Cross-Platform Correlation and Manual Verification: a SOCMINT case study," available on this profile), I already knew that page existed, yet I couldn't find it with strict, specific dorks (quotation marks, `site:` operators); it was a less constrained text search that surfaced it.

![Aiko's X profile](images/x-profile-aiko.png)
*Aiko's X profile*

The very first tweet gave the answer to the second question of Task 3: **Aiko Abe**.

![Tweet "I'm AikoAbe3"](images/tweet-aikoabe3.png)
*Tweet "I'm AikoAbe3"*

Once Task 3 was done, I paused to carefully look over Aiko's X profile, noting down in Obsidian what I saw:
- a tweet in which she introduces herself as "@AikoAbe3"
- a post that appears suspended/removed
- a satellite image of a region
- an image in which she says she's on her last layover before heading home
- an image with a cherry blossom tree along a long avenue, in which she says she stopped to admire it before checking out and heading home

**What I learned:**

To watch out for false positives and know what's worth pursuing further and what isn't; how a public key can be decoded and how information-rich it can be; how an overly rigid dork can fail where a more natural text search succeeds, so it's always worth trying both approaches before considering a lead exhausted.

## TASK 4 - UNVEIL

In Task 4, the hints refer to the commit history of the GitHub repositories, while the questions are about the world of cryptocurrencies. It was clear the answers were connected to the "stratum" clue found earlier in the ETH repo.

**Procedure:**

I went back to the ETH repo and looked more closely at the commit history where I had already spotted the wallet address. In the history there was an earlier commit that openly showed the wallet address. Even though the file had later been edited to clean up the exposed sensitive data, GitHub's immutable commit history still made it possible to recover the original version.

![miningscript history and ETH wallet address](images/github-commit-history.png)
*miningscript history and ETH wallet address*

As shown, the original commit reveals the wallet address: `0xa102397dbeeBeFD8cD2F73A89122fCdB53abB6ef`.

A Stratum-format URL is the standard a miner (i.e. an individual or entity that dedicates their computer to mining — the process by which new crypto is created and transactions are verified and added to the blockchain) uses to connect, or "introduce" themselves, to a mining pool in order to receive cryptocurrency rewards. It's like a home delivery: before receiving anything, you need to state precisely where to deliver it, who's ordering, and from where. The general structure `stratum://[wallet_address].[worker_id]:[password]@[pool_server]:[port]` shows each component that identifies a piece of the configuration:

- the **wallet address** is the delivery address — this is where the rewards arrive; a mistake here means someone else will receive the reward;
- the **worker ID** is like the name written on the buzzer — useful if multiple devices are working on the same wallet at the same time, since it allows you to tell which one is actually producing what;
- the **password** is only there to confirm the order;
- **server and port** are the address of the shop you connect to in order to place the order — i.e. the mining pool itself.

With this clue it was possible to answer the task's first question: the cryptocurrency of the attacker's wallet is **Ethereum (ETH)**. The second question asked for the wallet address, i.e. the same address recovered from the deleted commit shown above.

The third question is more specific: it asks which mining pool the attacker received payments from on **January 23, 2021**. The date of the GitHub commit matches. To dig deeper and find the answer to this question, I used **Etherscan**.

Etherscan is a block explorer, i.e. a search engine that lets you browse the Ethereum blockchain in real time. Its interface makes readable data that would otherwise exist only as a raw stream distributed across thousands of nodes worldwide. This tool is used to look up addresses, transactions, smart contracts, and much more. Entering the wallet address on Etherscan, the overview page shows some key information about the address: the current ETH balance and its value in dollars, tags associated with the address, the date of the first and last transaction made, and the address that funded it for the first time ("funded by"); further down, a table lists the address's transactions in chronological order with hash, sender, recipient, amount, and gas fee for each.

![ETH address overview](images/etherscan-overview.png)
*ETH address overview*

In this case, the address had a total of 42 transactions. I needed to find the one from January 23, 2021. Doing a rough calculation, that was about 2050 days before the current date. Scrolling through the transaction list, I reached that range of days and, by hovering the cursor over the "Age" field of each transaction close to that number, I could read the exact date/time and identify the one from January 23, 2021.

![Transaction from January 23, 2021](images/etherscan-transaction-jan23.png)
*Transaction from January 23, 2021*

This let me answer the third question. The mining pool the attacker received payments from on that date is **Ethermine** (the "From" column).

The last question of Task 4 asks which other cryptocurrency the attacker exchanged using their own wallet. On Etherscan, an address page has several tabs besides the default "Transactions" one; among these is also "Token Transfers (ERC-20)," which shows only the token movements — other than native ETH — made by that address.

![Token Transfers (ERC-20) tab](images/etherscan-erc20-transfers.png)
*Token Transfers (ERC-20) tab*

The image shows that the other currency used by the attacker is **Tether**.

**What I learned:**

This task let me learn the basics of the blockchain and cryptocurrency world: how to read an Etherscan page; how a transaction takes place and the various elements needed to carry it out.

## TASK 5 - TAUNT

In Task 5, the focus returns to the X account, whose full page and details I had already saved earlier. This task's hints refer to a screenshot of a message the attacker sent to OSINT Dojo on Twitter, and also suggest following the leads from the account toward the Dark Web.

**Procedure:**

Answering the first question of Task 5 was easy. It simply asked for the profile's handle, i.e.: **SakuraLoverAiko**.

The task's second question asked instead for the **BSSID** of the attacker's home Wi-Fi. The BSSID (Basic Service Set Identifier) is the unique physical address of an access point — the device (router or repeater) that broadcasts the Wi-Fi signal.

Here it's important to understand a fundamental distinction between the BSSID and the SSID. The SSID is the Wi-Fi network's name: freely chosen when configuring the router (e.g. "home1234") and changeable at will. The BSSID, on the other hand, is the physical address of the device broadcasting that network. It's like the device's own unique street address, tied to the specific hardware rather than to the user's choice.

This distinction matters for an investigation because two people could name their own Wi-Fi network the same way (same SSID), but they will always have a different BSSID, since they're different physical routers. The BSSID can be geolocated through databases like WiGLE, built by communities of people who physically map Wi-Fi networks while driving around (a practice called *wardriving*). If someone's router has ever been spotted by a wardriver, its BSSID will be associated with precise GPS coordinates, making it possible to trace where that network is physically located and therefore, most likely, where that person lives or works.

Back to Task 5: I realized that the post that appeared suspended on X, which I had noted earlier, probably contained the clue needed to answer this question. The only way to see its content was to check an archived version of the profile from before the tweet's suspension. I therefore used the Wayback Machine and was fortunate enough to find an archived copy from 2025.

![Aiko's X account archived on web.archive.org](images/wayback-x-profile.png)
*Aiko's X account archived on web.archive.org*

The recovered post contained the missing information: a list of Wi-Fi networks and their passwords, in which the visible alphanumeric string was a hash — i.e. the result of a mathematical function that takes a piece of content (text, file, image) and turns it into a fixed-length, unique, identifying string, like a fingerprint: even a tiny change to the original content completely changes the resulting hash. This same functionality — publicly accessible text via a link, with no need for registration or identification — also comes in handy for anyone who wants to share something without leaving direct traces tied to their real identity, and therefore for potentially illegitimate uses.

On Aiko's X profile there's also a comment from the attacker: *"Not too concerned about someone else finding them in the Dark web. Anyone who wants them will have to do a real DEEP search to find where I PASTEd them."* The wordplay is deliberate and is another clue for solving this task's final question, i.e. the BSSID.

The words DEEP and PASTE(d), written in capital letters, emphasize the wordplay that, combined with the hint to search the dark web, suggests there might be a service like Pastebin on the dark web too, perhaps called DEEP PASTE. DeepPaste works on the same principle as Pastebin — a unique link to retrieve content without registration — with the difference that the identifier used here is a hash, rather than a random ID as with Pastebin. At this point in the exercise I ran into my biggest difficulties, and I also learned a huge number of things about these text-hosting applications and about the dark web. I downloaded and, for the first time, used Tor Browser on my virtual machine, along with search engines like Ahmia and Torch. I discovered that searching for something on the dark web is very different from searching the clear web, and that sites disappear from one day to the next, but replacements pop up even faster. The goal of going onto the dark web for this task was to find Deep Paste in order to retrieve the information needed from the hash exposed by Aiko, and thus get the answer, or other clues that could help me finish Task 5; however, after quite a bit (a lot) of studying and after many attempts and searches, I stopped. Maybe it's just that I'm not skilled enough yet, but from what I understand, it's very likely that the Deep Paste site is no longer reachable. Even finding a paste service that's working and active today wouldn't help retrieve the specific content the attacker saved back in 2021 on Deep Paste, because the hash exposed in the tweet is tied EXCLUSIVELY to the Deep Paste database: a different service has a completely different database.

Not having been able to personally verify the original content on Deep Paste, I obtained the SSID value I needed, along with other clues, from a walkthrough published online — secondhand information which I nonetheless independently confirmed myself with a search on WiGLE. The network's name, i.e. the SSID, is: **DK1F-G**. Among the results were other Wi-Fi networks with their passwords saved in the list so as not to forget them; among these was also the public Wi-Fi of the city of Hirosaki, Japan.

![DeepPaste results](images/deeppaste-results.png)
*DeepPaste results*

With these clues, I was able to move forward.

On WiGLE, the advanced research page lets you enter various data to trace even more. WiGLE doesn't search for an exact geographic point (that would be too restrictive), but searches within a geographic rectangle, i.e. a range of latitude and longitude. Once I learned this, I did a test. I looked up the city of Hirosaki on Google Maps to get its coordinates and narrow down the search on the database.

![Coordinates of the city of Hirosaki, Japan](images/hirosaki-coordinates.png)
*Coordinates of the city of Hirosaki, Japan*

Entering the SSID (DK1F-G) together with a range of coordinates covering the Hirosaki area on WiGLE, the search returned the result I was looking for: the BSSID → **84:af:ec:34:fc:f8**.

Out of curiosity, I checked whether the geographic filter was really necessary to find the BSSID, or whether the SSID alone was enough to isolate a unique result. I repeated the same search leaving the longitude and latitude fields empty, and got the same result. This can happen when the SSID — the name given to one's own Wi-Fi — is genuinely original and unique. Still, the BSSID is the data point that's actually useful for physical geolocation.

**What I learned:**

With this task I did my first search on the dark web and learned a lot about it, especially how to search on this network; the various types of hashes and their uses (I had already used SHA-256 to validate evidence in other exercises), and what paste services are used for; I learned the difference between SSID and BSSID and how a router can be geolocated.

## TASK 6 - HOMEBOUND

In the room's final task, number 6, the initial hint holds a great lesson: in OSINT, there often isn't a "smoking gun" that points to one clear, definitive answer. An OSINT analyst instead has to learn to synthesize multiple pieces of information in order to draw a conclusion about what is probable, improbable, or possible.

**Procedure:**

To wrap up the room, it was necessary to use all the data available and the information gathered previously to trace the attacker and, specifically, where they live. Task 6's questions refer specifically to the tweets the attacker had posted — already noted earlier — in order to find out the name of the departure airport, the name of the airport for the last layover before reaching the destination, the name of the lake at the center of the aerial photo posted on the account, and finally the attacker's probable hometown.

The first question asks for the airport closest to the place where the attacker shared a photo before leaving.

Before leaving, Aiko had posted a tweet with the following photo.

![Tweet with cherry blossoms before departure](images/tweet-cherry-blossoms.png)
*Tweet with cherry blossoms before departure*

In the photo you can see some cherry trees along the avenue on the right; a walkway (possibly pedestrian) with safety barriers along the edge; some buildings on the left; a large green space, perhaps a playing field, further along on the left; and, in the background, a very tall white structure shaped like a tower. It was immediately clear that this structure was the main clue. First, though, I tried searching for the whole image, without cropping the tower, via Google Image Search, but the only matches found were Aiko's own posts and the room's solutions published over the years. I also tried with Yandex, but got the same result.

This initial attempt made me realize how important it is to analyze every detail of an image thoroughly, in order to run a search that is not only effective but also more targeted and reliable.

I therefore zoomed into the image and cropped the tower detail (despite the poor resolution), to run a test using the Search by Image extension on Brave, which lets you search an image across multiple search engines at once.

![Tower detail at very low resolution](images/tower-detail-lowres.png)
*Tower detail at very low resolution*

I ran the search across numerous engines — Google, Yandex, TinEye, Baidu, and others — but the only one to find an exact match in this case was Google. The tower in question is the **Washington Monument** (Washington, D.C., USA). Then, with a simple Google search, I found out that the airport closest to the obelisk is **Ronald Reagan Washington National Airport (DCA)**, located in Arlington (Virginia), about 6 km from the monument, confirmed via Google Maps. This airport's code (**DCA**) is the answer to the first question.

To find out at which airport the attacker had their last layover, another one of Aiko's posts came in handy, in which she explicitly states it's her last layover.

![Tweet "My final layover, time to relax!"](images/tweet-final-layover.png)
*Tweet "My final layover, time to relax!"*

The photo shows several details: in the foreground, the text "5 Star Airline Skytrax." A quick search revealed this is a prestigious award granted by the British rating agency Skytrax, given to those who achieve high quality in airport and onboard services and products. The elegant sign on the wall also indicates that this is a lounge at an airport.

Here too I used Google's Reverse Image Search. This time the search returned relevant results, aside from the ones related to the challenge itself, of course. The AI had already given me the answer right away, but in a real investigation it's important to verify the source. From these images I found out the lounge belongs to Japan Airlines First Class, and checking the relevant results shows it is specifically the lounge at **Tokyo Haneda Airport**, whose code is the answer to the second question: **HND**.

![Airport lounge search results](images/lounge-search-results.png)
*Airport lounge search results*

Task 6's third question asks for the name of the lake that appears in the aerial photo Aiko posted.

![Satellite photo posted by Aiko](images/tweet-satellite-photo.png)
*Satellite photo posted by Aiko*

The lake is clearly visible in the photo, centered slightly to the right; on the left there's an island with a very distinctive shape. Considering the other clues gathered so far — the layover in Tokyo and the reference to Hirosaki that came up from the Wi-Fi network name in the previous task — there is by now reasonable certainty that the image shows a portion of Japan.

I then used Google Earth, which offers very detailed imagery, searching for "Hirosaki, Japan." The image indeed showed a lake with a shape similar to the one in the tweet: **Lake Towada**. However, the oddly-shaped island on the left didn't appear in that area.

![Lake Towada](images/lake-towada.png)
*Lake Towada*

I therefore zoomed out to find that island. The island with the unmistakable shape is **Sado**. In that same area, further to the right, just like in the photo, there's another lake: **Inawashiro**. The shape of the landmass also matches the one in the tweet. This is the correct answer to the fourth question.

![Lake Inawashiro and Sado Island](images/lake-inawashiro-sado.png)
*Lake Inawashiro and Sado Island*

This step was a concrete example of how a plausible initial hypothesis can be corrected by evaluating important details, rather than stopping at a superficial observation.

The last question of Task 6, and of the whole room, asks for the city the attacker most likely considers home. With all the clues gathered, particularly the reference to Hirosaki, the answer is exactly that: **Hirosaki**.

**What I learned:**

This task made me realize that in OSINT, there is rarely a single, definitive piece of proof, and so an analyst has to be able to piece together multiple independent clues in order to formulate the most reasonable hypothesis.

## CONCLUSION

Going through the Sakura Room task by task, stopping to fully understand every technical concept encountered along the way — from SVG metadata, to GitHub's immutable commit history, to the structure of Ethereum transactions, to how WiGLE works, all the way to the reasoning needed to navigate the Dark Web — allowed me to connect SOCMINT skills, Blockchain Intelligence techniques, and GEOINT, much like what would happen in a real case. But above all, it gave me a much deeper understanding of investigative methodology and the intelligence cycle, which I will certainly apply in my future studies and future work.
