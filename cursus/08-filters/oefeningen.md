# Oefeningen op Filters

## Oefening 1

Toon enkel de loginnaam van de laatste vijf gebruikers die op het systeem zijn gemaakt, van de nieuwste naar de oudste. Toon enkel de gebruikersnamen.

::: details Oplossing tonen
```
tac /etc/passwd | head -5 | cut -d: -f1
```
:::

## Oefening 2

Wat is de optie om `grep` hoofdletterongevoelig te gebruiken?

::: details Oplossing tonen
```
-i
```

*Voorbeeld:*

```
grep -i "unix" linux.txt
```
:::

## Oefening 3

Toon de regels én regelnummers uit het bestand `linux.txt` die het woord `unix` of `Unix` bevatten. Zoek in de manpage voor het tonen van de regelnummers.

Voorbeeld van `linux.txt`:

```
I'm working with Linux
It know something about Minix
The foundation is Unix
unix
Minix
Unix
Test
Test
Test
```

::: details Oplossing tonen
```
grep -n "[Uu]nix" linux.txt
```
:::

## Oefening 4

Toon de regels uit `linux.txt` die het woord `Linux`, `Minix` of `Unix` bevatten. Gebruik de optie `-e` meerdere keren om naar elke tekenreeks te zoeken.

::: details Oplossing tonen
```
grep -e Linux -e Minix -e Unix linux.txt
```
:::

## Oefening 5

Tel het aantal regels dat het woord `Unix` bevat in het bestand `linux.txt`. Gebruik slechts één commando. Het resultaat is een getal dat het aantal regels weergeeft. Doorzoek de manpage om een oplossing te vinden.

::: details Oplossing tonen
```
grep -c "Unix" linux.txt
```
:::

## Oefening 6

Toon alle regels uit het bestand `linux.txt` die beginnen met een hoofdletter.

::: details Oplossing tonen
```
grep "^[A-Z]" linux.txt
```
:::

## Oefening 7

Druk het passwd-bestand af, geordend op gebruikers-ID. Zoek in sectie 5 van de manpage van `passwd` om erachter te komen welk veld de userid bevat. Zoek in de manpage van `sort` hoe je op een welbepaald veld kan sorteren en hoe je numeriek kan sorteren. In het resultaat zou de gebruiker `nobody` normaal gezien de laatste moeten zijn.

::: details Oplossing tonen
*Veld 3 is het UID; `-t:` stelt het scheidingsteken in op `:`*

```
sort -n -t: -k3 /etc/passwd
```
:::

## Oefening 8

Tel het aantal bestanden en mappen (niet de verborgen) uit je homefolder. Houd rekening met bestandsnamen met spaties.

- Ga naar je homefolder
- Toon alle bestanden en mappen (niet de verborgen) uit de map, maar telkens één bestand per lijn (zie manpage van `ls`)
- Tel het aantal lijnen
- Het resultaat is een getal

::: details Oplossing tonen
```
cd ~
```
```
ls -1 | wc -l
```
:::

## Oefening 9

Toon alle geïnstalleerde pakketten met `apt`, maar toon enkel de naam en de versie.

Tips:
- Gooi de warnings (= foutstroom) weg.
- Gooi de regel met de tekst `Listing...` weg.

Restricties:
- Je moet `tr` gebruiken om het gemakkelijker te maken.
- Je mag maar één keer `tr` en `cut` gebruiken.

::: details Oplossing tonen
```
apt list --installed 2>/dev/null | grep -v "Listing..." | tr '/' ' ' | cut -d' ' -f1,3
```
:::

## Oefening 10

Hoeveel geïnstalleerde pakketten zijn er op jouw systeem?

::: details Oplossing tonen
```
apt list --installed 2>/dev/null | grep -v "Listing..." | wc -l
```
:::

---

# Oefeningen op Reguliere Expressies

## Oefening 1

Maak het bestand `regtest.txt` met de volgende inhoud:

```
apple
banana
apricot
pear
peach
strawberry
mango
grape
orange
5isanumber
123
123abc
abc123
35abcd35
5five5
55fivefive55
555fivefivefive555
77sevenseven77
@d
@tsign@@
atsiiiiiiiiiiiign
```

::: details Oplossing tonen
```
cat > regtest.txt <<EOF
apple
banana
apricot
pear
peach
strawberry
mango
grape
orange
5isanumber
123
123abc
abc123
35abcd35
5five5
55fivefive55
555fivefivefive555
77sevenseven77
@d
@tsign@@
atsiiiiiiiiiiiign
EOF
```
:::

## Oefening 2

Gebruik reguliere expressies om de regels te filteren die aan onderstaande voorwaarden voldoen. Werk steeds met het bestand `regtest.txt`.

**De letter `a` bevatten**

Verwachte uitvoer:
```
apple
banana
apricot
pear
peach
strawberry
mango
grape
orange
5isanumber
123abc
abc123
35abcd35
atsiiiiiiiiiiiign
```

::: details Oplossing tonen
```
grep "a" regtest.txt
```
:::

**De letter `a` of `s` bevatten**

Verwachte uitvoer:
```
apple
banana
apricot
pear
peach
strawberry
mango
grape
orange
5isanumber
123abc
abc123
35abcd35
77sevenseven77
@tsign@@
atsiiiiiiiiiiiign
```

::: details Oplossing tonen
```
grep "[as]" regtest.txt
```

*Of met een extended regex:*

```
grep -E "a|s" regtest.txt
```
:::

**De letter `a` én `s` bevatten**

Verwachte uitvoer:
```
strawberry
5isanumber
atsiiiiiiiiiiiign
```

::: details Oplossing tonen
```
grep "a" regtest.txt | grep "s"
```

*Of met slechts één commando:*

```
grep -E "a.*s|s.*a" regtest.txt
```
:::

**Een `@` bevatten**

Verwachte uitvoer:
```
@d
@tsign@@
```

::: details Oplossing tonen
```
grep "@" regtest.txt
```
:::

**Beginnen met de letter `p`**

Verwachte uitvoer:
```
pear
peach
```

::: details Oplossing tonen
```
grep "^p" regtest.txt
```
:::

**Eindigen met de letter `t`**

Verwachte uitvoer:
```
apricot
```

::: details Oplossing tonen
```
grep "t$" regtest.txt
```
:::

**Beginnen met een getal**

Verwachte uitvoer:
```
5isanumber
123
123abc
35abcd35
5five5
55fivefive55
555fivefivefive555
77sevenseven77
```

::: details Oplossing tonen
```
grep "^[0-9]" regtest.txt
```
:::

**Beginnen met een cijfer en eindigen met een letter**

Verwachte uitvoer:
```
5isanumber
123abc
```

::: details Oplossing tonen
```
grep -E "^[0-9].*[A-Za-z]$" regtest.txt
```
:::

**2 of meer opeenvolgende letters `i` bevatten**

Verwachte uitvoer:
```
atsiiiiiiiiiiiign
```

::: details Oplossing tonen
```
grep -E "i{2,}" regtest.txt
```

*Of:*

```
grep -E "ii+" regtest.txt
```
:::

**Enkel nummers bevatten**

Verwachte uitvoer:
```
123
```

::: details Oplossing tonen
```
grep -E "^[0-9]+$" regtest.txt
```
:::

**Enkel letters bevatten**

Verwachte uitvoer:
```
apple
banana
apricot
pear
peach
strawberry
mango
grape
orange
atsiiiiiiiiiiiign
```

::: details Oplossing tonen
```
grep -E "^[a-zA-Z]+$" regtest.txt
```
:::

**Een of meer cijfers bevatten, gevolgd door een of meer letters (en eventueel nog gevolgd door andere karakters)**

Verwachte uitvoer:
```
5isanumber
123abc
35abcd35
5five5
55fivefive55
555fivefivefive555
77sevenseven77
```

::: details Oplossing tonen
```
grep -E "[0-9]+[a-zA-Z]+" regtest.txt
```
:::

**Een of meer cijfers bevatten, gevolgd door een of meer letters en eindigend op een cijfer**

Verwachte uitvoer:
```
5five5
```

::: details Oplossing tonen
```
grep -E "[0-9]+[a-zA-Z]+[0-9]$" regtest.txt
```
:::

## Oefening 3

Gebruik `sed` om:

- Een bestand `regtest_5.txt` te maken van `regtest.txt` waarbij alle cijfers `5` worden vervangen door `vijf`
- Een bestand `regtest_7.txt` te maken van `regtest.txt` waarbij de tekst `seven` telkens wordt vervangen door het getal `7`
- Een bestand `regtest_at.txt` te maken van `regtest.txt` waarbij alle `@`-symbolen worden vervangen door `at`

::: details Oplossing tonen
```
sed 's/5/vijf/g' regtest.txt > regtest_5.txt
```
```
sed 's/seven/7/g' regtest.txt > regtest_7.txt
```
```
sed 's/@/at/g' regtest.txt > regtest_at.txt
```
:::

## Oefening 4

Tel het aantal keer dat het cijfer `5` voorkomt in `regtest.txt`. Zoek in de manpage van `grep` naar een oplossing.

::: details Oplossing tonen
```
grep -o "5" regtest.txt | wc -l
```
:::

## Oefening 5

Zoek in de bash-manpage naar de header met de naam `REDIRECTION` (de tekst begint aan de linkerkant van de pagina). Is deze zoekfunctie hoofdlettergevoelig?

::: details Oplossing tonen
```
man bash
```

*Zoek in less naar de header aan de linkerkant:*

```
/^REDIRECTION
```

*Antwoord:* `man` opent `less` met de opties `-iR`. Hierdoor is de zoekfunctie in less **niet** hoofdlettergevoelig zolang je patroon enkel kleine letters bevat. Zodra je patroon een hoofdletter bevat, wordt de zoekactie wel hoofdlettergevoelig.
:::

## Oefening 6

Toon met reguliere expressies alleen de verborgen bestanden uit je homefolder. Begin met `ls -a` en pipe dit door naar `grep`.

::: details Oplossing tonen
*Inclusief `.` en `..`:*

```
ls -a ~ | grep '^\.'
```

*Zonder `.` en `..`:*

```
ls -a ~ | grep '^\.[^.]'
```
:::

## Oefening 7

Gebruik het commando `ls -la ~` en verander in de uitvoer:

- De referentie `.` naar `. (deze map)`
- De referentie `..` naar `.. (bovenliggende map)`
- Verwijder ook de regel die het totale aantal blokken weergeeft (begint met `total`)

> **Hint:** Als je het `$`-teken aan het einde van een tekenreeks gebruikt, betekent dit dat de regel met die tekenreeks moet eindigen. Om meerdere wijzigingen te doen, gebruik je `sed` meerdere keren.

::: details Oplossing tonen
```
ls -la ~ \
| sed '/^total/d' \
| sed 's/ \.$/ . (deze map)/' \
| sed 's/ \.\.$/ .. (bovenliggende map)/'
```
:::
