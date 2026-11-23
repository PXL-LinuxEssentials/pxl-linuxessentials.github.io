# Overzicht hoofdstuk

Hoofdstuk 11 in één blik: een bash-script schrijven en uitvoeren, variabelen en parameters gebruiken, de `PATH`-variabele begrijpen en taken plannen met `at` (eenmalig) en `cron` (herhalend).

## Een script maken en uitvoeren
Een script is een tekstbestand met commando's die na elkaar worden uitgevoerd.

```bash
#!/bin/bash
# Author: Linus Torvalds
echo "hello world"  # tekst tonen
```

* **Shebang:** de eerste regel (`#!/bin/bash`) bepaalt dat het script in bash draait.
* **Commentaar:** alles na een `#` wordt genegeerd.
* **Volgorde:** de regels worden van boven naar onder uitgevoerd.

| Uitvoeren | Voorwaarde | Opmerking |
|---|---|---|
| `./helloworld.sh` | `x`-recht (`chmod u+x helloworld.sh`) | `./` is nodig, ook in de huidige map |
| `/home/student/helloworld.sh` | `x`-recht | volledig pad |
| `bash helloworld.sh` | enkel `r`-recht | je geeft zelf de interpreter mee |
| `helloworld.sh` | `x`-recht en map staat in `PATH` | zonder pad uitvoeren |

## De variabele PATH
`PATH` is een lijst van mappen, gescheiden door `:`. Typ je een commando zonder pad, dan zoekt Linux er in elke map van de lijst naar.

| Commando | Toont |
|---|---|
| `echo $PATH` | de lijst op één regel |
| `echo $PATH \| tr ':' '\n'` | één map per regel |
| `which reboot` | in welke map het commando gevonden wordt (`/usr/sbin/reboot`) |

| Waar wijzig je `PATH`? | Geldt voor |
|---|---|
| `/etc/environment` | alle gebruikers, zichtbaar bij het aanmelden |
| `~/.profile` | enkel jouw gebruiker, zichtbaar bij het aanmelden |

::: tip ~/bin voor je eigen scripts
`.profile` voegt `~/bin` automatisch toe aan `PATH` als de map bestaat. Maak ze aan met `mkdir ~/bin`, **log opnieuw in**, en je scripts daarin werken overal zonder pad.
:::

## Variabelen en command substitution
| Wat | Voorbeeld | Resultaat |
|---|---|---|
| Eigen variabele | `CUSTOMDIR=testdir` | geen spaties rond `=` |
| Gebruiken | `echo $CUSTOMDIR` | `testdir` |
| Met accolades | `echo ${createdate}superfile` | verplicht als er tekst direct achter de naam staat |
| Systeemvariabelen | `$USER` · `$HOME` | `student` · `/home/student` |
| Command substitution | `echo "datum: $(date)"` | de uitvoer van het commando wordt ingevoegd |
| Een commando in een variabele | `createdate=$(date +"%Y-%m-%d_%H:%M:%S")` | `2025-11-11_10:38:13` |

```bash
#!/bin/bash
echo "hello $USER"
echo "your homefolder has $(ls -A1 ~ | wc -l) files/folders."
```

::: warning Accolades
Zonder accolades leest bash `$createdatesuperfile` als één variabelenaam, die niet bestaat. Gebruik `${createdate}superfile`.
:::

::: info Belgische datum
De uitvoer van `date` volgt de taalinstelling. Eenmalig: `LC_TIME=nl_BE.utf8 date`. Is de locale er nog niet, dan eerst `sudo locale-gen nl_BE.utf8`. Permanent: `sudo update-locale LC_TIME=nl_BE.UTF-8` en daarna herstarten.
:::

## Invoer en parameters
| Wat | Voorbeeld | Opmerking |
|---|---|---|
| Invoer vragen | `read folder` | het antwoord komt in de variabele `folder` |
| Parameters | `./params.sh first 2nd` | in het script: `$1` = `first`, `$2` = `2nd` |
| Het commando zelf | `$0` | de naam waarmee het script is gestart |

* Parameters lopen van `$1` tot `$9`.
* Maak het script uitvoerbaar met `chmod u+x` voor je `./params.sh` gebruikt.

```bash
#!/bin/bash
echo "Geef het absolute pad van de map die je wil controleren:"
read folder
echo "De map bevat $(ls -A1 $folder | wc -l) bestanden/mappen."
ls -A1 $folder | head -5
```

## De tijdzone controleren
Loopt de klok een uur te vroeg of te laat, dan staat de tijdzone fout. Dat is belangrijk voor `at` en `cron`.

| Commando | Doet |
|---|---|
| `date` | lokale tijd tonen |
| `timedatectl` | tijd, tijdzone en NTP-status tonen |
| `sudo timedatectl set-timezone Europe/Brussels` | tijdzone instellen |

## Eenmalig plannen met at
Installeren indien nodig: `sudo apt install at`. Je geeft het commando mee via `echo` en een pipe.

| Commando | Doet |
|---|---|
| `echo ./datefile.sh \| at 14:00` | script om 14:00 uitvoeren |
| `echo 'echo "hello" > /tmp/hello.txt' \| at now + 1 minutes` | commando over één minuut uitvoeren |
| `at -l` · `atq` | geplande taken tonen |
| `at -c 1` | tonen wat taak 1 precies uitvoert |
| `at -d 2` · `atrm 2` · `at -r 2` | taak 2 verwijderen |

* `at` voert de taken uit met `/bin/sh` (dat zegt de waarschuwing).
* Kijk in de manpage van `at` voor meer tijdsnotaties.

## Herhalend plannen met cron
**Persoonlijke crontab**

| Commando | Doet |
|---|---|
| `crontab -e` | je crontab bewerken (eerste keer: kies `1` voor nano) |
| `crontab -l` | je crontab tonen |

Eén regel per taak, vijf tijdsvelden en dan het commando:

```output
┌─────────── minuut (0-59)
│ ┌───────── uur (0-23)
│ │ ┌─────── dag van de maand (1-31)
│ │ │ ┌───── maand (1-12 of jan, feb, ...)
│ │ │ │ ┌─── dag van de week (0-6, zondag = 0 of 7, of sun, mon, ...)
│ │ │ │ │
* * * * *   echo Command ran on $(date) >> /tmp/crontest
```

| Tijdsveld | Betekenis |
|---|---|
| `* * * * *` | elke minuut |
| `30 23 * * 5` | elke vrijdag om 23:30 |
| `@reboot` | bij elke herstart (komt in de plaats van de vijf velden) |

* **Stoppen:** verwijder de regel uit je crontab.
* **Percent-teken:** in een crontab moet `%` ontsnapt worden met `\`, bv. `date +"\%F \%T"`. Voorbeeld: `@reboot echo Herstart om $(date +"\%F \%T") >> $HOME/rebootlog`.

**Systeembrede crontab: `/etc/crontab`**
* Bewerken kan enkel met `sudo`. Je hoeft `crontab` daarna niet uit te voeren.
* Er is een **extra kolom met de gebruiker** tussen de tijdsvelden en het commando.
* Voorbeeld, elke vrijdag om 23:30 een backup als root: `30 23 * * 5 root /scripts/backuphomefolders.sh`.

| Map | Bevat scripts die cron uitvoert |
|---|---|
| `/etc/cron.hourly` | elk uur |
| `/etc/cron.daily` | dagelijks |
| `/etc/cron.weekly` | wekelijks |
| `/etc/cron.monthly` | maandelijks |

## Kiezen: at of cron?
| Vraag | Antwoord |
|---|---|
| Moet de taak **één keer** draaien? | `at` |
| Moet de taak **herhaald** draaien? | `cron` (`crontab -e`) |
| Moet de taak als **root of een andere gebruiker** draaien? | `/etc/crontab` met een gebruikerskolom |
| Moet de taak bij **elke herstart** draaien? | `@reboot` in je crontab |

## Valkuilen
::: warning De vaakst gemaakte fouten
1. **`./` vergeten:** `helloworld.sh` alleen werkt enkel als de map in `PATH` staat.
2. **Geen `x`-recht:** `Permission denied`. Geef `chmod u+x` of start het met `bash script.sh`.
3. **Spaties rond `=`:** `A = 1` is fout, schrijf `A=1`.
4. **Accolades vergeten** als er tekst direct na een variabele komt.
5. **Niet opnieuw ingelogd** na het aanmaken van `~/bin` of het wijzigen van `.profile`.
6. **Verkeerde tijdzone:** `at` en `cron` draaien dan op een ander uur dan je verwacht.
7. **`%` in cron** zonder `\`.
8. **Relatieve paden in cron:** cron draait niet in je huidige map. Gebruik volledige paden.
:::

## Test jezelf
::: details 1. Wat doet de eerste regel #!/bin/bash?
Dit is de shebang: het script draait in bash.
:::

::: details 2. Op welke drie manieren kan je een script uitvoeren, en wat is er telkens nodig?
`./script.sh` (`x`-recht), met volledig pad (`x`-recht), of `bash script.sh` (alleen `r`-recht). Zonder pad kan het enkel als de map in `PATH` staat.
:::

::: details 3. Hoe zorg je dat scripts in ~/bin overal werken?
Maak de map aan met `mkdir ~/bin` en log opnieuw in. `.profile` voegt ze dan toe aan `PATH`.
:::

::: details 4. Wat doet $(date) in een script, en hoe heet dat?
Het voert `date` uit en voegt de uitvoer in op die plaats (command substitution of shell embedding). Je kan het resultaat ook in een variabele bewaren: `d=$(date)`.
:::

::: details 5. Wat toont ./params.sh a b, als het script echo $2 bevat?
`b`, want `$1` is `a` en `$2` is `b`.
:::

::: details 6. Plan het commando touch /tmp/x over 5 minuten in.
`echo 'touch /tmp/x' | at now + 5 minutes`. Controleren met `at -l`, verwijderen met `at -d <nummer>`.
:::

::: details 7. Wat betekent 0 8 * * 1 in een crontab?
Elke maandag om 08:00.
:::

::: details 8. Waarin verschilt /etc/crontab van crontab -e?
In `/etc/crontab` staat een extra kolom met de gebruiker, en je hebt `sudo` nodig om het te bewerken. Met `crontab -e` bewerk je je eigen crontab.
:::

::: details 9. Hoe laat je een commando bij elke herstart draaien?
Met `@reboot` in plaats van de vijf tijdsvelden, in je crontab.
:::

::: details 10. Waarom loopt at of cron een uur anders dan je verwacht?
De tijdzone staat fout. Controleer met `timedatectl` en stel in met `sudo timedatectl set-timezone Europe/Brussels`.
:::
