---
outline: deep
---

# Kennistoets: Filters

Klik een antwoordoptie aan of denk er eerst zelf over na voor je de oplossing bekijkt.

<FillIn
  vraag="Het commando dat het aantal regels in een bestand telt is ___. (enkel commando met optie)"
  antwoord="wc -l"
/>

<Quiz vraag="Welk teken gebruik je om de standaarduitvoer van een commando naar een bestand te schrijven?" opties="pipe-teken ( | )|ampersand-teken ( &amp; )|kleiner-dan-teken ( &lt; )|groter-dan-teken ( &gt; )" :correct="3">

**Groter-dan-teken (`>`)**

Met `>` schrijf je de standaarduitvoer (stdout) van een commando naar een bestand. Het bestand wordt aangemaakt als het nog niet bestaat en anders overschreven. Voorbeeld: `ls > output.txt`.

</Quiz>

<Quiz vraag="Wat doet het commando: cut -d ',' -f1 ?" opties="Het sorteert het bestand.|Het verwijdert een kolom.|Het voegt een kolom toe.|Het toont de eerste kolom van een CSV-bestand (comma-separated values)." :correct="3">

**Het toont de eerste kolom van een CSV-bestand.**

`-d ','` stelt de komma in als scheidingsteken, `-f1` selecteert het eerste veld. Het commando `cut` knipt kolommen uit regels op basis van een scheidingsteken of tekenpositie.

</Quiz>

<FillIn
  vraag="Als je op een Linux server een bestand wilt downloaden van een website kan je gebruik maken van ___. (enkel commando)"
  antwoord="wget of curl"
  patroon="^(wget|curl)$"
/>

<Quiz vraag="Welke optie gebruik je in grep om hoofdletterongevoelig te zoeken?" opties="-i|-c|-v|-n" :correct="0">

**`-i`**

De optie `-i` (ignore case) maakt de zoekactie hoofdletterongevoelig. Zo matcht `grep -i "linux" bestand.txt` zowel `Linux`, `LINUX` als `linux`.

</Quiz>

<Quiz vraag="Wat is de uitvoer van 'wc -w bestand.txt' als het bestand leeg is?" opties="Geen uitvoer|0|1|Error" :correct="1">

**`0`**

`wc -w` telt het aantal woorden. Een leeg bestand heeft geen woorden, dus de uitvoer is `0 bestand.txt`. Er is geen fout omdat het bestand wél bestaat, het is gewoon leeg.

</Quiz>

<Quiz vraag="Het commando cut kan geen kolommen scheiden aan de hand van een spatie." opties="Waar|Niet waar" :correct="1">

**Niet waar.**

`cut` kan wel degelijk een spatie gebruiken als scheidingsteken via de optie `-d ' '`. Voorbeeld: `echo "hello world" | cut -d ' ' -f2` geeft `world` als uitvoer.

</Quiz>

<Quiz vraag="Reguliere expressies kunnen enkel worden gebruikt met grep." opties="Waar|Niet waar" :correct="1">

**Niet waar.**

Reguliere expressies worden breed ondersteund in Linux. Naast `grep` kun je ze ook gebruiken met `sed`, `awk`, `find`, en in programmeertalen zoals Python, JavaScript en Perl.

</Quiz>

<Quiz vraag="Wat is de functie van het 'tee'-commando?" opties="Het filtert de uitvoer op basis van een reguliere expressie.|Het telt de woorden in de uitvoer.|Het stuurt de uitvoer naar zowel de standaarduitvoer als naar een bestand.|Het voert een sortering van de invoer uit." :correct="2">

**Het stuurt de uitvoer naar zowel de standaarduitvoer als naar een bestand.**

`tee` leest van stdin en schrijft tegelijk naar stdout én naar een bestand. Zo kan je een pipeline-resultaat bewaren zonder de uitvoer op het scherm te verliezen. Voorbeeld: `ls | tee lijst.txt`.

</Quiz>

<Quiz vraag="Wat doet de optie -v in het grep-commando?" opties="Het retourneert alle regels die NIET overeenkomen met het opgegeven patroon.|Het maakt de zoekopdracht hoofdletterongevoelig.|Het toont het aantal overeenkomsten.|Het schrijft de uitvoer naar een bestand." :correct="0">

**Het retourneert alle regels die NIET overeenkomen met het opgegeven patroon.**

`grep -v` staat voor "invert match". Het is handig om rijen weg te filteren die je niet wilt zien. Voorbeeld: `grep -v "^#" bestand.txt` toont alle regels behalve de commentaarregels.

</Quiz>
