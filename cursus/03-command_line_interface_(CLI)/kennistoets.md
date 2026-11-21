---
outline: deep
---

# Kennistoets: Command Line Interface (CLI)

Klik op een antwoordoptie of denk eerst zelf na voordat je het antwoord bekijkt.

<Quiz vraag="Het commando ls toont de inhoud van een directory, terwijl ls -a ook de verborgen bestanden toont." opties="Waar|Niet waar" :correct="0">

**Waar.**

`ls` toont enkel de zichtbare bestanden en mappen. Met de optie `-a` (all) worden ook verborgen bestanden getoond — dit zijn bestanden waarvan de naam begint met een punt, zoals `.bashrc`.

</Quiz>

<Quiz vraag="Het commando 'man' geeft toegang tot de handleiding van een specifiek commando." opties="Waar|Niet waar" :correct="0">

**Waar.**

`man <commando>` opent de manual page van dat commando. Je vindt er alle opties, argumenten en voorbeelden. Navigeer met de pijltjestoetsen en sluit af met `q`.

</Quiz>

<Quiz vraag="Om de korte beschrijving van een commando te zien, gebruik je het commando ___." opties="whatis|apropos|whereis|man -k" :correct="0">

**whatis.**

`whatis ls` geeft een één-regelige beschrijving van het commando. Hetzelfde resultaat krijg je met `man -f ls`.

</Quiz>

<Quiz vraag="Met !! wordt er gerefereerd naar het vorige commando." opties="Waar|Niet waar" :correct="0">

**Waar.**

`!!` is een bash history-expansie die het volledige vorige commando herhaalt. Dit is handig om een commando opnieuw uit te voeren met sudo: `sudo !!`.

</Quiz>

<Quiz vraag="'sudo' staat gebruikers toe om commando's als de gebruiker root uit te voeren." opties="Waar|Niet waar" :correct="0">

**Waar.**

`sudo` (superuser do) laat een gebruiker die in de groep `sudo` zit toe om één commando uit te voeren met rootrechten, zonder volledig als root in te loggen.

</Quiz>

<Quiz vraag="Om de geschiedeniscache van de commando's te bekijken, typ je het commando ___ in de terminal." opties="history|recall|log|past" :correct="0">

**history.**

`history` toont een genummerde lijst van eerder uitgevoerde commando's. Commando's die beginnen met een spatie worden niet bewaard, en dubbele opeenvolgende commando's worden slechts één keer opgeslagen.

</Quiz>

<Match
  vraag="Match de commando's met hun beschrijvingen:"
  prompts="sudo|apt install|whoami|free -h"
  antwoorden="Voer een commando uit met superuser privileges.|Installeert een pakket.|Geeft de huidige gebruiker weer.|Toont geheugeninformatie in een leesbaar formaat."
  afleidingen="Toont het aantal gratis pakketten die geïnstalleerd zijn.|Toont de manpage van een commando."
/>

<Quiz vraag="Wat gebeurt er als je het commando 'sudo shutdown now' invoert?" opties="Niets gebeurt omdat het geen geldige opdracht is.|De computer wordt onmiddellijk uitgeschakeld.|De computer gaat in slaapstand.|De computer herstart onmiddellijk." :correct="1">

**De computer wordt onmiddellijk uitgeschakeld.**

`shutdown now` sluit het systeem onmiddellijk af. Met de optie `-r` (`shutdown -r now`) herstart het systeem. Zonder `sudo` geeft het commando een fout omdat rootrechten vereist zijn.

</Quiz>

<Match
  vraag="Match de commando's met hun beschrijvingen:"
  prompts="man|shutdown -r now|echo|ls -a"
  antwoorden="Toont de manual pages van een commando.|Herstart de computer onmiddellijk.|Geeft de opgegeven tekst weer.|Toont alle bestanden, inclusief verborgen."
  afleidingen="Herhaalt het laatste commando.|Zet de computer onmiddellijk uit."
/>

<Quiz vraag="Je kunt geen verborgen bestanden zien zonder extra opties in het ls commando." opties="Waar|Niet waar" :correct="0">

**Waar.**

Zonder extra opties toont `ls` enkel bestanden en mappen waarvan de naam niet begint met een punt. Gebruik `ls -a` om verborgen bestanden te zien, of `ls -la` voor een uitgebreide weergave inclusief verborgen bestanden.

</Quiz>
