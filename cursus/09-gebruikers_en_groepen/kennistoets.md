---
outline: deep
---

# Kennistoets: Gebruikers en Groepen

Klik een antwoordoptie aan of denk er eerst zelf over na voor je de oplossing bekijkt.

<FillIn
  vraag="Het bestand dat de gecodeerde wachtwoorden van gebruikers bevat is ___. (volledig pad)"
  antwoord="/etc/shadow"
/>

<Quiz vraag="Een gebruiker kan nooit meer dan één UID tegelijkertijd hebben." opties="Waar|Niet waar" :correct="0">

**Waar.**

Elke gebruiker heeft precies één UID (User ID). Dit getal identificeert de gebruiker uniek in het systeem. Het is wel mogelijk dat twee gebruikersnamen hetzelfde UID delen (wat je moet vermijden), maar een gebruiker bezit slechts één UID tegelijk.

</Quiz>

<Quiz vraag="Met welk commando verwijder je een gebruiker én zijn homefolder? (commando met optie)" opties="remove|usermod -r|deluser|userdel -r" :correct="3">

**`userdel -r`**

`userdel` verwijdert de gebruiker uit de systeembestanden (`/etc/passwd`, `/etc/shadow`, `/etc/group`). De optie `-r` zorgt er bovendien voor dat de homefolder en de mailspool van de gebruiker ook worden verwijderd.

</Quiz>

<FillIn
  vraag="Het commando om een nieuwe gebruiker aan te maken is ___. (enkel commando)"
  antwoord="useradd of adduser"
  patroon="useradd( -m)?|adduser"
/>

<Quiz vraag="Wat is het doel van de homefolder van een gebruiker?" opties="Het is een logboek van systeemactiviteit.|Het is de systeemmap voor applicaties.|Het is een tijdelijke opslagplaats voor bestanden.|Het is de persoonlijke map waar bestanden van de gebruiker worden opgeslagen." :correct="3">

**Het is de persoonlijke map waar bestanden van de gebruiker worden opgeslagen.**

De homefolder (standaard `/home/<gebruikersnaam>`) is de persoonlijke werkruimte van een gebruiker. Hier worden persoonlijke bestanden, configuratiebestanden (dotfiles zoals `.bashrc`) en documenten bewaard. Alleen de gebruiker zelf en root hebben er standaard toegang toe.

</Quiz>

<FillIn
  vraag="De shell voor nieuwe gebruikers is standaard ingesteld op ___. (twee karakters)"
  antwoord="sh"
  patroon="^(/bin/)?sh$"
/>

<Quiz vraag="Wat is de functie van het bestand /etc/group?" opties="Het bevat systeembestanden.|Het bevat gebruikersinformatie.|Het bevat informatie over groepen op het systeem.|Dit bestand bestaat niet want de naam is niet juist geschreven." :correct="2">

**Het bevat informatie over groepen op het systeem.**

`/etc/group` bevat per regel een groep met vier velden: groepsnaam, wachtwoordveld, GID (Group ID) en een lijst van gebruikers die lid zijn van die groep. Het bestand bestaat wel degelijk en is een standaard onderdeel van elk Linux-systeem.

</Quiz>

<FillIn
  vraag="De gebruikersgegevens worden bewaard in het bestand ___. (volledig pad)"
  antwoord="/etc/passwd"
/>

<Quiz vraag="Wat doet het commando 'passwd'?" opties="Wijzigt of stelt het wachtwoord van een gebruiker in.|Verwijdert een gebruiker.|Maakt een gebruiker aan met onmiddellijk ook een wachtwoord.|Voert een commando uit met het wachtwoord van root." :correct="0">

**Wijzigt of stelt het wachtwoord van een gebruiker in.**

`passwd` wordt gebruikt om het eigen wachtwoord te wijzigen. Als root kan je met `sudo passwd <gebruiker>` het wachtwoord van elke gebruiker instellen of wijzigen. Het nieuwe wachtwoord wordt gehasht opgeslagen in `/etc/shadow`.

</Quiz>

<Match
  vraag="Koppel de commando's aan hun beschrijving:"
  prompts="groups|sudo visudo|ssh-keygen|userdel -r"
  antwoorden="Toont de groepen waar de gebruiker lid van is.|Bewerkt de sudoers file.|Genereert een SSH keypair.|Verwijdert een gebruiker en diens home directory."
  afleidingen="Verwijdert recursief alle gebruikers van het systeem."
/>
