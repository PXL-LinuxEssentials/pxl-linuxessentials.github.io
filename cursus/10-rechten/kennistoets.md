# Kennistoets: Rechten

Klik een antwoordoptie aan of bedenk het antwoord zelf vóór je de oplossing bekijkt.

<Quiz vraag="Wat betekent de 'setgid' bit op een map?" opties="Het staat alleen de eigenaar toe om bestanden te bekijken.|Bestanden die in de map worden gemaakt, krijgen dezelfde groepseigenaar als de map.|Het voorkomt dat bestanden worden verwijderd.|Het verhoogt de prestaties van het systeem." :correct="1">

**Bestanden die in de map worden gemaakt, krijgen dezelfde groepseigenaar als de map.**

De `setgid` bit op een map zorgt ervoor dat nieuwe bestanden en submappen die erin worden aangemaakt automatisch de groepseigenaar van de map overerven. Dit is handig bij gedeelde mappen zodat alle teamleden bestanden kunnen lezen en bewerken zonder dat de groepseigenaar telkens handmatig moet worden aangepast.

</Quiz>

<Match
  vraag="Match de volgende commando's met hun functie:"
  prompts="chmod|chown|usermod|getfacl"
  antwoorden="Wijzig de bestandspermissies.|Verander de eigenaar van een bestand.|Wijzig de eigenschappen van een gebruiker.|Toon de access control lists van een bestand."
  afleidingen="Verandert enkel de gebruikersrechten van een file of directory."
/>

<Quiz vraag="Wat is een sticky bit?" opties="Het verhoogt de uitvoerrechten van een bestand.|Het voorkomt dat gebruikers bestanden verwijderen die niet van hen zijn.|Het maakt een bestand onleesbaar voor anderen.|Het zorgt ervoor dat het bestand bovenaan verschijnt tijdens het oplijsten van de inhoud van zijn directory." :correct="1">

**Het voorkomt dat gebruikers bestanden verwijderen die niet van hen zijn.**

De sticky bit op een map zorgt ervoor dat enkel de eigenaar van een bestand (of root) dat bestand kan verwijderen of hernoemen, ook al heeft een andere gebruiker schrijfrechten op de map. Dit wordt o.a. gebruikt op `/tmp`.

</Quiz>

<Quiz vraag="Wat is het doel van de umask-waarde?" opties="Om de standaardpermissies voor nieuwe bestanden en mappen te bepalen.|Om het besturingssysteem te herstarten in recovery mode (herstelmodus).|Om de grootte van de harde schijf te wijzigen na een herstart.|Om gebruikers te blokkeren op het systeem." :correct="0">

**Om de standaardpermissies voor nieuwe bestanden en mappen te bepalen.**

De `umask` is een maskerwaarde die wordt afgetrokken van de maximale permissies (`666` voor bestanden, `777` voor mappen). Zo bepaalt de umask welke permissies nieuw aangemaakte bestanden en mappen standaard krijgen.

</Quiz>

<Match
  vraag="Match de volgende bestandspermissies met hun betekenis:"
  prompts="r|w|x|-"
  antwoorden="Lezen van een bestand.|Schrijven naar een bestand.|Uitvoeren van een bestand.|Geen rechten."
  afleidingen="Verwijderen van een bestand."
/>

<Quiz vraag="Wat is het effect van een umask-waarde 000?" opties="Nu worden nieuwe bestanden aangemaakt zonder permissies.|Nu worden nieuwe bestanden aangemaakt met alle permissies.|Nu worden nieuwe mappen aangemaakt zonder permissies.|Nu worden nieuwe mappen aangemaakt met alle permissies." :correct="3">

**Nu worden nieuwe mappen aangemaakt met alle permissies.**

Met `umask 000` wordt er niets gemaskeerd: `777 - 000 = 777`, dus mappen krijgen `rwxrwxrwx`. Voor bestanden geldt `666 - 000 = 666` (`rw-rw-rw-`), want de execute-bit wordt nooit automatisch gezet op bestanden.

</Quiz>

<Quiz vraag="Wat is het resultaat van de permissies 1775 op een directory?" opties="Geen speciale bits zijn ingesteld.|Alleen de eigenaar van de bestanden of de directory en root kunnen bestanden in deze directory verwijderen.|De sticky bit is ingesteld en schrijfrechten zijn enkel verleend aan de groep.|Geen schrijfrechten voor de groep." :correct="1">

**Alleen de eigenaar van de bestanden of de directory en root kunnen bestanden in deze directory verwijderen.**

`1775` = sticky bit (`1`) + `rwxrwxr-x` (`775`). De sticky bit zorgt ervoor dat gebruikers in de map enkel hun eigen bestanden kunnen verwijderen. De rest van de permissies geven volledige toegang aan eigenaar en groep, en lees-/uitvoerrechten aan anderen.

</Quiz>

<Quiz vraag="Wat kan je bereiken met het commando 'usermod -aG groupname username'?" opties="Verwijder de gebruiker uit een groep.|Verander de eigenaar van een bestand.|Verander de naam van de gebruiker.|Voeg een gebruiker toe aan een groep zonder andere groepslidmaatschappen te verliezen." :correct="3">

**Voeg een gebruiker toe aan een groep zonder andere groepslidmaatschappen te verliezen.**

De optie `-aG` staat voor append + groups. Zonder `-a` zou de gebruiker enkel lid zijn van de opgegeven groep en al zijn andere secundaire groepen verliezen.

</Quiz>

<Quiz vraag="Wat is het effect van het commando 'chmod 400 bestand'?" opties="De eigenaar heeft geen toegang.|Alleen de eigenaar kan het bestand lezen.|Iedereen kan het bestand lezen, maar enkel de eigenaar kan het wijzigen.|Alleen de groep kan het bestand lezen." :correct="1">

**Alleen de eigenaar kan het bestand lezen.**

`400` = `r--------`: de eigenaar heeft alleen leesrecht, de groep en anderen hebben helemaal geen toegang. Dit wordt vaak gebruikt voor gevoelige bestanden zoals SSH-sleutels.

</Quiz>

<Quiz vraag="Wat betekent de umask-waarde 022?" opties="Toegewezen rechten zijn rw-r--r-- voor nieuwe bestanden.|Toegewezen rechten zijn rw-r--r-- voor nieuwe mappen.|Alleen de eigenaar kan het bestand uitvoeren.|Iedereen heeft volledige rechten." :correct="0">

**Toegewezen rechten zijn `rw-r--r--` voor nieuwe bestanden.**

`666 - 022 = 644` → `rw-r--r--`. De eigenaar kan lezen en schrijven, groep en anderen kunnen alleen lezen. Voor mappen: `777 - 022 = 755` → `rwxr-xr-x`.

</Quiz>
