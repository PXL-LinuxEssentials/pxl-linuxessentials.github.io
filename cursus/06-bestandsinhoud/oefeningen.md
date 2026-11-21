# Oefeningen op bestandsinhoud

::: info Hoe werk je met deze oefeningen?
Probeer elke oefening **eerst zelf** op je Ubuntu-VM. Kijk pas daarna naar de oplossing. Loopt het mis? Gebruik `man <commando>` (afsluiten met `q`). Controleer je resultaat telkens met `cat`.
:::

## Oefening 1
Ontdek waarom je `less` zou moeten gebruiken in plaats van `more`.

::: details Oplossing tonen
`less` laat je vooruit **en** achteruit scrollen, zoeken (`/`, `?`), naar begin/einde springen (`g`/`G`) en kan groeiende logs volgen (`F`). `more` is beperkter: vooral vooruit en per pagina, en het sluit zichzelf af aan het einde van het bestand. Zie:

```
man less
```
```
man more
```
Afsluiten doe je met `q`.
:::

## Oefening 2
Toon de eerste regel van het bestand `/proc/meminfo` om erachter te komen hoeveel geheugen je aan je Ubuntu Virtual-machine hebt gegeven.

::: details Oplossing tonen
```
head -n 1 /proc/meminfo
```
*De regel `MemTotal` toont het totale geheugen in **kB** (kilobytes). Deel door 1024 voor MB, nog eens door 1024 voor GB.*
:::

## Oefening 3
Toon de laatste 3 regels van het bestand `passwd` in de map `etc` van de hoofdmap.

::: details Oplossing tonen
```
tail -n 3 /etc/passwd
```
:::

## Oefening 4
Toon de eerste 4 tekens (=bytes) van het bestand `/etc/passwd`. Doorzoek de manpage van `head` om erachter te komen hoe dit moet. Je zou de naam van een bepaalde gebruiker moeten zien. Let wel op! De output staat hier **voor** de prompt. Wie is deze gebruiker?

::: details Oplossing tonen
```
head -c 4 /etc/passwd
```
*Antwoord: `root`, de administrator van Linux.*
:::

## Oefening 5
Gebruik `cat` om de volgende tekst in een nieuw bestand `mytextfile` in je homefolder te plaatsen:

```
Dit is mijn tekst
verdeeld over meerdere lijnen
ingevoegd door cat.
```

::: details Oplossing tonen
```
cat > ~/mytextfile << EOF
Dit is mijn tekst
verdeeld over meerdere lijnen
ingevoegd door cat.
EOF
```
*Alternatief zonder eindmarkering: `cat > ~/mytextfile`, typ de drie regels en sluit af met `Ctrl+D`.*
:::

## Oefening 6
Gebruik het commando `echo` drie keer met output redirection om de volgende tekst in een nieuw bestand `myechotextfile` in je homefolder te plaatsen:

```
Dit is mijn tekst
verdeeld over meerdere lijnen
ingevoegd door echo.
```

**Moeilijker:** het is ook mogelijk om dit te doen met slechts **één** `echo`-commando. Maar je zal in de manpage moeten zoeken naar de juiste optie om telkens een *nieuwe lijn*-code te kunnen meegeven. Ook deze code vind je terug in de manpage.

::: details Oplossing tonen
Met **drie** keer `echo` (let op: de eerste keer `>`, daarna `>>`):

```
echo "Dit is mijn tekst" > ~/myechotextfile
```
```
echo "verdeeld over meerdere lijnen" >> ~/myechotextfile
```
```
echo "ingevoegd door echo." >> ~/myechotextfile
```

*Één commando (moeilijker):*

```
echo -e "Dit is mijn tekst\nverdeeld over meerdere lijnen\ningevoegd door echo." > ~/myechotextfile
```
*De optie `-e` zorgt ervoor dat `echo` de code `\n` (nieuwe lijn) interpreteert.*
:::

## Oefening 7
Gebruik `cat` om het bestand `.bashrc` in je homefolder te kopiëren naar een nieuw bestand met de naam `.bashrc.backup`.

::: details Oplossing tonen
```
cat ~/.bashrc > ~/.bashrc.backup
```
*Ter info: in de praktijk gebruik je hiervoor `cp ~/.bashrc ~/.bashrc.backup`. Dat leren we in een volgend hoofdstuk.*
:::

## Oefening 8
Wanneer je een nieuwe gebruiker toevoegt, wordt een nieuwe regel **onderaan** het bestand `/etc/passwd` toegevoegd. Toon de inhoud van dit bestand, maar in de volgorde van nieuwste gebruiker naar oudste gebruiker (andersom dan normaal).

::: details Oplossing tonen
```
tac /etc/passwd
```
:::

## Oefening 9
Gebruik het commando `tail` om het bestand `/var/log/auth.log` open te houden, zodat je alle nieuwe logboekvermeldingen ziet verschijnen wanneer ze zich voordoen. (Je kan een paar keer op `Enter` drukken om de nieuwe regels te scheiden.) Start in een nieuw PowerShell-venster een nieuwe ssh-sessie en meld je aan. Log vervolgens opnieuw uit. Wat zag je in de logboeken? Stop het commando met `Ctrl+C`.

::: details Oplossing tonen
```
sudo tail -f /var/log/auth.log
```
*Je ziet o.a.:*
- *`Accepted password/publickey for <user> from <IP>`*
- *`session opened/closed for user <user>`*

*Krijg je "Permission denied"? Vergeet dan `sudo` niet.*
:::

## Oefening 10
Open het configuratiebestand van ssh, `/etc/ssh/sshd_config`, met het `less`-commando en zoek met de zoekfunctie naar `PasswordAuth`. Met `PasswordAuthentication` kan je bijvoorbeeld instellen dat er enkel nog met SSH-keys kan ingelogd worden op de server en niet meer met wachtwoord.

1. Ga terug naar de eerste regel.
2. Zoek nu naar `passwordauth` met kleine letters. Wat gebeurt er?
3. Typ `-i` om hoofdletterongevoelig te zoeken en probeer opnieuw.

::: details Oplossing tonen
```
less /etc/ssh/sshd_config
```
1. Zoeken: `/PasswordAuth` + `Enter`. Gebruik `n` voor de volgende treffer en `N` voor de vorige.
2. Terug naar de eerste regel: `g`.
3. Zoeken naar `/passwordauth` + `Enter`. Je vindt niets, want zoeken is hoofdlettergevoelig.
4. Typ `-i` + `Enter` om over te schakelen naar hoofdletterongevoelig zoeken.
5. Zoek opnieuw `/passwordauth` + `Enter`. Nu vind je de regels wel.

*Afsluiten met `q`.*
:::

## Oefening 11
Gebruik `nano` om de tekst te bewerken in het bestand `myechotextfile` dat je eerder in je homefolder hebt gemaakt, zodat het er zo uitziet:

```
Dit is mijn tekst, bewerkt,
nog steeds verdeeld over meerdere lijnen
Ingevoegd door Echo en bewerkt door Nano.
```

::: details Oplossing tonen
```
nano ~/myechotextfile
```
*Bewerk de tekst. Opslaan & sluiten: `Ctrl+S`, daarna `Ctrl+X`.*
:::

## Oefening 12
Gebruik `cat` met de eindmarkering `LinuxIsFun` om de tekst te **overschrijven** in het bestand `myechotextfile` dat je eerder in je homefolder hebt gemaakt:

```
Deze tekst is veel interessanter.
Ik gebruik nog steeds meerdere lijnen d'oh,
gewoon omdat het kan.
```

::: details Oplossing tonen
```
cat > ~/myechotextfile <<LinuxIsFun
Deze tekst is veel interessanter.
Ik gebruik nog steeds meerdere lijnen d'oh,
gewoon omdat het kan.
LinuxIsFun
```
*Vergeet de eindmarkering niet op een eigen regel te typen, anders blijft de shell wachten op meer invoer.*
:::

## Oefening 13
Druk de volledige inhoud van de eerder gemaakte bestanden `mytextfile` en `myechotextfile` samen af met slechts één commando.

::: details Oplossing tonen
```
cat ~/mytextfile ~/myechotextfile
```
:::

## Oefening 14
Haal de laatste 10 aangemaakte gebruikers op en zet ze in het bestand `nieuwsteUsers` met slechts één commando.

::: details Oplossing tonen
```
tail -n 10 /etc/passwd > ~/nieuwsteUsers
```
:::

## Oefening 15
Dit is een grote oefening op `nano`. Doorloop de stappen **a t.e.m. m** na elkaar.

**a.** Open een nieuw bestand, genaamd `Linus Torvalds`, met nano. Kopieer de volgende tekst naar de nano-editor (plakken doe je met je terminal, zie hoofdstuk-theorie).

```
linus Benedict torvalds, * , is a Finnish-American software engineer who is the creator and, historically, the main developer of the Linux kernel, used by Linux distributions and other operating systems such as Android. 
He also created the distributed version control system Git.
 
linus torvalds was born in Helsinki, Finland. His parents were campus radicals at the University of Helsinki in the 1960s. 
linus torvalds was born in Helsinki, Finland. His parents were campus radicals at the University of Helsinki in the 1960s. 
  
Torvalds attended the University of Helsinki from 1988 to 1996, graduating with a master's degree in computer science.
His academic career was interrupted after his first year of study when he joined the Finnish Navy Nyland Brigade in the summer of 1989, selecting the 11-month officer training program to fulfill the mandatory military service of Finland. 
  
He gained the rank of second lieutenant, with the role of an artillery observer. 
  
He bought computer science professor Andrew Tanenbaum's book Operating Systems: Design and Implementation, in which Tanenbaum describes MINIX, an educational stripped-down version of Unix. In 1990, Torvalds resumed his university studies, and was exposed to Unix for the first time.His MSc thesis was titled Linux: A Portable Operating System.
  
His interest in computers began with a Commodore VIC-20 at the age of 11 in 1981. He started programming for it in BASIC, then later by directly accessing the 6502 CPU in machine code (he did not utilize assembly language).
He wrote a Pac-Man clone, Cool Man. 
  
On 5 January 1991 he purchased an Intel 80386-based clone of IBM PC before receiving his MINIX copy, which in turn enabled him to begin work on Linux.
  
The first Linux prototypes were publicly released in late 1991. Version 1.0 was released on 14 March 1994.
  
Torvalds first encountered the GNU Project in 1991 when another Swedish-speaking computer science student, Lars Wirzenius, took him to the University of Technology to listen to free software guru Richard Stallman's speech. Torvalds used _____ GNU General Public License version 2 (GPLv2) for his Linux kernel.
  
The history of Linux 
Linus was born 28 December 1969 in Finland
```

**b.** Sla de wijzigingen op en sluit nano af.

**c.** Open het bestand opnieuw met nano.

**d.** Zoek naar de tekst `1981` om te weten wat er dat jaar is gebeurd.

**e.** De tweede alinea bevat twee keer dezelfde regel. Gebruik een sneltoets om één van de twee regels te verwijderen.

**f.** Zoek naar `linus` en vervang dit door `Linus`.

**g.** Selecteer alleen de tekst `born 28 December 1969` van de laatste regel. Knip het en plak het op de eerste regel waar het sterretje staat (`*`).

**h.** Zoek naar `torvalds` en vervang dit door `Torvalds`.

**i.** Ga naar **regel 9, kolom 80** (let op: je hebt in stap e een regel verwijderd, waardoor alle regels met één opgeschoven zijn). Vervang de punt (`.`) door een uitroepteken (`!`).

**j.** Ga naar de laatste regel tekst. Knip de hele lijn weg. Maak de knip ongedaan. Voer de knip opnieuw uit.

**k.** Gebruik knippen en plakken om de laatste regel tekst naar de bovenkant van het document te verplaatsen.

**l.** Zoek in de help binnen nano om erachter te komen hoe je het 'totale aantal regels, woorden en tekens' kunt weergeven.

**m.** Gebruik twee keer een sneltoets (`Ctrl+...`) om nano op te slaan en af te sluiten.

::: details Oplossing tonen
```
nano ~/Linus\ Torvalds
```

*a) Typ het commando hierboven. De backslash `\` zorgt ervoor dat de shell de spatie als deel van de bestandsnaam ziet. Alternatief: `nano "Linus Torvalds"`.*

*b & c) Opslaan & heropenen: `Ctrl+S`, `Ctrl+X`, daarna opnieuw `nano ~/Linus\ Torvalds`.*

*d) Zoeken: `Ctrl+W` → typ `1981` → `Enter`.*

*e) Dubbele regel verwijderen: ga op de overbodige regel staan → `Ctrl+K`.*

*f) Vervangen: `Ctrl+\` → zoek: `linus` → vervang: `Linus` → `A` (alle).*

*g) Selecteer `born 28 December 1969`: ga naar het begin van die tekst → `Ctrl+6` (Mark) → pijltjes tot het einde van de selectie → `Ctrl+K` (knip) → ga naar het sterretje `*` op de eerste regel → `Ctrl+U` (plak).*

*h) Vervangen: `Ctrl+\` → zoek: `torvalds` → vervang: `Torvalds` → `A` (alle).*

*i) Ga naar regel 9, kolom 80: `Ctrl+/` → typ `9,80` → `Enter` → vervang `.` door `!`.*

*j) Ga naar de laatste regel → `Ctrl+K` → ongedaan maken: `Alt+U` → opnieuw uitvoeren: `Alt+E`.*

*k) Knip de laatste regel met `Ctrl+K` → `Ctrl+/` → `1,1` → `Enter` → plak met `Ctrl+U`.*

*l) Aantal regels/woorden/tekens: `Alt+D`.*

*m) `Ctrl+S`, daarna `Ctrl+X`.*
:::

## Oefening 16
**Extra challenge:** gebruik het commando `head` om alles in het bestand `/etc/passwd` af te drukken, zonder het aantal regels in het bestand te kennen. Je zal in de manpage moeten zoeken naar een oplossing. Probeer dit nu ook met het commando `tail`.

::: details Oplossing tonen
```
head -n -0 /etc/passwd
```
```
tail -n +1 /etc/passwd
```
*`head -n -0` betekent: alles behalve de laatste 0 regels. `tail -n +1` betekent: alles vanaf regel 1.*
:::

## Oefening 17
We kunnen `cat` gebruiken om de inhoud van meerdere bestanden onder elkaar af te drukken, maar het is moeilijk om te zien welk deel uit welk bestand komt. Met `head` en `tail` kan je dit oplossen. Druk de **volledige** inhoud van `mytextfile` en `myechotextfile` af, **samen met de bestandsnamen**.

*Hint: bekijk de manpages van `head` en `tail` en combineer met wat je in oefening 16 leerde.*

::: details Oplossing tonen
```
tail -n +1 mytextfile myechotextfile
```
```
head -n -0 mytextfile myechotextfile
```
*Bij **meerdere bestanden** zetten `head` en `tail` automatisch de bestandsnaam erboven (`==> naam <==`). Werk je met **één** bestand en wil je toch de naam zien, dan gebruik je de optie `-v` (verbose):*

```
head -v mytextfile
```
:::

## Oefening 18 (extra)
Toon enkel de regels **5 t/m 8** van `/etc/passwd`. Je mag hiervoor `head` en `tail` combineren met het teken `|` (pipe). Dat leren we in een later hoofdstuk, maar je kan het al proberen.

*Hint: neem eerst de eerste 8 regels, en hou daar de laatste 4 van over.*

::: details Oplossing tonen
```
head -n 8 /etc/passwd | tail -n 4
```
*De pipe `|` geeft de uitvoer van het eerste commando door als invoer aan het tweede.*
:::

## Optionele oefening
Gebruik het commando `vimtutor` om te leren hoe je `vim` gebruikt. Wat is er zo anders aan deze editor?

::: details Oplossing tonen
```
vimtutor
```
*Vim is **modaal**: je wisselt tussen NORMAL (navigeren en bewerken met commando's), INSERT (tekst invoeren) en REPLACE (tekst vervangen). Je werkt met sneltoetsen en commando's. Uit vim raak je met `Esc` en dan `:q!` (zonder opslaan) of `:wq` (opslaan en afsluiten).*
:::
