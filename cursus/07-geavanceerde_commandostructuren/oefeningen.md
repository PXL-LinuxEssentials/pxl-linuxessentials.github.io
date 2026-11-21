# Oefeningen op geavanceerde commandostructuren

## File globbing

### Oefening 1
Maak een nieuwe map met de naam `FileGlobEx` met de bestanden `script.sh`, `scrupt.sh` en `scrApt.sh`. Gebruik het commando `touch` om de bestanden te maken.

::: details Oplossing tonen
```
mkdir ~/FileGlobEx && cd ~/FileGlobEx
```
```
touch script.sh scrupt.sh scrApt.sh
```
:::

### Oefening 2
Probeer het volgende commando:

```
ls scr[a-z]pt.*
```

Pas het commando aan zodat dit niet meer hoofdlettergevoelig is en test.

::: details Oplossing tonen
```
ls scr[a-zA-Z]pt.*
```
:::

### Oefening 3
Maak de volgende bestanden met slechts één commando: `script.sd`, `script.dh`, `script2.dh`, `script.ds`, `script2.ds`, `script2.dd`, `script3.ss` en `script3.ds`.

::: details Oplossing tonen
```
touch script.{sd,dh,ds} script2.{dh,ds,dd} script3.{ss,ds}
```
:::

### Oefening 4
Zoek in de map naar alle bestanden die eindigen op `.sh` of `.sd` of `.dh` of `.ds` of `.ss` of `.dd`.

Probeer dit één keer op te lossen met vierkante haken en één keer zonder.

::: details Oplossing tonen
*Zonder vierkante haken (accolades):*

```
ls *.{sh,sd,dh,ds,ss,dd}
```

*Met vierkante haken:*

```
ls *.[ds][shd]
```
:::

### Oefening 5
Zoek in de map naar alle bestanden die beginnen met `scr`, dan één willekeurig teken, gevolgd door `pt`. Na `pt` kan er een niet-gespecificeerd aantal tekens zijn, maar het bestand moet eindigen met een `h` of een `s`.

::: details Oplossing tonen
```
ls scr?pt*[hs]
```
:::

### Oefening 6
Zorg ervoor dat het commando `ls /b*` niet de inhoud van de gevonden mappen weergeeft, maar de mappen zelf. Zoek in de manpage naar een oplossing.

::: details Oplossing tonen
```
ls -d /b*
```
:::

### Oefening 7
Toon alle bestanden en mappen die eindigen op `.conf` in de map `/etc`.

::: details Oplossing tonen
```
ls /etc/*.conf
```
:::

### Oefening 8
Toon alle bestanden en mappen die eindigen op `.d` gevonden in de map `/etc`. Toon de inhoud van deze mappen niet.

::: details Oplossing tonen
```
ls -d /etc/*.d
```
:::

### Oefening 9
Toon alle bestanden en mappen uit de map `/etc` die `sh` ergens in hun naam hebben. Toon de inhoud van deze mappen niet.

::: details Oplossing tonen
```
ls -d /etc/*sh*
```
:::

### Oefening 10
Toon alle bestanden en mappen uit de map `/etc` waarvan de naam uit exact 10 tekens bestaat. Toon de inhoud van de gevonden mappen niet.

::: details Oplossing tonen
```
ls -d /etc/??????????
```
:::

### Oefening 11
Zoek in de map `/etc` naar een bestand met `os` in de naam gevolgd door `release` ergens. (Als je het bestand gevonden hebt, kan je ook altijd eens in de file gaan kijken om te achterhalen welke informatie deze bevat.)

::: details Oplossing tonen
```
ls /etc/*os*release*
```
:::

### Oefening 12
Voer het volgende commando uit en leg het resultaat uit:

```
ls -d /usr/share/bash-completion/completions/resolv*conf
```

::: details Oplossing tonen
*Het commando toont paden die matchen op `resolv*conf` in die map. De optie `-d` zorgt dat, als er mappen matchen, alleen hun naam getoond wordt (niet de inhoud). Vaak matcht dit o.a. `resolvconf`.*
:::

### Oefening 13
Zoek naar alle bestanden die beginnen met twee cijfers uit de map `/etc/grub.d`.

::: details Oplossing tonen
```
ls /etc/grub.d/[0-9][0-9]*
```
:::

### Oefening 14
Toon een lijst van alle bestanden die **niet** beginnen met een nummer uit de map `/etc/grub.d`.

::: details Oplossing tonen
```
ls /etc/grub.d/[^0-9]*
OF
ls /etc/grub.d/[!0-9]*
```
:::

## Aliases

### Oefening 1
Installeer het pakket `lolcat` en maak een alias om `lolcat` uit te voeren in plaats van `cat`. Bekijk het bestand `~/.bash_history` met `cat`.

::: details Oplossing tonen
```
sudo apt install -y lolcat
```
```
alias cat="lolcat"
```
```
cat ~/.bash_history
```
:::

### Oefening 2
Eenmaal getest, zorg ervoor dat je alias in de toekomst wordt onthouden (na opnieuw opstarten, enz.).

::: details Oplossing tonen
```
echo 'alias cat="lolcat"' >> ~/.bash_aliases
```
```
source ~/.bashrc
```
:::

### Oefening 3
Maak een alias om je scherm leeg te maken wanneer je het commando `c` geeft.

::: details Oplossing tonen
```
alias c="clear"
```
:::

### Oefening 4
Verwijder de alias `c` om je scherm leeg te maken.

::: details Oplossing tonen
```
unalias c
```
:::

### Oefening 5
Zoek in de manpage van het commando `free` om erachter te komen hoe je de resultaten in gigabytes en human readable kunt tonen. Voeg een alias toe aan het systeem die in de toekomst zal worden onthouden (na opnieuw opstarten) zodat wanneer je het commando `memory` geeft, het commando `free` wordt uitgevoerd met de juiste opties.

De output moet ongeveer als volgt zijn:

```
student@linux-ess:~$ memory
               total        used        free      shared  buff/cache   available
Mem:            3.9G        315M        3.0G        1.0M        575M        3.3G
Swap:             0B          0B          0B
```

::: details Oplossing tonen
```
man free
```
```
echo 'alias memory="free -h"' >> ~/.bash_aliases
```
```
source ~/.bashrc
```
```
memory
```
:::

## I/O-redirection

### Oefening 1
Maak een nieuw bestand met de naam `userinfo` in je homefolder. Doe dit door de uitvoer van het `echo`-commando van de variabele `$USER` om te leiden naar dit bestand.

::: details Oplossing tonen
```
echo "$USER" > ~/userinfo
```
:::

### Oefening 2
Voeg de uitvoer van een `echo` van de variabele `$UID` toe aan dit bestand.

::: details Oplossing tonen
```
echo "$UID" >> ~/userinfo
```
:::

### Oefening 3
Kopieer, zonder `sudo` te gebruiken, de map `/etc` recursief naar de map `/tmp` (= alle submappen en bestanden inbegrepen). Het is normaal om een paar foutmeldingen te krijgen! Gebruik de manpage van het kopieer commando om te zoeken naar een oplossing om recursief te kopiëren.

::: details Oplossing tonen
```
cp -r /etc /tmp
```
*`-r` is recursief. Foutmeldingen kunnen verschijnen door ontbrekende rechten.*
:::

### Oefening 4
Doe de laatste oefening nog een keer, maar stuur de foutmeldingen naar het zwarte gat.

::: details Oplossing tonen
```
cp -r /etc /tmp 2>/dev/null
```
:::

### Oefening 5
Doe dezelfde oefening opnieuw, maar stuur de foutmeldingen naar `~/backup.errors`.

::: details Oplossing tonen
```
cp -r /etc /tmp 2> ~/backup.errors
```
:::

### Oefening 6
Voer `ls /tmp/*` uit, maar verzend het resultaat en de foutmeldingen beide naar het bestand `~/contentslashtmp.full`.

::: details Oplossing tonen
```
ls /tmp/* &> ~/contentslashtmp.full
```
:::

### Oefening 7
Maak het bestand `userinfo` leeg door slechts één teken toe te voegen voor de bestandsnaam op de opdrachtregel.

::: details Oplossing tonen
```
> ~/userinfo
```
:::

## Control operators

### Oefening 1
Als je in het verleden aliassen hebt gemaakt voor de commando's `rm`, `cp` en `mv`, moet je ze verwijderen. Je kan ze vinden in de bestanden `~/.bashrc` of `~/.bash_aliases`. Verwijder deze regels uit die bestanden en start een nieuwe shell.

::: details Oplossing tonen
*Tijdelijk in huidige sessie:*

```
unalias rm; unalias cp; unalias mv
```

*Blijvend: open en verwijder de alias-regels:*

```
nano ~/.bash_aliases
```

*Nieuwe shell starten of config herladen:*

```
exec bash
```
:::

### Oefening 2
Maak een commando dat tijdens het verwijderen van het bestand `test` de foutmeldingen onderdrukt door ze naar het zwarte gat te sturen, de tekst `"Met succes verwijderd!"` toont wanneer het bestand met succes is verwijderd, en de tekst `"Kon het bestand niet verwijderen!"` geeft wanneer het bestand niet kon worden verwijderd.

::: details Oplossing tonen
```
rm test 2>/dev/null && echo "Met succes verwijderd!" || echo "Kon het bestand niet verwijderen!"
```
:::

### Oefening 3
Stel je voor dat je een back-up moet maken van alle homefolders naar de map `/backup`. Nadat de back-up is gekopieerd, moet de pc worden afgesloten. Helaas moet je gaan. Hoe kun je dit doen zodat je nu kunt vertrekken? Probeer dit eens.

Een goede back-up behoudt ook de tijdstempels en eigenaars van het bestand!

::: details Oplossing tonen
```
sudo cp -a /home /backup && sudo shutdown -h now
```
*`-a` behoudt rechten, tijdstempels en symlinks.*
:::

### Oefening 4
Maak een map `bron` en een map `bestemming` in je homefolder. Maak ook een tekstbestand `belangrijk.txt` in de map `bron`. Kopieer dit bestand naar de map `bestemming`. Als de kopie is geslaagd, verwijder je de map `bron` met `rm -rf`. Hoe kun je dit doen met slechts één opdrachtregel?

::: details Oplossing tonen
```
mkdir ~/bron ~/bestemming && echo "tekst" > ~/bron/belangrijk.txt && cp -a ~/bron/belangrijk.txt ~/bestemming/ && rm -rf ~/bron
```
:::

### Oefening 5
Wat is de uitvoer van het volgende commando? (Probeer te antwoorden zonder het eerst in de terminal te typen.)

```
echo Hello#world
```

::: details Oplossing tonen
```
Hello#world
```
:::

### Oefening 6
Wat is de uitvoer van het volgende commando? (Probeer te antwoorden zonder het eerst in de terminal te typen.)

```
echo Hello #world
```

::: details Oplossing tonen
```
Hello
```
*Het deel `#world` wordt beschouwd als commentaar door de spatie voor `#`.*
:::

### Oefening 7
Wat is de uitvoer van het volgende commando? (Probeer te antwoorden zonder het eerst in de terminal te typen.)

```
echo \\\\\??\#\"\ \\ #\\
```

::: details Oplossing tonen
```
\\??#" \
```
*Het deel `#\\` is commentaar. De backslashes voor de overige tekens zorgen voor escaping.*
:::

### Oefening 8
Wijzig de foutuitvoer van het commando `ls` zodat deze de melding `"Ik kan dit bestand of deze map niet vinden, sorry"` toont. De normale werking van het commando moet hetzelfde blijven.

::: details Oplossing tonen
```
ls /pad/dat/niet/bestaat 2>/dev/null || echo "Ik kan dit bestand of deze map niet vinden, sorry"
```
:::
