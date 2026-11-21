---
outline: deep
---

# Kennistoets: Bestanden en mappen

Klik een antwoordoptie aan of bedenk het zelf voor je de oplossing bekijkt.

<Match
  vraag="Koppel de folder actie aan het juiste commando."
  prompts="Maak een nieuwe map aan|Verander de naam van een bestand|Verwijder een bestand|Maak een kopie van een bestand"
  antwoorden="mkdir|mv|rm|cp"
  afleidingen="touch"
/>

<Match
  vraag="Koppel de termen aan hun betekenis."
  prompts="Keypair|SSH|Terminal|Cloud instance"
  antwoorden="Combinatie van een public en private key.|Veilige manier om in te loggen op een server.|Interface voor het uitvoeren van commando's.|Virtuele server in de cloud."
  afleidingen="Firewall"
/>

<FillIn
  vraag="Om het huidige werkpad weer te geven, gebruik je het commando ___."
  antwoord="pwd"
/>

<Quiz vraag="Je kan met 'sudo rm' bestanden uit de homefolder van andere gebruikers verwijderen." opties="Waar|Niet waar" :correct="0">

**Waar.**

`sudo rm` voert het verwijdercommando uit met superuser rechten. Hierdoor kan je bestanden verwijderen in mappen waar je normaal geen schrijfrechten hebt, zoals de homedirectory van andere gebruikers.

</Quiz>

<Match
  vraag="Koppel de systeemcommando's aan hun functies."
  prompts="sudo|nano|tree|cat"
  antwoorden="Voert een commando uit met superuser rechten.|Een teksteditor voor het bewerken van bestanden.|Toont de structuur van directories.|Toont de inhoud van een bestand."
  afleidingen="showfilestructure"
/>

<Quiz vraag="Wat is de correcte manier om een bestand met een spatie in de naam te maken?" opties="Verander de bestandsnaam naar een naam zonder spaties.|Gebruik aanhalingstekens of een escape-teken.|Dit gaat niet in de CLI. Hiervoor moet je de GUI gebruiken.|Gebruik het commando touch zonder aanhalingstekens." :correct="1">

**Gebruik aanhalingstekens of een escape-teken.**

Spaties hebben een speciale betekenis in de shell: ze scheiden argumenten. Je kan dit omzeilen met aanhalingstekens (`touch "mijn bestand.txt"`) of een backslash als escape-teken (`touch mijn\ bestand.txt`).

</Quiz>

<Match
  vraag="Koppel de commando's aan hun beschrijving."
  prompts="pwd|ls -a|find|cd"
  antwoorden="Toont het huidige werkpad.|Toont ook verborgen bestanden.|Zoekt naar bestanden in een directory.|Wijzig de huidige werkmap."
  afleidingen="man"
/>

<FillIn
  vraag="Een absoluut pad begint altijd met ___ (één karakter)."
  antwoord="/"
/>

<Match
  vraag="Koppel de zoekcommando's aan hun beschrijving."
  prompts="find|locate|grep|apropos"
  antwoorden="Zoekt naar bestanden op het filesysteem.|Zoekt in een database naar bestanden.|Zoekt naar tekst in bestanden.|Zoekt naar commando's gerelateerd aan een tekst."
  afleidingen="whoami"
/>

<FillIn
  vraag="De huidige map kan voorgesteld worden door ___ (één karakter)."
  antwoord="."
/>
