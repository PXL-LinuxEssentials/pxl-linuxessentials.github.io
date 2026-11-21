# Overzicht hoofdstuk

Hoofdstuk 06 in één blik: bestanden bekijken, doorbladeren, aanmaken en bewerken.

## Alles tonen: cat en tac
Geef een pad (relatief of absoluut) als argument en de volledige inhoud verschijnt in de terminal.

| Commando | Doet | Voorbeeld |
|---|---|---|
| `cat bestand` | toont de volledige inhoud | `cat /etc/os-release` |
| `tac bestand` | toont de inhoud omgekeerd (onder → boven) | `tac /etc/os-release` |
| `cat f1 f2` | plakt meerdere bestanden na elkaar | `cat count1.txt count2.txt` |

```bash
# relatief en absoluut pad geven hier dezelfde output (cwd = /home/student)
student@linux-ess:~$ cat count1.txt count2.txt
student@linux-ess:~$ cat /home/student/count1.txt /home/student/count2.txt
```

::: warning
`cat` overspoelt de terminal bij grote bestanden. Gebruik dan `less`.
:::

## Begin of einde: head en tail
| Je vraag | Commando |
|---|---|
| De eerste 10 regels? | `head /etc/passwd` |
| De laatste 10 regels? | `tail /etc/passwd` |
| Enkel de eerste 2 regels? | `head -n 2 /etc/passwd` (getal naar keuze) |
| De laatste 5 gebeurtenissen in een log? | `sudo tail -n 5 /var/log/auth.log` |
| Een log live volgen? | `sudo tail -f /var/log/auth.log` (`f` = follow) |

::: tip
`tail -f` blijft draaien en toont nieuwe regels zodra ze erbij komen. Stoppen doe je met {{Ctrl+C}}.
:::

## Bladeren: more versus less
| | more | less |
|---|---|---|
| Richting | enkel omlaag | omhoog én omlaag |
| Per scherm | {{Space}} | {{PgUp}} · {{PgDn}} |
| Per regel | – | {{↑}} · {{↓}} |
| Afsluiten | `q` | `q` |

| Toets in less | Doet |
|---|---|
| `/tekst` | zoeken naar tekst |
| `n` · `N` | volgende · vorige treffer |
| `-i` | hoofdletterongevoelig zoeken |
| `g` · `G` | naar de eerste · laatste regel |

::: info
Manpages openen standaard in `less`: dezelfde toetsen werken dus ook in `man`. `less` sluit je af met `q` ({{Ctrl+C}} werkt niet).
:::

## Aanmaken: echo en >
`echo` drukt zijn argument af. Met `>` stuurt de shell die uitvoer naar een bestand in plaats van naar het scherm (*output redirection*).

| Syntax | Betekenis |
|---|---|
| `echo tekst` | toont tekst op het scherm (quotes maken het argument duidelijker) |
| `echo tekst > f` | schrijft naar `f` en overschrijft de oude inhoud |
| `echo tekst >> f` | voegt toe onderaan `f` |
| `cat a > b` | kopieert de inhoud van `a` naar `b` |

::: warning Twee valkuilen
1. `>` wist wat er al in het bestand stond. Zonder waarschuwing.
2. Bestaat het bestand nog niet? Dan maken `>` en `>>` het aan.
:::

Controleer na met `ls` en `cat demofile`.

## Meerdere regels typen: cat >
**a. Stoppen met {{Ctrl+D}}**

```bash
student@linux-ess:~$ cat > jokes.txt
What is a Linux user's favorite game?
sudo ku
```
Eindig met {{Ctrl+D}} (EOF) op een nieuwe regel.

**b. Eigen eindmarkering**

```bash
student@linux-ess:~$ cat > schooltasks.txt << end
learn 'new commands'
play "minecraft"
end
```

| Methode | Einde van de invoer | Handig voor |
|---|---|---|
| `cat > f` | {{Ctrl+D}} op een nieuwe regel | snel een paar regels |
| `cat > f << end` | het woord `end` alleen op een regel | tekst met `'` en `"`, scripts |

::: tip
De eindmarkering mag elk woord zijn (`end`, `EOF` …), zolang je het onderaan exact zo herhaalt.
:::

## Extra: teksteditor nano
Open een nieuw of bestaand bestand met `nano jokes2.0.txt`. Navigeer met de pijltjes; onderaan staan de sneltoetsen.

| Opslaan en afsluiten | Knippen en plakken | Zoeken |
|---|---|---|
| {{Ctrl+S}} opslaan | {{Shift+pijl}} selecteren | {{Ctrl+W}} zoek ({{Ctrl+Q}} terug) |
| {{Ctrl+O}} opslaan als … | {{Ctrl+K}} knip selectie/regel | {{Alt+W}} volgende treffer |
| {{Ctrl+X}} afsluiten | {{Ctrl+U}} plakken | {{Ctrl+\}} zoek en vervang |

| Toets | Doet |
|---|---|
| {{Ctrl+/}} | naar regel (en kolom) |
| {{Alt+U}} · {{Alt+E}} | ongedaan maken · opnieuw uitvoeren |
| {{Alt+N}} | regelnummers tonen/verbergen |
| {{Alt+S}} | automatische tekstterugloop aan/uit |
| {{Ctrl+Home}} / {{Ctrl+End}} | naar de eerste / laatste regel |

::: tip
Snelst opslaan en afsluiten: {{Ctrl+S}} gevolgd door {{Ctrl+X}}. Nieuwsgierig naar vi/vim? Probeer `vimtutor`.
:::

## Test jezelf
::: details 1. Je opent een groot logbestand met cat en ziet enkel het einde. Wat gebruik je beter?
`less bestand`: daarin kun je omhoog en omlaag scrollen en zoeken met `/`.
:::

::: details 2. Wat is het verschil tussen echo hi > f en echo hi >> f?
`>` overschrijft de inhoud van `f`, `>>` voegt de regel onderaan toe.
:::

::: details 3. Volg de nieuwe aanmeldingen in /var/log/auth.log live.
`sudo tail -f /var/log/auth.log`, stoppen met {{Ctrl+C}}.
:::

::: details 4. Maak een kopie van jokes.txt met enkel cat.
`cat jokes.txt > jokes2.0.txt`
:::
