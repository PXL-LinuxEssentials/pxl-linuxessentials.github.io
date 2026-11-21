---
outline: deep
---

# Kennistoets: Software en pakketten

Klik een antwoordoptie aan of bedenk het zelf voor je de oplossing bekijkt.

<Quiz vraag="Het commando 'apt' kan ook worden gebruikt om softwarepakketten te verwijderen." opties="Waar|Niet waar" :correct="0">

**Waar.**

`apt remove <pakket>` verwijdert een geïnstalleerd pakket. Met `apt purge <pakket>` worden ook de configuratiebestanden verwijderd.

</Quiz>

<Quiz vraag="Wat moet je controleren als je een nieuwe package wilt installeren met apt?" opties="Of de cache is bijgewerkt|Of de firewall uit staat|Of je als root gebruiker bent ingelogd|Of de server aanstaat" :correct="0">

**Of de cache is bijgewerkt.**

Met `sudo apt update` wordt de lokale apt-cache bijgewerkt. Zo weet apt welke pakketten en versies beschikbaar zijn in de repositories. Zonder dit kan je een verouderde versie installeren of het pakket helemaal niet vinden.

</Quiz>

<Quiz vraag="Welke bestandsextensie gebruiken tar-ballen meestal?" opties=".iso|.zip|.rar|.tar.gz" :correct="3">

**.tar.gz.**

Een tarball is een archief gemaakt met `tar` (`.tar`) dat daarna gecomprimeerd is met `gzip` (`.gz`). De volledige extensie is `.tar.gz`. (De verkorte vorm `.tgz` bestaat ook.) `.zip` en `.rar` zijn andere archiefformaten.

</Quiz>

<Quiz vraag="Wat doet het commando 'gzip'?" opties="Het test de integriteit van softwarepakketten.|Het archiveert een bestand zonder compressie.|Het comprimeert een bestand om zijn grootte te verkleinen.|Het decrypted beveiligde bestanden." :correct="2">

**Het comprimeert een bestand om zijn grootte te verkleinen.**

`gzip` comprimeert één bestand en vervangt het origineel door een `.gz`-versie. Het wordt vaak gecombineerd met `tar` om gecomprimeerde archieven (tarballs) te maken.

</Quiz>

<FillIn
  vraag="De webserver luistert standaard op poort ___ voor inkomend HTTP-verkeer."
  antwoord="80"
/>

<Match
  vraag="Koppel de commando's aan hun functies:"
  prompts="sudo apt update|sudo apt upgrade|sudo apt install [pakket]"
  antwoorden="Downloaden van de repositories naar de lokale apt-cache|Upgraden van geïnstalleerde pakketten|Installeren van een specifiek pakket"
  afleidingen="sudo apt remove|Verwijderen van een pakket"
/>

<Match
  vraag="Match software met het juiste gebruik of doel:"
  prompts="Nginx|apt|tar"
  antwoorden="Webserver|Package manager voor Ubuntu|Archiveren van bestanden"
  afleidingen="Ubuntu|Besturingssysteem"
/>

<Quiz vraag="Wat is het verschil tussen 'apt remove' en 'apt purge'?" opties="Er is geen verschil; ze zijn identiek.|'apt remove' verwijdert alleen afhankelijkheden.|'apt purge' verwijdert ook configuratiebestanden van de software.|'apt purge' kan geen software verwijderen." :correct="2">

**'apt purge' verwijdert ook configuratiebestanden van de software.**

`apt remove` verwijdert de software maar laat configuratiebestanden staan. `apt purge` verwijdert zowel de software als alle bijbehorende configuratiebestanden, wat handig is bij een volledige herinstallatie.

</Quiz>

<Quiz vraag="Waarom is het uitvoeren van 'sudo apt update' belangrijk voordat je een pakket installeert?" opties="Het zorgt ervoor dat alle installaties automatisch gebeuren.|Het verbergt systeemfouten.|Het vermindert de systeembelasting.|Om ervoor te zorgen dat je de meest actuele lijst van beschikbare pakketten hebt." :correct="3">

**Om ervoor te zorgen dat je de meest actuele lijst van beschikbare pakketten hebt.**

`sudo apt update` synchroniseert de lokale pakketlijst met de repositories. Zonder deze stap kan apt een pakket niet vinden of een verouderde versie installeren.

</Quiz>

<Quiz vraag="Wat is een 'snap' in de context van software-installatie?" opties="Een beveiligingsupdate voor het besturingssysteem.|Een type compressieformaat.|Een specifieke versie van een softwarepakket.|Een bundel software met al zijn dependencies ingepakt in één bestand." :correct="3">

**Een bundel software met al zijn dependencies ingepakt in één bestand.**

Een snap is een universeel pakketformaat dat de applicatie samen met al zijn dependencies verpakt. Hierdoor werkt het op verschillende Linux-distributies zonder conflicten met systeembibliotheken.

</Quiz>

<Quiz vraag="Wat geeft 'apt show <pakket>' aan?" opties="Een lijst van alle geconfigureerde pakketten.|Gedetailleerde informatie over het opgegeven pakket.|Een index van opstartprogramma's.|Een foutmelding over een niet-beschikbaar pakket." :correct="1">

**Gedetailleerde informatie over het opgegeven pakket.**

`apt show <pakket>` toont informatie zoals de versie, beschrijving, grootte, afhankelijkheden en de repository waar het pakket vandaan komt.

</Quiz>

<Quiz vraag="Wat doet het commando 'tar -czf' in Linux?" opties="Het verfijnt een pakketlijst.|Het maakt een gecomprimeerd archiefbestand aan.|Het pakt een archiefbestand uit.|Het installeert nieuwe softwarepakketten." :correct="1">

**Het maakt een gecomprimeerd archiefbestand aan.**

De opties staan voor: `c` = create (aanmaken), `z` = gzip-compressie toepassen, `f` = het volgende argument is de bestandsnaam van het archief. Samen maken ze een gecomprimeerde tarball.

</Quiz>

<Quiz vraag="Wat is de primaire functionaliteit van het bestand /etc/apt/sources.list?" opties="Het geeft de repositories aan waar apt in kan zoeken voor pakketten.|Het bevat systeembestanden en logboeken.|Het is een configuratiebestand voor de gebruikersinterface.|Het verwijdert ongebruikte software." :correct="0">

**Het geeft de repositories aan waar apt in kan zoeken voor pakketten.**

Op oudere Ubuntu-versies staan de repositories in `/etc/apt/sources.list`; vanaf Ubuntu 24.04 staan ze standaard in `/etc/apt/sources.list.d/ubuntu.sources`. Beide bevatten de URLs van de softwarebronnen (repositories). Wanneer je `sudo apt update` uitvoert, worden deze bronnen geraadpleegd om de beschikbare pakketten te bekijken.

</Quiz>

<Quiz vraag="Wat zijn dependencies in de context van software-installatie?" opties="Bestanden die handmatig moeten worden gedownload.|Softwarecomponenten die nodig zijn voor de werking van een andere applicatie.|Verouderde softwareversies.|Optionele programma-add-ons." :correct="1">

**Softwarecomponenten die nodig zijn voor de werking van een andere applicatie.**

Dependencies zijn bibliotheken of andere pakketten waarvan een applicatie afhankelijk is om te werken. `apt` lost deze automatisch op bij installatie.

</Quiz>

<FillIn
  vraag="Een bestand dat je gecomprimeerd hebt met zip kan je terug uitpakken met ___."
  antwoord="unzip"
/>
