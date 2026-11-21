---
outline: deep
---

# Kennistoets: Geavanceerde commandostructuren

Klik een antwoordoptie aan of bedenk het zelf voor je de oplossing bekijkt.

<Quiz vraag="Hoe maak je een bestand aan met de naam 'userinfo' met de huidige gebruikersnaam als inhoud?" opties="echo $USER > userinfo|nano userinfo $USER|touch userinfo|echo userinfo > $USER" :correct="0">

**`echo $USER > userinfo`**

`$USER` is een omgevingsvariabele met de huidige gebruikersnaam. Het `>`-teken leidt de uitvoer van `echo` om naar het bestand `userinfo` (en maakt het aan als het nog niet bestaat).

</Quiz>

<FillIn
  vraag="Een wildcard dat nul of meer tekens vertegenwoordigt in de bestandsnaam is ___."
  antwoord="*"
/>

<Quiz vraag="Wat is het doel van de alias opdracht in de shell?" opties="Om commando's te verwijderen.|Om fouten te negeren.|Om complexe commando's simpelere namen te geven.|Om de shell te resetten." :correct="2">

**Om complexe commando's simpelere namen te geven.**

Met `alias` kan je een kortere of eenvoudigere naam koppelen aan een (reeks) commando('s). Bijvoorbeeld: `alias ll="ls -la"`.

</Quiz>

<Quiz vraag="De foutuitvoer kan niet worden omgeleid naar een bestand." opties="Waar|Niet waar" :correct="1">

**Niet waar.**

Foutuitvoer (stderr, stream 2) kan worden omgeleid met `2>`. Bijvoorbeeld: `commando 2> errors.txt` schrijft foutmeldingen naar het bestand `errors.txt`. Met `2>/dev/null` worden ze genegeerd.

</Quiz>

<Quiz vraag="De commando's '&&' en '||' kunnen worden gebruikt om logische operatoren in shell scripts aan te geven." opties="Waar|Niet waar" :correct="0">

**Waar.**

`&&` voert het volgende commando uit als het vorige geslaagd is (exit code 0). `||` voert het volgende commando uit als het vorige mislukt is (exit code ≠ 0).

</Quiz>

<Match
  vraag="Match de termen met de juiste beschrijvingen:"
  prompts="alias|bash|stdout|stderr"
  antwoorden="Een ingebouwde naam voor een complex commando.|De standaard shell in Ubuntu.|De standaard uitvoer stream.|De stream voor foutmeldingen."
  afleidingen="Commando om het netwerk te herstarten."
/>

<Quiz vraag="Wat is de output van 'echo Hello#world'?" opties="Hello#world|Hello|#world|Hello world" :correct="0">

**`Hello#world`**

Het hekje (`#`) wordt alleen als commentaar behandeld als er een spatie voor staat. `Hello#world` is één aaneengesloten argument, dus de volledige string wordt afgedrukt.

</Quiz>

<FillIn
  vraag="De foutuitvoer van een commando kan worden omgeleid naar ___ om deze te negeren."
  antwoord="/dev/null"
/>

<FillIn
  vraag="Een bestand dat je best gebruikt om aliassen op te slaan is ___ in je home directory."
  antwoord=".bash_aliases"
/>

<Quiz vraag="Wat geeft de opdracht 'find /' zonder extra opties weer?" opties="Alle foutmeldingen van het systeem.|Een lijst van actieve processen.|Een lijst van bestanden vertrekkend vanaf de root-directory.|Alle geconfigureerde netwerken." :correct="2">

**Een lijst van bestanden vertrekkend vanaf de root-directory.**

`find /` doorzoekt het volledige bestandssysteem recursief vanaf de root (`/`) en toont elk bestand en elke map. Zonder extra opties worden alle gevonden paden afgedrukt.

</Quiz>
