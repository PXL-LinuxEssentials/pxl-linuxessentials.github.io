# Overzicht hoofdstuk

Hoofdstuk 08 in één blik: tekst filteren, structureren en transformeren met pipes. Eerst de basis die het vaakst fout loopt: globbing of regex, en de vierkante haken.

## Globbing of regex?
Dezelfde tekens, een andere betekenis. Vraag je altijd af: wie leest dit patroon, de shell of het commando?

| | File globbing | Reguliere expressies |
|---|---|---|
| Wie | de shell, vóór het commando start | het commando zelf |
| Werkt op | bestandsnamen | tekst / inhoud |
| Gebruikt door | `ls cp mv rm cat` …, `find -name "*.conf"` | `grep`, `sed`, `rename`, `/` zoeken in `less` en `man` |

| Teken | Globbing | Regex |
|---|---|---|
| `*` | 0+ willekeurige tekens | 0+ keer het vorige teken |
| `+` | gewoon een plusteken | 1+ keer het vorige teken (met `-E`, anders `\+`) |
| `?` | precies 1 willekeurig teken | vorige teken optioneel (0 of 1, met `-E`, anders `\?`) |
| `.` | gewoon een punt | 1 willekeurig teken |
| `^` | geen globbing-teken | begin van de regel |
| `$` | geen globbing-teken | einde van de regel |
| `[abc]` | erin: 1 teken dat a, b of c is | erin: 1 teken dat a, b of c is |
| `[!a]` / `[^a]` | eruit: `[!a]` 1 teken dat géén a is | eruit: `[^a]` 1 teken dat géén a is |
| "eindigt op .txt" | `ls *.txt` | `grep "\.txt$"` |

::: warning Regex altijd tussen aanhalingstekens
Zonder quotes vervangt de shell `p*` in `grep p* bestand` eerst door bestandsnamen.
:::

## Vierkante haken: tekens erin [ ] en eruit [^ ]
Alles tussen `[ ]` staat voor precies één teken. Je kiest welke tekens mogen (erin) of welke niet mogen (eruit).

| Patroon | Betekent: één teken dat … | Voorbeeld met regexlist.txt |
|---|---|---|
| `[abc]` | erin: a, b of c is | `grep -i "^[cms]"` → Charlotte, Max, Stan … |
| `[io]` | erin: i of o is | `grep "T[io]m"` → Tim, Tom |
| `[0-9]` | erin: een cijfer is (bereik 0 t/m 9) | `grep "^[0-9]"` → 128, 32, 192.168.1.19 … |
| `[a-z]` · `[A-Z]` | erin: een kleine letter · een hoofdletter is | `grep "^[a-z]"` → john.doe@pxl.be, pxl … |
| `[a-zA-Z]` | erin: een letter is, klein of hoofd (bereiken combineren) | `grep "^[a-zA-Z]"` → alle namen, pxl … (geen getallen) |
| `[a-zA-Z0-9]` | erin: een letter of cijfer is | |
| `[^l]` | eruit: géén l is | `grep "px[^l]"` → pxxl, pxe … (niet pxl) |
| `[^0-9]` | eruit: géén cijfer is | `grep "[^0-9]$"` → eindigt niet op een cijfer |
| `[^a-zA-Z0-9:/.]` | eruit: géén letter, cijfer, `:`, `/` of `.` is | vindt regels met een spatie of `@` |

* **De `^` hangt af van waar hij staat.** Vóór de haken = begin van de regel: `^[0-9]` de regel begint met een cijfer. Binnen de haken, als eerste teken = *niet* (eruit): `[^0-9]` één teken dat géén cijfer is.
* **Binnen `[ ]` gewoon:** een punt in `[.]` is een échte punt. Buiten de haken schrijf je `\.`.
* **Meer dan één teken?** Zet er een aantal achter: `[a-z]*` (altijd), `[0-9]+`, `[0-9]{1,3}` (met `-E`).

**Waar moet dat ene teken staan? Combineer [ ] met ^ en $.** Zonder `^` of `$` mag het teken overal in de regel staan. Met `^` kijkt grep alleen naar het eerste teken, met `$` alleen naar het laatste.

| Patroon | Voorbeeld | Uitleg |
|---|---|---|
| `^[aeiou]` | Emma | `^` ervoor: het EERSTE teken moet erin zitten (a, e, i, o of u) |
| `[aeiou]$` | Emma | `$` erachter: het LAATSTE teken moet erin zitten |
| `^[^aeiou]` | Max | eerste `^` = begin, tweede `^` = eruit: eerste teken géén klinker |

| Patroon (met `grep -i`) | Lees als | Resultaat in regexlist.txt |
|---|---|---|
| `[aeiou]` | ergens in de regel een klinker | 25 van de 39 regels, bv. Max, Stan … |
| `^[aeiou]` | erin: het eerste teken is een klinker | Emma, Ian, Ellen |
| `[aeiou]$` | erin: het laatste teken is een klinker | Charlotte, Emma, Sara, Nora, pxe … |
| `^[aeiou].*[aeiou]$` | begint én eindigt met een klinker | Emma |
| `^[^aeiou]` | eruit: het eerste teken is géén klinker | Max, John, 128, pxl … (niet Emma, Ian, Ellen) |
| `[^aeiou]$` | eruit: het laatste teken is géén klinker | Max, Ian, Tim, 128 … |

::: warning
`[a-z]` is hoofdlettergevoelig. Wil je beide, gebruik `[a-zA-Z]` of `grep -i`. En `[abc]` zoekt één teken, niet het woord "abc".
:::

## De lopende band: pipes
Elk commando doet één ding. Met `|` gaat de uitvoer (stdout) van het ene naar de invoer (stdin) van het volgende.

```bash
student@linux-ess:~$ cat auth.log | grep Failed | cut -d' ' -f8 | sort | uniq
```
lees → filter → knip → orden → ontdubbel

| Syntax | Betekenis |
|---|---|
| <code>a &#124; b</code> | stdout van a gaat naar stdin van b |
| <code>a &#124;& b</code> | stdout én stderr gaan naar b (filters zien anders geen foutmeldingen) |
| `tee bestand` | schrijft naar een bestand en laat de stroom doorlopen |
| `tee -a bestand` | voegt toe in plaats van te overschrijven |
| <code>&#124; sudo tee /pad</code> | schrijft waar je geen rechten hebt. `sudo cmd > /pad` faalt, want de redirect doet je eigen shell. |

## Selecteren: welke regels? grep
| Je vraag | Commando |
|---|---|
| Regels met "Failed"? | `grep Failed auth.log` |
| Hoofdletters maken niet uit? | `grep -i failed auth.log` |
| Regels zonder "Failed"? | `grep -v Failed auth.log` |
| Context erbij? | `-A n` erna · `-B n` ervoor · `-C n` rondom |
| Enkel het volledige woord? | `grep -w test` (niet "tested") |
| A én B? | <code>grep A &#124; grep B</code> of `grep "A.*B"` |
| A of B? | <code>grep -E "A&#124;B"</code> · `grep -e A -e B` · <code>grep "A\&#124;B"</code> |
| Ook in foutmeldingen zoeken? | <code>find /sys -iname "*kernel*" &#124;& grep debug</code> |

::: info
`grep` is standaard hoofdlettergevoelig, en het patroon mag overal in de regel staan.
:::

## Vorm geven: knippen, sorteren, tellen
| Commando | Doet | Voorbeeld |
|---|---|---|
| `cut -d'x' -fN` | splitst op teken x, toont kolom N | `cut -d':' -f1,6 /etc/passwd` |
| `sort` | zet regels op volgorde | <code>… &#124; sort</code> |
| `uniq` | verwijdert dubbele opeenvolgende regels | <code>… &#124; sort &#124; uniq</code> |
| `wc` | telt regels · woorden · bytes | `-l -w -c -m` |

::: warning Altijd sort vóór uniq
`uniq` vergelijkt alleen buren.
:::

Bouw een pipeline stap per stap op en bekijk telkens de uitvoer:

```bash
student@linux-ess:~$ grep Failed auth.log
student@linux-ess:~$ grep Failed auth.log | cut -d' ' -f8
student@linux-ess:~$ grep Failed auth.log | cut -d' ' -f8 | sort | uniq
```

## Transformeren: tr versus sed
| | tr | sed |
|---|---|---|
| Werkt op | losse karakters | patronen (woorden, regex) |
| Vervangen | `tr 'a-z' 'A-Z'` | `sed 's/Failed/Incorrect/'` |
| Verwijderen | `tr -d ':'` (het teken) | `sed '/Failed/d'` (de hele regel) |
| Extra | `-s` herhaalde tekens worden één · `'\n'` newline | `g` alle treffers · `i` hoofdletterongevoelig · `-E` extended regex · `-i` bestand zelf aanpassen |

::: warning Drie valkuilen
1. Zonder `g` vervangt `sed` enkel de eerste treffer per regel.
2. Zonder `-i` blijft het bestand zelf ongewijzigd.
3. Slashes in je patroon botsen met de `/` van `s/…/…/`. Zie hieronder.
:::

**Ander scheidingsteken.** `sed` neemt het teken direct na de `s` als scheidingsteken tussen zoekpatroon en vervanging. Bevat je patroon zelf een `/` (zoals `://`), kies dan een ander teken dat er niet in voorkomt: `_` `#` `|`

```bash
student@linux-ess:~$ sed -E 's/https?://.*/url masked/'       ⟵ FOUT: sed ziet de / in :// als einde van het zoekpatroon
student@linux-ess:~$ sed -E 's/https?:\/\/.*/url masked/'     ⟵ werkt, maar elke / escapen leest moeilijk
student@linux-ess:~$ sed -E 's_https?://.*_url masked_'       ⟵ beter: _ als scheidingsteken
```

## Regular expressions: zoeken op vorm
| Wat | Betekenis |
|---|---|
| **a · Welk karakter?** | `.` één willekeurig teken · `[abc]` `[0-9]` erin: één uit de set · `[^0-9]` eruit: alles behalve · `\.` een échte punt |
| **b · Hoeveel keer?** (geldt voor het teken ervóór) | `*` 0+ · `+` 1+ · `?` 0 of 1 · `{3}` precies 3 · `{1,3}` 1 tot 3 · `{2,}` 2+ |
| **c · Waar?** | `^` begin · `$` einde van de regel |
| **d · Groeperen** | `( )` groep: `pxe( boot)?` · <code>&#124;</code> of: <code>^M&#124;n$</code> |

| Regex | Lees als |
|---|---|
| `e$` | eindigt op een e → Charlotte, pxe, http://www.pxl.be … |
| `^E.*a$` | begint met E én eindigt op a → Emma |
| `px*l` | p, nul of meer x, dan l → pl, pxl, pxxl … |
| `px+l` (met `-E`) | p, één of meer x, dan l → pxl, pxxl … (niet pl) |
| `t.m` (met `-i`) | t, één willekeurig teken, m → Tim, Tom |
| `^...\.` | begint met 3 willekeurige tekens, dan een échte punt |
| `https?://` | http, optionele s, dan :// |
| `^([0-9]{1,3}\.){3}[0-9]{1,3}$` | IPv4-formaat (geen validatie van 0–255) |
| `^.+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}` | e-mail-formaat |

::: warning Alleen met -E
<code>+ ? { } &#124; ( )</code> werken alleen met `-E`. Zonder `-E` escape je ze: `\+ \? \{ \} \| \( \)`.
:::

## Test jezelf
::: details 1. Wat betekent * in ls *.txt, en wat in grep "px*l"?
Globbing: nul of meer willekeurige tekens. Regex: nul of meer keer het vorige teken (`x`).
:::

::: details 2. Wat is het verschil tussen ^[0-9] en [^0-9]?
`^[0-9]`: de regel begint met een cijfer. `[^0-9]` (eruit): ergens staat een teken dat géén cijfer is.
:::

::: details 3. Zoek de regels die beginnen met een C, M of S, hoofdletters maken niet uit.
`grep -i "^[cms]" regexlist.txt`
:::

::: details 4. Waarom geeft grep "p*" álle regels terug?
`p*` betekent "nul of meer p's", en elke regel bevat nul p's.
:::

::: details 5. Toon de gebruikers die minstens één keer succesvol inlogden.
`grep Accepted auth.log | cut -d' ' -f8 | sort | uniq`
:::

::: details 6. Verschil tussen tr -d 'x' en sed '/x/d'?
`tr` verwijdert het teken `x`, `sed` verwijdert de hele regel waarin `x` staat.
:::
