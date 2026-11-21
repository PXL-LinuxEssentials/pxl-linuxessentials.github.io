# Overzicht hoofdstuk

Hoofdstuk 04 in één blik: werken met mappen, paden, mapinhoud tonen, bestanden en mappen beheren en zoeken.

## Werken met mappen: pwd, cd, tree
| Je vraag | Commando |
|---|---|
| In welke map sta ik? | `pwd` → `/home/student` |
| Naar een andere map? | `cd /etc` |
| Terug naar mijn homefolder? | `cd ~` of gewoon `cd` |
| Terug naar de vorige map? | `cd -` |
| Boomstructuur van de huidige map? | `tree` |
| Ook verborgen bestanden (.naam)? | `tree -a` |
| Boom van een andere map? | `tree /etc/dhcp` |

* `/` = root directory: het hoogste niveau. Geen schijfletters: in Windows begint een pad met `C:\`.
* `~` = homefolder `/home/student`, zoals `C:\Users`. Daar heb je alle rechten.
* **Tab-completion:** druk op {{Tab}} om commando's, bestands- en mapnamen aan te vullen.

## Paden: absoluut versus relatief
| | Absoluut pad | Relatief pad |
|---|---|---|
| Begint bij | de root: altijd met `/` | de huidige map |
| Voorbeeld | `cd /home/student/Downloads` | `cd Downloads/Steam/games` |
| Werkt | vanuit elke map hetzelfde | hangt af van waar je staat (`pwd`) |

| Afkorting | Verwijst naar | Voorbeeld |
|---|---|---|
| `.` | de huidige map | `ls -alh .` |
| `..` | de bovenliggende map | `cd ..` |
| `~` | de homefolder van de gebruiker | `cd ~` |

```bash
# vanuit /home/student/Downloads twee niveaus omhoog, dan naar teacher
student@linux-ess:~/Downloads$ cd ../../teacher       ⟵ wordt /home/teacher
```

::: info Slash achteraan
Een slash achteraan een map is optioneel: `cd /home/student/` = `cd /home/student`.
:::

## Wat staat er? ls en file
| Commando | Doet |
|---|---|
| `ls` | inhoud van de huidige map |
| `ls /` | inhoud van een opgegeven map (absoluut of relatief pad) |
| `ls -a` | *all*: ook verborgen bestanden (beginnen met een punt, bv. `.bashrc`) |
| `ls -l` | *long listing*: rechten, eigenaar, grootte, datum |
| `ls -h` | *human readable*: groottes in K, M, G in plaats van bytes |
| `ls -alh` | combineren mag, in elke volgorde: `-a -l -h` = `-hal` |
| `file bestand` | toont het bestandstype (extensies zijn niet verplicht in Linux) |

```output
-rw-r--r-- 1 student student 3.7K Oct  5 13:40 .bashrc
rechten    eigenaar groep   grootte  laatst gewijzigd  naam
```

::: tip Alles is een bestand
Alles in Linux is een bestand: ook mappen, je harde schijf, een USB-stick en je toetsenbord.
:::

## Aanmaken, verplaatsen, kopiëren
| Commando | Doet | Voorbeeld |
|---|---|---|
| `mkdir map` | maakt een map | `mkdir backups` |
| `mkdir -p pad` | maakt ook de ontbrekende tussenmappen | `mkdir -p backups/Steam/games` |
| `touch bestand` | maakt een leeg bestand | `touch "File Two"` |
| `mv bron doel` | verplaatst een bestand of map | `mv aFile aFolder/` |
| `mv oud nieuw` | hernoemt (of verplaatst én hernoemt) | `mv aFile ../newFileName` |
| `cp bron doel` | kopieert een bestand | `cp myFile myFolder/` |
| `cp -r map kopie` | kopieert een map recursief (met inhoud) | `cp -r myFolder/ myFolder.backup` |
| `cp -i bron doel` | interactief: vraagt eerst of overschrijven mag | `cp -i myFile myFolder/` |

::: warning Drie valkuilen
1. `touch File One` maakt twee bestanden. Spaties? Gebruik `"..."`, `'...'` of `File\ One`.
2. `cp` overschrijft een bestaand bestand zonder te vragen. Gebruik `-i`.
3. Hoofdlettergevoelig: `walkthroughs` en `Walkthroughs` zijn twee mappen.
:::

## Hernoemen in bulk en verwijderen
`rename` hernoemt veel bestanden tegelijk met een regex: `s/zoek/vervang/`. Niet geïnstalleerd? `sudo apt -y install rename`.

| Commando | Leest als |
|---|---|
| `rename 's/file/document/' *.txt` | vervang `file` door `document` in alle namen die eindigen op `.txt` |
| `rename 's/\.txt/.odt/' *` | extensie `.txt` → `.odt`; `\.` = een échte punt |
| `rename -E 's/\.odt/.doc/i' -E 's/\.backup/.doc/' *` | meerdere regels tegelijk; `i` = hoofdletterongevoelig (`.odt` én `.ODT`) |

* **Speciale tekens escapen:** `* . $ [ ] ( ) / { }` betekenen iets in een regex. Zet er een `\` voor om ze letterlijk te bedoelen.
* **Wildcard `*`:** in bash betekent `*` nul, één of meer willekeurige tekens: `*.txt` = alles dat eindigt op `.txt`.

| Verwijderen | Doet |
|---|---|
| `rm bestand` | verwijdert een bestand |
| `rmdir map` | verwijdert enkel een lege map |
| `rm -rf map` | `-r` recursief: map met alle inhoud · `-f` force: niets vragen |

::: danger Geen vuilnisbak
Linux heeft geen vuilnisbak. Wat je met `rm` verwijdert, is voorgoed weg. Extra voorzichtig met `rm -rf` als root.
:::

## Extra: zoeken met find en locate
| | find | locate |
|---|---|---|
| Zoekt in | het bestandssysteem zelf | een database van bestanden |
| Snelheid | trager | veel sneller |
| Startmap | op te geven (standaard: huidige map + submappen) | geen: altijd het hele systeem |
| Nieuwe bestanden | meteen gevonden | pas na `sudo updatedb` |
| Hoofdletterongevoelig | `-iname` | `-i` |

| Je vraag | Commando |
|---|---|
| Alles met "sh" in de naam, hier en dieper? | `find -name "*sh*"` |
| Overal zoeken, zonder "Permission denied"? | `sudo find / -name "modem*"` |
| Overal, hoofdletterongevoelig? | `sudo find / -iname "modem*"` |
| Database bijwerken? | `sudo updatedb` |
| Snel zoeken in de database? | `locate testfile` (`sudo` voor alle mappen) |
| Hoofdletterongevoelig, enkel de bestandsnaam? | `sudo locate -i -b modem` |

::: tip Aanhalingstekens
Zet het zoekpatroon van `find` tussen aanhalingstekens (`"*sh*"`), zodat de shell de `*` niet zelf invult.
:::

## Test jezelf
::: details 1. Je staat in /home/student/Downloads. Ga met een relatief pad naar /home/teacher.
`cd ../../teacher`
:::

::: details 2. Waarom faalt mkdir backups/Steam/games/PayDay2?
De tussenmappen bestaan nog niet. Oplossing: `mkdir -p backups/Steam/games/PayDay2`.
:::

::: details 3. Je maakt testfile aan, maar locate testfile vindt niets. Waarom?
De database is nog niet bijgewerkt: eerst `sudo updatedb`.
:::

::: details 4. Kopieer de map myFolder met alle inhoud naar myFolder.backup.
`cp -r myFolder myFolder.backup`
:::
