# Overzicht hoofdstuk

Hoofdstuk 05 in één blik: software en pakketten installeren, bijwerken en verwijderen, en bestanden comprimeren en archiveren.

## Package manager en repositories
Een package manager zoekt in een database naar het pakket, installeert het met al zijn dependencies, ruimt ze later op en beheert updates. In Ubuntu is dat `apt`.

**sources.list** (welke repo's) → **apt update** (lijsten downloaden) → **/var/lib/apt/lists** (lokale database) → **apt install** (installeren)

| Waar | Wat staat er |
|---|---|
| `/etc/apt/sources.list` | lijst van repositories die apt gebruikt |
| `/etc/apt/sources.list.d/` | extra bronnen, bv. `ubuntu.sources` (URIs, Suites, Components) |
| `/var/lib/apt/lists/` | de gedownloade (gecachte) pakketlijsten na `apt update` |

::: info sudo en andere distributies
`apt` wijzigt het hele systeem: installeren, verwijderen en bijwerken vraagt `sudo`. `apt` is voor Ubuntu/Debian. Andere distributies gebruiken `pacman`, `rpm`, `yum`, `dnf` …
:::

## Software beheren: apt
| Je vraag | Commando |
|---|---|
| Pakketlijsten vernieuwen? | `sudo apt update` |
| Een programma zoeken voor .zip? | `apt search "\.zip file"` (`\.` = letterlijke punt) |
| Info over een pakket (versie, dependencies)? | `apt show zip` |
| Installeren (of één pakket bijwerken)? | `sudo apt install zip` |
| Verwijderen, config blijft staan? | `sudo apt remove zip` |
| Verwijderen mét configuratiebestanden? | `sudo apt purge zip` |
| Ongebruikte dependencies opruimen? | `sudo apt autoremove` |
| Alle geïnstalleerde pakketten bijwerken? | `sudo apt upgrade` |
| Alle pakketten · enkel geïnstalleerde? | `apt list` · `apt list --installed` |
| Waar staat het uitvoerbare bestand? | `which zip` → `/usr/bin/zip` |

::: warning update ≠ upgrade
`apt update` vernieuwt enkel de packagedatabase, `apt upgrade` werkt de geïnstalleerde pakketten bij. Altijd eerst `update`.
:::

```bash
student@linux-ess:~$ sudo apt install zap
E: Unable to locate package zap
```
Typefout of repo ontbreekt: pakket niet gevonden.

## Comprimeren: gzip en gunzip
Comprimeren houdt de inhoud, maar maakt het bestand kleiner (70M → 19M in de cursus).

| Commando | Doet | Resultaat |
|---|---|---|
| `gzip bestand` | comprimeert één bestand | `bestand.gz`, origineel weg |
| `gunzip bestand.gz` | decomprimeert | `bestand`, `.gz` weg |
| `ls -lh` | grootte leesbaar tonen (K, M) | vergelijk voor en na |

::: tip
`gzip` werkt op één bestand. Meerdere bestanden of mappen? Eerst samenvoegen met `tar`.
:::

## Archiveren: tar
`tar` voegt bestanden en mappen samen in één bestand. Met `-z` gaat het meteen door gzip: een tarball (`.tar.gz` of `.tgz`).

| Optie | Staat voor | Betekenis |
|---|---|---|
| `-c` | create | maak een archief |
| `-x` | extract | pak alles uit |
| `-t` | list | toon enkel de inhoud, pakt niets uit |
| `-f` | file | het volgende argument is het archief |
| `-z` | gzip | (de)comprimeren via gzip |
| `-C map` | change dir | uitpakken in die map |

| Je wil | .tar | .tar.gz (tarball) |
|---|---|---|
| Maken | `tar -cf D.tar Downloads` | `tar -czf D.tar.gz Downloads` |
| Inhoud bekijken | `tar -tf D.tar` | `tar -tzf D.tar.gz` |
| Uitpakken (hier) | `tar -xf D.tar` | `tar -xzf D.tar.gz` |
| Uitpakken in map | `tar -xf D.tar -C /tmp` | `tar -xzf D.tar.gz -C backup` |

* **Ezelsbruggetje:** *create*, *extract*, *list*, altijd met *file*.
* **Valkuil:** de map achter `-C` moet al bestaan: eerst `mkdir backup`.
* **Software als tarball:** eerst uitpakken met `tar -xzf`, dan pas gebruiken.

## zip versus tar.gz
| | zip | tar + gzip |
|---|---|---|
| Werkwijze | meerdere bestanden comprimeren in één stap | tar bundelt, gzip comprimeert |
| Maken | `zip my.zip .bashrc .profile` | `tar -czf my.tgz .bashrc` |
| Inhoud bekijken | `unzip -l my.zip` | `tar -tzf my.tgz` |
| Uitpakken | `unzip my.zip` | `tar -xzf my.tgz` |
| Eigenaar en rechten | niet bewaard: wie uitpakt wordt eigenaar | bewaard |

```bash
# uitpakken als root
student@linux-ess:/tmp$ sudo unzip zipdemo.zip         ⟵ .bashrc is van root root
student@linux-ess:/tmp$ sudo tar -xzf tardemo.tgz      ⟵ .bashrc blijft van student student
```

::: tip Backups
Daarom gebruik je op Linux `tar` voor backups: eigenaars en rechten blijven behouden.
:::

## Extra: andere spelers dpkg en snap
| | apt | dpkg | snap |
|---|---|---|---|
| Repositories | ja | nee, je hebt de .deb al nodig | snap store |
| Dependencies | automatisch | niet automatisch ("dependency hell") | zitten in de snap zelf |
| Eigenheid | standaard in Ubuntu | voorloper van apt-get/apt | eigen bubbel, distro-onafhankelijk, meerdere versies naast elkaar |

| dpkg | |
|---|---|
| `sudo dpkg -i pakket.deb` | installeren |
| `sudo dpkg-reconfigure keyboard-configuration` | pakket herconfigureren |

| snap | |
|---|---|
| `snap search` · `snap info` | zoeken · details |
| `sudo snap install` · `snap remove` | installeren · verwijderen |
| `snap list` (`--all` alle versies) | geïnstalleerde snaps |
| `snap refresh` · `snap revert` | upgraden · terug |
| `snap changes` · `snap version` | geschiedenis · versie |

::: info Geen snap update
`snap update` bestaat niet: de snap-daemon controleert zelf 4 keer per dag op updates. Kanaal: standaard *stable*, en dat houden we zo.
:::

## Test jezelf
::: details 1. Je doet sudo apt update. Zijn je programma's nu bijgewerkt?
Nee. `update` vernieuwt enkel de pakketlijsten; bijwerken doe je met `sudo apt upgrade`.
:::

::: details 2. Na sudo apt remove zip staat unzip er nog. Hoe ruim je het op?
`sudo apt autoremove`
:::

::: details 3. Pak app.tar.gz uit in de (nieuwe) map app.
`mkdir app` en daarna `tar -xzf app.tar.gz -C app`
:::

::: details 4. Waarom kies je voor een backup tar.gz en geen zip?
`tar` bewaart de eigenaar en de rechten van elk bestand, zip niet.
:::
