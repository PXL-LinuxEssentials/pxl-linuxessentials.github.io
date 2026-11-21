# Overzicht hoofdstuk

Hoofdstuk 07 in één blik: hoe de shell je commando leest, bestandsnamen genereert, uitvoer omleidt en commando's aan elkaar koppelt.

## Hoe leest de shell je commando?
De shell (bash, *Bourne Again SHell*) knipt je regel op elke reeks spaties of tabs. Het eerste stuk is het commando, de rest zijn argumenten. De spaties zelf verdwijnen.

```bash
student@linux-ess:~$ echo I like to game ⟵ commando = echo, daarna 4 argumenten
I like to game
```

Met `x="play    games"`:

| Schrijfwijze | Spaties behouden? | `$variabele` vervangen? | Voorbeeld → uitvoer |
|---|---|---|---|
| zonder quotes | nee | ja | `echo a     $x` → `a play games` |
| "dubbele quotes" | ja | ja | `echo "a     $x"` → `a     play    games` |
| 'enkele quotes' | ja | nee, alles letterlijk | `echo 'a     $x'` → `a     $x` |
| `\` escape | enkel het volgende teken | nee, voor dat teken | `echo a\ \ \ \$x` → `a   $x` |

::: tip Vuistregel
Dubbele quotes rond variabelen: `"$x"`. Helemaal letterlijk? Enkele quotes. Elke spatie escapen met `\` werkt, maar is onleesbaar.
:::

## File globbing: bestandsnamen laten genereren
De shell vervangt het patroon door de passende bestandsnamen, nog voor het commando start. Het commando zelf ziet het patroon nooit.

| Teken | Betekenis | Voorbeeld | Past op |
|---|---|---|---|
| `*` | nul, één of meer willekeurige tekens | `file*` | `file`, `file1`, `fileabc` |
| `?` | precies één willekeurig teken | `file?` | `file1`, `filea` (niet `file`, niet `filebc`) |
| `[abc]` | één teken uit de set | `file[12]` | `file1`, `file2` |
| `[a-z]` `[0-9]` | één teken uit het bereik | `file[0-9]` | `file1`, `file2`, `file3` |
| `[!a-z]` | één teken niet uit de set (`[^a-z]` werkt ook) | `file[!a-z]*` | `file1`, `file2`, `file3` |

| Je vraag | Patroon |
|---|---|
| Begint met F? | `F*` |
| Eindigt op .conf? | `*.conf` |
| Bevat een a? | `*a*` |
| Begint met een hoofdletter? | `[A-Z]*` |
| Exact vier tekens? | `????` |
| Eindigt op een cijfer? | `*[0-9]` |

::: warning Hoofdlettergevoelig
Globbing is hoofdlettergevoelig: `file*` vindt `File4` niet. Past er niets, dan geeft bash het patroon ongewijzigd door: `ls: cannot access 'File??'`.
:::

**Globbing tegenhouden**

```bash
student@linux-ess:~$ echo **** TITLE ****     ⟵ ✗ de shell vervangt **** door alle bestandsnamen
student@linux-ess:~$ echo "**** TITLE ****"   ⟵ ✓
student@linux-ess:~$ echo '**** TITLE ****'   ⟵ ✓
student@linux-ess:~$ rm file*                 ⟵ ✗ verwijdert file, file1, file2, … én 'file*'
student@linux-ess:~$ rm 'file*'               ⟵ ✓ enkel het bestand met de naam file*
```

::: tip Eerst kijken, dan verwijderen
Test een patroon eerst met `echo file*`: zo zie je exact wat de shell ervan maakt, voor je `rm` gebruikt.
:::

## Aliassen: eigen korte commando's
| Commando | Doet |
|---|---|
| `alias show='ls -lah'` | maakt de alias `show` |
| `alias rm='rm -i'` | extra veiligheid: `rm` vraagt eerst bevestiging |
| `alias` | toont alle aliassen · `alias ls` toont er één |
| `unalias rm` | verwijdert de alias |
| `\ls` | voert het échte commando uit, zonder alias |
| `type -a ls` | toont wat de shell zal uitvoeren: alias, builtin of bestand |

**Alias bewaren:** een alias geldt enkel in de huidige shell. Bewaar hem in `~/.bash_aliases` (Ubuntu) of `~/.bashrc` (RHEL) en laad met `source ~/.bash_aliases` of open een nieuwe terminal.

**Zoekvolgorde van de shell:** 1 alias → 2 functie → 3 builtin (`cd`, `echo`) → 4 bestand in `$PATH` (`/usr/bin/ls`)

## I/O-redirection: uitvoer omleiden
**0 · stdin** (invoer, toetsenbord) → **commando** → **1 · stdout** (normale uitvoer, scherm) en **2 · stderr** (foutmeldingen, scherm)

| Syntax | Betekenis |
|---|---|
| `cmd > bestand` | stdout naar bestand, overschrijft (= `1>`) |
| `cmd >> bestand` | stdout naar bestand, voegt toe |
| `cmd 2> /dev/null` | foutmeldingen weggooien (het "zwarte gat") |
| `cmd > out.txt 2> err.txt` | stdout en stderr elk naar een eigen bestand |
| `cmd &> bestand` | stdout én stderr naar hetzelfde bestand · `&>>` voegt toe |
| `cmd > bestand 2>&1` | idem, klassieke schrijfwijze: stderr gaat waar stdout naartoe gaat |
| `cmd < bestand` | stdin uit een bestand in plaats van het toetsenbord |

::: warning > maakt het bestand eerst leeg
`>` maakt het bestand leeg, nog voor het commando start: `sort data.txt > data.txt` laat een leeg bestand achter.
:::

::: warning De volgorde telt
`cmd > f 2>&1` ✓ beide naar het bestand · `cmd 2>&1 > f` ✗ stderr blijft op het scherm.
:::

## Control operators: commando's koppelen
Elk commando eindigt met een exit-code: 0 = gelukt, iets anders = mislukt. Bekijk ze met `echo $?`.

| Operator | Tweede commando loopt… | Voorbeeld |
|---|---|---|
| `a ; b` | altijd, na elkaar | `echo hello ; pwd` |
| `a && b` | enkel als a gelukt is | `mkdir backup && cd backup` |
| <code>a &#124;&#124; b</code> | enkel als a mislukt is | <code>cd /data &#124;&#124; echo "geen map"</code> |
| <code>a && b &#124;&#124; c</code> | b als a lukt, anders c | zie hieronder |

```bash
student@linux-ess:~$ zecho first ; echo $?     ⟵ 127: commando niet gevonden
student@linux-ess:~$ echo first ; echo $?      ⟵ 0: gelukt
student@linux-ess:~$ rm testfile 2> /dev/null && echo "file deleted" || echo "failed to delete"
```

::: warning Geen echte if-then-else
`a && b || c` is geen echte if-then-else: `c` loopt ook als `a` lukt maar `b` faalt. Voor echte logica: `if … then … else … fi`.
:::

## Test jezelf
::: details 1. Verschil in uitvoer tussen echo "$HOME" en echo '$HOME'?
`"$HOME"` toont je homemap, bv. `/home/student`. `'$HOME'` toont letterlijk `$HOME`.
:::

::: details 2. Hoe verwijder je enkel het bestand met de naam file*?
`rm 'file*'` of `rm file\*`. Zonder quotes vervangt de shell `file*` door alle bestanden die met `file` beginnen.
:::

::: details 3. ls toont kleuren, \ls niet. Waarom?
`ls` is een alias voor `ls --color=auto`. Met `\ls` sla je de alias over. Controleer met `type ls`.
:::

::: details 4. Waarom komen de fouten van find / 2>&1 > out.txt toch op je scherm?
Redirections gaan van links naar rechts: `2>&1` wijst stderr naar het scherm (waar stdout op dat moment heen gaat). Juist: `find / > out.txt 2>&1` of `find / &> out.txt`.
:::

::: details 5. Wat doet mkdir /root/test && echo gelukt || echo mislukt als gewone gebruiker?
`mkdir` faalt (geen rechten), dus `echo gelukt` wordt overgeslagen en je ziet `mislukt`, plus de foutmelding van `mkdir` tenzij je `2> /dev/null` toevoegt.
:::
