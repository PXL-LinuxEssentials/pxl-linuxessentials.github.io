# Overzicht hoofdstuk

Hoofdstuk 01 in één blik: wat Linux is, waar het draait, hoe het is opgebouwd, de weg van Unix via GNU naar Linux, distributies en waarom Linux.

## Een besturingssysteem, net als de rest
Linux beheert de hardware en zorgt voor de communicatie tussen software en hardware, net als Windows, macOS of ChromeOS.

| Besturingssysteem | Van | Opmerking |
|---|---|---|
| Windows | Microsoft | meest gebruikt op desktops |
| macOS | Apple | via BSD een "echte" UNIX |
| ChromeOS | Google | gebouwd op de Linux-kernel |
| Linux | de gemeenschap | minder prominent op desktop; sterk op server, IoT en mobiel |

::: info Android
Android, een van de populairste platformen ter wereld, draait op de Linux-kernel.
:::

## Waar draait Linux?
| Waar | Aandeel Linux |
|---|---|
| Top-500 supercomputers | **100%** |
| Top 1 miljoen servers | **96%** |
| Cloudinfrastructuur (AWS en co) | **90%** |

Verder in: smartphones, (web)servers, tablets, IoT-toestellen, slimme wasmachines, zelfrijdende auto's, modems en routers, PlayStations, effectenbeurzen.

::: tip Overal
Linux zit overal, ook waar je het niet ziet. Alleen op het klassieke bureaublad is het het minst zichtbaar.
:::

## Zeven bouwstenen van een Linux-systeem
| # | Bouwsteen | Taak |
|---|---|---|
| 1 | Bootloader | start het systeem op |
| 2 | Kernel | het hart: beheert cpu, geheugen en randapparaten |
| 3 | Init-systeem | start de diensten op (bv. `systemd`) |
| 4 | Daemons | diensten die op de achtergrond draaien |
| 5 | Grafische server | tekent het beeld (X-server) |
| 6 | Desktopomgeving | GNOME, KDE, Xfce … |
| 7 | Toepassingen | software, via de app store van de distributie |

::: warning Ubuntu Server
Ubuntu Server heeft geen grafische server en desktopomgeving (5 en 6): je werkt in de CLI.
:::

## 1969: het ontstaan van UNIX
**Multics** (te log) → **Unics** (1969, Bell Labs) → **Unix** (herschreven in C) → **licenties** (o.a. Berkeley)

Ken Thompson en Dennis Ritchie werkten mee aan Multics, dat te log werd. In hun vrije tijd bouwden ze een eenvoudiger alternatief. De naam evolueerde van Unics naar Unix. Begin jaren '70 herschreven ze het volledig in de nieuwe taal C. AT&T mocht wettelijk niet actief zijn op de computermarkt en licentieerde de broncode aan universiteiten, waaronder Berkeley.

| Persoon | Bekend van |
|---|---|
| Ken Thompson | bedenker van UTF-8, mede-ontwikkelaar van Go |
| Dennis Ritchie | bedenker van de programmeertaal C |
| Brian Kernighan | co-auteur van "The C Programming Language" |

## Twee takken: System V versus BSD
| | System V | BSD |
|---|---|---|
| Wie | AT&T | Universiteit van Berkeley |
| Soort | de eigen commerciële versie | verder ontwikkeld, open source |
| Afgeleiden | HP-UX, Solaris | Ultrix, later FreeBSD |

Na een rechtszaak (Berkeley vs. AT&T) kwam er BSD 4.4-Lite, vrij van AT&T-broncode: de basis voor FreeBSD en, via NeXTSTEP, voor macOS.

**De UNIX-filosofie:** "Eén programma, één taak, en doe die goed." De output van het ene programma is de input van het volgende: het idee achter pipes.

**POSIX-standaard:** legt vast welke API's een besturingssysteem moet aanbieden, zodat programma's compatibel zijn tussen UNIX-varianten.

## GNU, MINIX en de Linux-kernel
**GNU (jaren '80):** gestart door Richard Stallman ("GNU's Not Unix") als reactie op de commercialisering van Unix. Bouwde vrije tools voor een open source besturingssysteem, maar miste een kernel.

**MINIX:** geschreven door Andrew Tanenbaum als educatief besturingssysteem, om studenten OS-ontwerp te leren.

**1991:** Linus Torvalds, student in Finland, kent MINIX en UNIX maar wil de beperkingen van MINIX overwinnen. Zijn kernel draait op gewone 386-pc's.

| Wanneer | Wat |
|---|---|
| 1991 | eerste Linux-kernel, met dezelfde filosofie als UNIX (System V + BSD) |
| vóór versie 1.0 | overgestapt op de GPL-licentie |
| 1992 | X Window System toegevoegd, waardoor een desktop mogelijk wordt |
| vandaag | die "hobby" wordt nog elke dag verder ontwikkeld |

::: warning Geen UNIX, wel UNIX-like
Linux is geen versie van UNIX, maar een kloon ("UNIX-like"): geen gedeelde broncode, wel dezelfde filosofie. GNU-tools + Linux-kernel = GNU/Linux.
:::

## Distro's: één kernel, honderden smaken
**Linux-kernel + GNU-utilities + eenvoudige installer = distributie.** De juiste keuze hangt af van je ervaring, je voorkeur voor de interface en je doel (desktop of server).

| Doel | Voorbeelden |
|---|---|
| Desktop | Ubuntu, Linux Mint, Manjaro, Debian, Fedora, Elementary OS, openSUSE, Arch Linux |
| Server | Red Hat Enterprise Linux, CentOS, **Ubuntu Server (deze cursus)**, SUSE Enterprise Linux, Oracle Linux |
| Specifiek doel | Clonezilla: schijven klonen en herstellen |

| Distro | Kenmerk |
|---|---|
| Debian | sinds 1993, volledig door de gemeenschap. Stabiel, met apt-pakketbeheer. Basis voor tientallen distro's. |
| Ubuntu | gebaseerd op Debian, van Canonical. Desktop, server en cloud; om de twee jaar een LTS-versie. |
| RHEL | Red Hat Enterprise Linux (IBM): commercieel, gecertificeerd, jarenlange ondersteuning. |

| Software installeren | Hoe |
|---|---|
| Grafisch | app store, bv. GNOME Software of AppCenter |
| Terminal, Debian-familie | `apt install …` |
| Terminal, Fedora-familie | `dnf install …` (vroeger `yum`) |

## Waarom Linux? Gratis, stabiel, open source
| | Linux | Windows Server |
|---|---|---|
| Kostprijs | gratis (je mag er wel geld voor vragen) | betalend, plus extra licenties per gebruiker |
| Broncode | beschikbaar: bestuderen en aanpassen mag | niet beschikbaar |
| Stabiliteit | servers draaien vaak jarenlang zonder herstart; enkel een kernelupdate vraagt een reboot | |

::: tip Vrijheid
De licenties van Linux garanderen de vrijheid om het programma voor elk doel te gebruiken én het recht om de broncode te bestuderen en aan te passen: de basis van het open-source-model.
:::

## Extra: Tux en de tijdlijn
**Waarom een pinguïn?** In 1993 wordt Linus in een zoo in Canberra (Australië) gebeten door een pinguïn en stelt er later zelf een voor als mascotte. In 1996 tekent Larry Ewing de pinguïn in GIMP. De naam Tux komt van James Hughes: "Torvalds UniX".

| Jaar | Besturingssysteem |
|---|---|
| 1969 | UNIX ontstaat bij Bell Labs |
| 1981 | MS-DOS voor de eerste IBM-pc |
| 1984 | Mac OS voor de Apple Macintosh |
| 1985 | Windows 1.0 van Microsoft |
| 1991 | Linux, door Linus Torvalds |
| 2001 | Mac OS X (BSD/UNIX-basis) en Windows XP |
| 2008 | Android, gebouwd op de Linux-kernel |
| vandaag | Linux overal: cloud, servers, supercomputers, mobiel, IoT |

## Test jezelf
::: details 1. In welke markten is Linux het sterkst, en waar minder?
Sterk op servers, supercomputers, cloud, IoT en mobiel (Android); minder prominent op de desktop.
:::

::: details 2. Welke bouwsteen start de diensten op, en hoe heet die in Ubuntu?
Het init-systeem: `systemd`.
:::

::: details 3. Wat is het verschil tussen System V en BSD?
System V is de commerciële versie van AT&T, BSD de open source tak van Berkeley.
:::

::: details 4. Wat ontbrak er aan het GNU-project, en wie vulde dat in?
Een kernel. Linus Torvalds schreef in 1991 de Linux-kernel.
:::

::: details 5. Is Linux een versie van UNIX?
Nee, een kloon ("UNIX-like"): geen gedeelde broncode, wel dezelfde filosofie.
:::

::: details 6. Waaruit bestaat een distributie?
Linux-kernel + GNU-utilities + een eenvoudige installer, bv. Ubuntu, Debian of RHEL.
:::
