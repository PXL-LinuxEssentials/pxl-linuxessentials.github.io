---
outline: deep
---

# Kennistoets: Bestandsinhoud

Klik een antwoordoptie aan of bedenk het zelf voor je de oplossing bekijkt.

## Deel 1: dit hoofdstuk

<Match
  vraag="Koppel de commando's aan hun beschrijvingen:"
  prompts="cat|tail|less|tac"
  antwoorden="Toont de volledige inhoud van een bestand op het scherm.|Toont de laatste regels van een bestand.|Toont bestanden met mogelijkheid om omhoog en omlaag te scrollen, per regel en per pagina.|Toont de regels van een bestand in omgekeerde volgorde."
  afleidingen="Toont bestanden met mogelijkheid om enkel omlaag te scrollen per pagina."
/>

<Quiz vraag="Het commando 'head' toont standaard de laatste 10 regels van een bestand." opties="Waar|Niet waar" :correct="1">

**Niet waar.**

`head` toont de **eerste** regels van een bestand (standaard 10). Voor de laatste regels gebruik je `tail`.

</Quiz>

<Quiz vraag="Om hoofdletterongevoelig te zoeken in less typen we '-i'." opties="Waar|Niet waar" :correct="0">

**Waar.**

Binnen `less` typ je `-i` gevolgd door `Enter` om hoofdletterongevoelig zoeken in te schakelen. Daarna gebruik je `/zoekterm` om te zoeken.

</Quiz>

<Quiz vraag="Hoe sluit je less af?" opties="Met Ctrl+C|Met q|Met Ctrl+X|Met Esc" :correct="1">

**Met `q`.**

`q` (*quit*) sluit `less` af. {{Ctrl+C}} stopt enkel een lopende actie, zoals `F` (live volgen). {{Ctrl+X}} is de afsluitcombinatie van `nano`.

</Quiz>

<Quiz vraag="Wat is het verschil tussen > en >> bij output redirection?" opties="> overschrijft het bestand, >> voegt toe aan het einde|> voegt toe aan het einde, >> overschrijft het bestand|Er is geen verschil|> werkt met echo, >> werkt met cat" :correct="0">

**`>` overschrijft, `>>` voegt toe.**

Met `>` verdwijnt de oude inhoud van het bestand meteen. Met `>>` blijft de oude inhoud staan en komt de nieuwe tekst eronder.

</Quiz>

<Quiz vraag="Je gebruikt 'cat > jokes.txt' en bent klaar met typen. Welke toetsencombinatie sluit de invoer af?" opties="Ctrl+C|Ctrl+D|Ctrl+Z|Ctrl+S" :correct="1">

**{{Ctrl+D}}.**

{{Ctrl+D}} stuurt een *end of file* (EOF) naar het lopende proces. Het bestand wordt daarna weggeschreven.

</Quiz>

<Quiz vraag="Welk commando toont de laatste 20 regels van een bestand 'log.txt'?" opties="head -n 20 log.txt|tail -n 20 log.txt|tail -f 20 log.txt|tac 20 log.txt" :correct="1">

**`tail -n 20 log.txt`.**

`-n` bepaalt het aantal regels. `-f` (follow) volgt het bestand live, en heeft geen getal als argument.

</Quiz>

<Quiz vraag="Wat gebeurt er als je 'head -n 1 a.txt b.txt' uitvoert?" opties="Enkel de eerste regel van a.txt|De eerste regel van elk bestand, met telkens de bestandsnaam erboven|Een foutmelding, want head accepteert maar één bestand|De laatste regel van beide bestanden" :correct="1">

**De eerste regel van elk bestand, met de bestandsnaam erboven.**

Bij meerdere bestanden tonen `head` en `tail` automatisch een kopregel `==> bestandsnaam <==`.

</Quiz>

<Match
  vraag="Koppel de sneltoetsen in nano aan hun functies:"
  prompts="Ctrl+S|Ctrl+X|Ctrl+K|Ctrl+U|Ctrl+W|Ctrl+\"
  antwoorden="Opslaan.|Nano afsluiten.|Knippen van een regel of selectie.|Plakken van geknipte tekst.|Zoeken naar tekst.|Zoeken en vervangen."
  afleidingen="Kopiëren naar het klembord van Windows."
/>

<Quiz vraag="Je hebt in nano per ongeluk een regel geknipt met Ctrl+K. Hoe maak je dat ongedaan?" opties="Ctrl+Z|Alt+U|Ctrl+U|Alt+E" :correct="1">

**{{Alt+U}}.**

{{Alt+U}} is *undo*. {{Alt+E}} is *redo*. {{Ctrl+U}} plakt de geknipte tekst, wat in dit geval ook werkt, maar het is geen undo.

</Quiz>

<FillIn
  vraag="Om een logbestand live te volgen gebruik je het commando tail met de optie ___ (bv. -x)."
  antwoord="-f"
  patroon="^-f$"
/>

<FillIn
  vraag="Welk commando toont de eerste 4 tekens (bytes) van /etc/passwd? Typ het volledige commando."
  antwoord="head -c 4 /etc/passwd"
  patroon="^head\s+-c\s*4\s+/etc/passwd$"
/>

## Deel 2: herhaling uit andere hoofdstukken

<Match
  vraag="Koppel de termen aan hun betekenis:"
  prompts="nginx.conf|/etc/nginx/sites-enabled|/var/www/html|/etc/passwd"
  antwoorden="Configuratiebestand voor Nginx.|Directory voor configuratiebestanden van websites die draaien op de webserver.|Default locatie van de HTML-bestanden van de default website.|Bestand met gebruikersinformatie."
  afleidingen="Bestand met de wachtwoorden van de gebruikers."
/>

<Match
  vraag="Koppel de begrippen aan hun definities:"
  prompts="Default-website|access-log|error-log"
  antwoorden="Standaard website die wordt weergegeven bij toegang tot een server.|Bevat informatie over webpagina toegang.|Bevat fouten die zijn opgetreden op de server."
  afleidingen="Bevat informatie over het gebruik van de Access database van Microsoft."
/>

<Match
  vraag="Koppel de tools aan hun gebruiksdoelen:"
  prompts="nano|wget|tar|gzip"
  antwoorden="Teksteditor voor het bewerken van bestanden.|Downloaden van bestanden van het web.|Archiveren van meerdere bestanden in één bestand zonder compressie.|Comprimeren van één bestand."
  afleidingen="Comprimeren van meerdere bestanden in één keer."
/>

<Match
  vraag="Koppel de termen aan hun associaties:"
  prompts="scp|unzip|tac|head"
  antwoorden="Veilig kopiëren van bestanden tussen client en server.|Uitpakken van gecomprimeerde bestanden.|Toont de tekstregels van een bestand in omgekeerde volgorde.|Toont de eerste regels van een bestand."
  afleidingen="Veilig kopiëren van ssh-keypairs tussen client en server."
/>

<Match
  vraag="Koppel de sneltoetsen aan hun functies:"
  prompts="Ctrl + R|Ctrl + S , Ctrl + X|Ctrl + C|Ctrl + F5"
  antwoorden="Reverse zoeken naar eerder ingevoerde commando's.|Opslaan en afsluiten van de nano-editor.|Afbreken van een commando in uitvoering.|Harde refresh van de webpagina."
  afleidingen="Kopiëren naar het klembord."
/>

<FillIn
  vraag="Websitebestanden (html,...) moeten by default worden geplaatst in de directory ___ om zichtbaar te zijn op de webserver."
  antwoord="/var/www/html"
  patroon="^/var/www/html/?$"
/>

<FillIn
  vraag="Om de configuratiefile van de standaard website na installatie van de Nginx webserver te editeren, gebruik je het commando ___ (volledig commando)."
  antwoord="sudo nano /etc/nginx/sites-enabled/default OF sudo nano /etc/nginx/sites-available/default"
  patroon="^(sudo )?nano /etc/nginx/sites-(enabled|available)/default$"
/>
