# Overzicht hoofdstuk

Hoofdstuk 02 in één blik: virtualisatie, een VM aanmaken in VMware Workstation en Ubuntu Server installeren.

## Virtualisatie
Een computersysteem met een besturingssysteem virtueel laten draaien op een ander systeem. Zo draaien meerdere gast-besturingssystemen, elk met eigen virtuele hardware, op één host.

**host** (je laptop) → **VMware** (virtualisatiesoftware) → **VM** (virtuele hardware) → **Ubuntu Server** (gast-OS)

| Begrip | Betekenis |
|---|---|
| Host system | de fysieke computer waarop alles draait |
| Gast-besturingssysteem | het OS dat in de VM draait |
| Virtuele machine (VM) | een virtuele computer met eigen virtuele hardware |
| Cloud instance | een gehuurde server bij een cloudprovider, met openbaar IP-adres |

::: info Cloud eerst
In de cursus werk je normaal in een cloud instance. De lokale VM is je backup, bv. als je geen internet hebt.
:::

## Wat heb je nodig?
| Wat | Uitleg |
|---|---|
| Ubuntu Server `.iso` | het installatiebestand; een .iso is een exacte kopie van een cd/dvd. Ubuntu is een op Debian gebaseerde distro. |
| Virtualisatiesoftware | VMware Workstation (gebruikt en ondersteund in de cursus), VirtualBox, Hyper-V: zelfde doel |

## Nieuwe VM aanmaken in VMware
| Scherm | Kies |
|---|---|
| Menu | File › New Virtual Machine |
| Configuratietype | Typical |
| Installatiebron | I will install the operating system later |
| Besturingssysteem | Linux, versie Ubuntu 64-bit |
| Naam en locatie | naam voor de VM, eventueel een andere map |
| Schijfgrootte | 20 GB (later uit te breiden) |
| Hardware | Customize Hardware › New CD/DVD › blader naar het .iso-bestand |
| Afronden | Finish |

::: warning Geen cloudmap
Sla de VM niet op in een map die met de cloud synchroniseert (OneDrive, Dropbox, Google Drive). Je VM crasht en je bent alles kwijt.
:::

## UEFI instellen en opstarten
Edit virtual machine settings › Options › Advanced › UEFI

**Side channel mitigations:** krijg je bij elke start een waarschuwing hierover? Die instelling vind je op dezelfde plek (Options › Advanced).

**Opstarten:** klik op het groene pijltje: de VM start en de installatie begint.

## Ubuntu Server installeren
Geen muis: navigeer met de pijltjes en {{Enter}}.

| Scherm | Kies |
|---|---|
| Opstartmenu | Ubuntu proberen of installeren: installeren |
| Taal | English |
| Installer update | overslaan (als het scherm verschijnt) |
| Toetsenbord | Belgian (AZERTY); Mac: French (Macintosh) |
| Volgende 7 schermen | niets wijzigen: Done / Continue |
| Profiel | gebruiker `student`, server `linux-ess`, wachtwoord `pxl` |
| Ubuntu Pro | Skip for now |
| Extra pakketten | enkel OpenSSH server |
| Einde installatie | Reboot now verschijnt |

1. **Vóór {{Enter}}:** VM-settings › CD/DVD › *Connect at power on* uitvinken.
2. **Herstarten:** druk op {{Enter}}. Na de herstart nog eens {{Enter}} voor de loginprompt.
3. **Inloggen:** login: `student` {{Enter}}, dan wachtwoord `pxl` {{Enter}}.

::: warning Cd/dvd loskoppelen
Vergeet je de cd/dvd los te koppelen, dan start de installatie telkens opnieuw wanneer je de VM opstart.
:::

## Extra: handige toetsen en problemen
| Probleem | Oplossing |
|---|---|
| Je muis zit "vast" in de VM | {{Ctrl+Alt}} geeft je muis terug aan Windows |
| Fout: Intel VT-x is disabled | activeer de VT-x-optie in de BIOS van je laptop |
| De installatie start bij elke boot opnieuw | CD/DVD: *Connect at power on* uitvinken |
| Je ziet je wachtwoord niet bij het typen | normaal in een CLI: gewoon typen en {{Enter}} |
| Waarschuwing over side channel mitigations | Edit virtual machine settings › Options › Advanced |

## Test jezelf
::: details 1. Wat is het verschil tussen de host en het gast-besturingssysteem?
De host is je fysieke computer; het gast-OS (Ubuntu Server) draait in de VM erop.
:::

::: details 2. Waarom kies je bij het aanmaken "I will install the operating system later"?
Je koppelt het .iso-bestand zelf via Customize Hardware › New CD/DVD.
:::

::: details 3. Waarom mag je VM niet in je OneDrive-map staan?
De synchronisatie doet de VM crashen en je verliest alles.
:::

::: details 4. Na een herstart begint de installatie opnieuw. Wat ben je vergeten?
De cd/dvd loskoppelen: *Connect at power on* uitvinken in de VM-settings.
:::
