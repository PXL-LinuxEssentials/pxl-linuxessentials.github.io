# Overzicht hoofdstuk

Hoofdstuk 03 in één blik: de command line interface, de prompt, commando's met opties en argumenten, hulp via manpages en de shell history.

## De CLI en de prompt
Ubuntu Server heeft geen GUI: geen muis, alleen het toetsenbord. Dat bespaart systeembronnen, verkleint het aanvalsoppervlak en maakt automatiseren makkelijker.

| | CLI | GUI |
|---|---|---|
| Voluit | command line interface | graphical user interface |
| Invoer | enkel toetsenbord | muis en toetsenbord |
| Sterk in | efficiënt, betrouwbaar, automatisering | visueel werken |

**De prompt ontleed**

```bash
student@linux-ess:~$ ⟵ gebruiker @ hostnaam : huidige map $
```

* `~` = homefolder `/home/student`, te vergelijken met `C:\Users\student`.
* `$` = gewone gebruiker. De `$` sluit de prompt af en toont dat je als gewone gebruiker bent ingelogd. Daarna typ je je commando.

::: tip Wachtwoord typen
Bij het inloggen zie je je wachtwoord niet terwijl je typt. Dat is normaal: typ het gewoon en druk op {{Enter}}.
:::

## Commando's, opties en argumenten
```bash
student@linux-ess:~$ sudo shutdown -r now ⟵ sudo = als root, shutdown = commando, -r = optie, now = argument
```

| Onderdeel | Herken je aan | Voorbeeld |
|---|---|---|
| Commando | het eerste woord: wat moet er gebeuren | `echo`, `shutdown` |
| Optie | begint met een koppelteken; breidt de werking uit | `-r`, `--help` |
| Argument / parameter | gescheiden door spaties; waarop het commando werkt | `echo hello world` |

::: warning Hoofdlettergevoelig
Alles in Linux is hoofdlettergevoelig: commando's, opties, argumenten, bestands- en mapnamen. Elk commando heeft zijn eigen set opties.
:::

## Afsluiten en herstarten: sudo shutdown
`sudo` = *super user do*: voert het commando uit als root (vergelijk: administrator in Windows).

| Je vraag | Commando |
|---|---|
| De VM correct afsluiten, nu meteen? | `sudo shutdown now` |
| Zonder tijd opgeven? | `sudo shutdown` (gepland na 1 minuut) |
| Herstarten? | `sudo shutdown -r now` (`--reboot`) |
| Uitschakelen (standaard)? | `sudo shutdown -P now` (`--poweroff`) |
| Enkel stoppen (halt)? | `sudo shutdown -H now` (`--halt`) |
| Een geplande shutdown annuleren? | `sudo shutdown -c` |
| Korte hulptekst? | `shutdown --help` |

::: tip
`sudo shutdown now` is dé correcte manier om je virtuele machine af te sluiten.
:::

## Hulp zoeken: man
Manpages (*manual pages*) beschrijven alle geïnstalleerde commando's, maar ook configuratie- en systeembestanden.

| Commando | Doet |
|---|---|
| `man shutdown` | manpage van een commando |
| `man sudo.conf` | manpage van een configuratiebestand |
| `man man` | alles over manpages zelf |
| `man -k shutdown` | zoekt in de beschrijvingen van commando's |
| `apropos shutdown` | hetzelfde als `man -k` |

| Toets in een manpage | Doet |
|---|---|
| {{Space}} · {{↑}} {{↓}} | volgende pagina · regel per regel |
| `/woord` + {{Enter}} | zoeken |
| `n` · `N` | volgende · vorige treffer |
| `g` · `G` | eerste · laatste regel |
| `h` | hulp |
| `q` | afsluiten (*quit*) |

::: tip
Typ eerst `g` (naar de eerste regel) en begin dán pas te zoeken met `/`.
:::

## Manpage-secties, whatis en whereis
Hetzelfde woord kan een commando én een configuratiebestand zijn. Het getal tussen haakjes is de sectie.

```bash
student@linux-ess:~$ apropos passwd
```
```output
passwd (1)       - change user password          <- het commando
passwd (1ssl)    - compute password hashes
passwd (5)       - the password file             <- het bestand /etc/passwd
```

| Commando | Doet |
|---|---|
| `man passwd` | opent de eerste sectie die gevonden wordt (hier 1: het commando) |
| `man 5 passwd` | opent sectie 5: het configuratiebestand `/etc/passwd` |
| `whatis route` | korte beschrijving, zonder de manpage te openen |
| `whereis -m ls` | locatie van de manpage: `/usr/share/man/man1/ls.1.gz` |

::: info Gecomprimeerd
Manpages zijn gecomprimeerde tekstbestanden (`.gz`, vergelijkbaar met zip). `man ls` opent eigenlijk `ls.1.gz`.
:::

## Snelle hulp met tldr
Snel hulp bij een commando, in het Nederlands, met korte praktische voorbeelden. Dat doet `tldr`, kort voor *too long; didn't read*. Eerst installeren en de pagina's ophalen, dan een alias maken, dan gebruiken. Het pakket heet `tealdeer`, het commando dat je typt is `tldr`.

| Commando | Doet |
|---|---|
| `sudo apt install tealdeer` | installeert de client |
| `tldr --update` | haalt de (Engelse) hulppagina's op en bewaart ze lokaal |
| `tldr -L nl --update` | haalt ook de Nederlandse pagina's op (`-L` = taal) |

::: warning Eerst updaten
Zonder `--update` heb je geen pagina's. Voer het één keer uit, daarna werkt het offline.
:::

**Alias `hulp` maken**

```bash
student@linux-ess:~$ echo "alias hulp='tldr -L nl'" >> ~/.bashrc
student@linux-ess:~$ source ~/.bashrc
```

| Onderdeel | Betekent |
|---|---|
| `>> ~/.bashrc` | voegt de regel toe aan het einde van je profielbestand. Bij elke nieuwe bash-shell wordt dat uitgevoerd |
| `source ~/.bashrc` | laadt het bestand nu meteen, zodat de alias in deze shell werkt |

::: danger Gebruik >>, nooit >
Met één pijltje overschrijf je je hele `.bashrc`.
:::

| Commando | Doet |
|---|---|
| `hulp tar` | korte Nederlandse uitleg met voorbeelden voor `tar` |
| `hulp <commando>` | hetzelfde voor elk ander commando |
| `tldr -L nl tar` | de lange vorm, zonder alias |

**hulp (tldr)** = korte, praktische voorbeelden, handig om snel te weten hoe je iets gebruikt. **man** = de volledige handleiding met alle opties, handig om alles op te zoeken.

::: details Test jezelf: tldr
**Wat doet `tldr -L nl --update`?** Het haalt de Nederlandse hulppagina's op.

**Waarom `>>` en niet `>` in het alias-commando?** Met `>>` voeg je toe, met `>` overschrijf je je hele `.bashrc`.

**Waarom `source ~/.bashrc`?** Zodat de alias meteen werkt, zonder een nieuwe shell te openen.
:::

## Extra: shell history
De shell (in Ubuntu: `bash`) is het programma dat je commando's in de CLI leest en uitvoert. Ze onthoudt je vorige commando's, zodat je ze kunt herhalen, aanpassen of opzoeken.

| Je vraag | Commando / toets |
|---|---|
| Vorige commando's terughalen? | {{↑}} · {{↓}} |
| Het laatste commando opnieuw? | `!!` ("bang bang") |
| Laatste commando opnieuw, maar met sudo? | `sudo !!` |
| De laatste 10 commando's tonen? | `history 10` |
| Commando nr. 261 opnieuw uitvoeren? | `!261` |
| Achterwaarts zoeken (nieuw naar oud)? | {{Ctrl+R}} + zoektekst, nog eens {{Ctrl+R}} voor de volgende |
| Gevonden commando uitvoeren · stoppen? | {{Enter}} · {{Ctrl+C}} |

**Niet in de history:** een commando dat begint met een spatie (in sommige distributies) en een commando dat identiek is aan het vorige.

```bash
student@linux-ess:~$ cat /etc/shadow
cat: /etc/shadow: Permission denied
student@linux-ess:~$ sudo !!
sudo cat /etc/shadow
```

::: info
`/etc/shadow` bevat de wachtwoorden van de gebruikers en is om veiligheidsredenen enkel leesbaar voor root.
:::

## Test jezelf
::: details 1. Wat zijn het commando, de optie en het argument in shutdown -r now?
`shutdown` is het commando, `-r` de optie, `now` het argument.
:::

::: details 2. Je wilt de manpage van het bestand /etc/passwd, niet van het commando. Wat typ je?
`man 5 passwd`
:::

::: details 3. Je krijgt "Permission denied". Hoe voer je hetzelfde commando snel opnieuw uit als root?
`sudo !!`
:::

::: details 4. Je weet de naam van een commando niet, wel dat het iets met shutdown te maken heeft. Hoe zoek je?
`man -k shutdown` of `apropos shutdown`
:::
