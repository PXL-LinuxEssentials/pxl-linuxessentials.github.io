# Kennistoets: Automatisatie

Klik een antwoordoptie aan of bedenk het antwoord zelf vóór je de oplossing bekijkt.

<Quiz vraag="Een cronjob kan worden ingesteld om elke week op dezelfde dag te draaien." opties="Waar|Niet waar" :correct="0">

**Waar.**

In de crontab-syntaxis staat het vijfde veld voor de dag van de week (0–7, waarbij 0 en 7 beide zondag zijn). Door een vaste waarde in te stellen (bijv. `0` voor zondag) wordt de cronjob wekelijks op dezelfde dag uitgevoerd.

</Quiz>

<Quiz vraag="Wat doet het commando 'chmod u+x bestandsnaam.sh'?" opties="Verwijdert leesrechten van iedereen.|Geeft uitvoerrechten aan de eigenaar van het bestand.|Geeft uitvoerrechten aan iedereen voor het bestand.|Verandert de eigenaar van het bestand." :correct="1">

**Geeft uitvoerrechten aan de eigenaar van het bestand.**

`u+x` staat voor *user + execute*: enkel de uitvoerbit van de eigenaar (`u`) wordt toegevoegd. Om uitvoerrechten aan iedereen te geven, zou je `a+x` of `chmod +x` gebruiken.

</Quiz>

<Match
  vraag="Koppel de soorten jobs aan hun beschrijving:"
  prompts="Cronjob|At job|Foreground process|Background process"
  antwoorden="Een taak die herhaaldelijk wordt uitgevoerd volgens een schema.|Een taak die op een specifiek tijdstip éénmaal zal worden uitgevoerd.|Een taak die interactie kan hebben met de eindgebruiker.|Een taak die geen interactie kan hebben met de eindgebruiker."
  afleidingen="Een taak die voor een andere taak draait en daardoor prioriteit krijgt."
/>

<Quiz vraag="Waarvoor staat de term 'shebang' in een bash-script?" opties="Het verwijst naar de hoofdmap van de gebruiker.|Het geeft aan welke interpreter moet worden gebruikt om het script uit te voeren.|Het is een type commando binnen het script.|Het is een foutmelding bij het uitvoeren van scripts." :correct="1">

**Het geeft aan welke interpreter moet worden gebruikt om het script uit te voeren.**

De shebang (`#!/bin/bash`) staat op de eerste regel van een script en vertelt het besturingssysteem welke interpreter het script moet uitvoeren. Zonder shebang wordt de standaard shell gebruikt, wat onverwacht gedrag kan veroorzaken.

</Quiz>

<Quiz vraag="Wat is de juiste manier om een variabele in een bash-script aan te roepen?" opties="Door de variabelenaam zonder dollarteken te gebruiken.|Door de variabelenaam met een spatie ervoor te gebruiken.|Door de variabelenaam tussen haakjes te plaatsen.|Door een dollarteken voor de variabelenaam te plaatsen." :correct="3">

**Door een dollarteken voor de variabelenaam te plaatsen.**

In bash gebruik je `$variabelenaam` of `${variabelenaam}` om de waarde van een variabele op te vragen. Zonder het dollarteken wordt de naam letterlijk als tekst behandeld en niet als variabele.

</Quiz>

<Quiz vraag="Welke rol speelt de variabele PATH in een Linux-systeem?" opties="Het slaat de tijdelijke bestanden op die zijn gemaakt tijdens het uitvoeren van scripts.|Het geeft de standaard shell weer die wordt gebruikt.|Het bepaalt de zoekpaden voor uitvoerbare bestanden.|Het toont het pad van het huidige script in uitvoer." :correct="2">

**Het bepaalt de zoekpaden voor uitvoerbare bestanden.**

Wanneer je een commando intypt, doorzoekt de shell alle mappen in `$PATH` van links naar rechts totdat het uitvoerbare bestand gevonden wordt. Als een map niet in `$PATH` staat, moet je het volledige pad opgeven om een script daar uit te voeren.

</Quiz>

<Quiz vraag="Wat doet het commando 'echo $(date)' binnen een bash-script?" opties="Het slaat de uitvoer van het script op in een bestand.|Het haalt de huidige datum op en toont deze in de uitvoer.|Het voert een echo commando uit op een welbepaalde tijd in de toekomst.|Het start een nieuwe shell sessie." :correct="1">

**Het haalt de huidige datum op en toont deze in de uitvoer.**

`$(date)` is command substitution: de uitvoer van het commando `date` wordt als tekst ingevoegd in de `echo`-opdracht. Het resultaat is dat de huidige datum en tijd op het scherm worden afgedrukt.

</Quiz>

<Quiz vraag="Hoe kan je een script runnen dat je hebt gemaakt in de huidige folder?" opties="Door de naam van het bestand zonder pad in te voeren.|Door het script vanuit de /bin map uit te voeren.|Door het script uit te voeren met './' voor de naam van het script.|Door de inhoud van het script te openen met een teksteditor." :correct="2">

**Door het script uit te voeren met `./` voor de naam van het script.**

De huidige map (`.`) staat standaard niet in `$PATH` om veiligheidsredenen. Door `./` te gebruiken, geef je expliciet aan dat het script in de huidige map staat. Alternatieven zijn het volledige pad opgeven of de map toevoegen aan `$PATH`.

</Quiz>

<Quiz vraag="Wat symboliseert het '#' teken in een bash-script?" opties="Het start een nieuwe regel in het script.|Het betekent dat het volgende een variabele is.|Het duidt aan dat de rest van die lijn een commentaar is.|Het geeft aan dat het volgende commando moet uitgevoerd worden als root." :correct="2">

**Het duidt aan dat de rest van die lijn een commentaar is.**

Alles na `#` op dezelfde regel wordt door de shell genegeerd bij de uitvoering. Uitzondering: de shebang `#!/bin/bash` op de allereerste regel wordt wél verwerkt door het besturingssysteem (niet door de shell zelf).

</Quiz>

<Quiz vraag="Hoe start je een bash-script dat geen uitvoerrechten heeft?" opties="Door het script gewoon te typen zonder prefix.|Door de interpreter mee te geven zoals 'bash scriptnaam'.|Door het script in een andere shell uit te voeren.|Door het script te verplaatsen naar de map /bin." :correct="1">

**Door de interpreter mee te geven zoals `bash scriptnaam`.**

Als een script geen execute-bit heeft (`chmod +x` niet uitgevoerd), kan je het toch uitvoeren door de interpreter expliciet aan te roepen: `bash show.sh` of `sh show.sh`. De shell leest het bestand dan als invoer in plaats van het als uitvoerbaar programma te starten.

</Quiz>
