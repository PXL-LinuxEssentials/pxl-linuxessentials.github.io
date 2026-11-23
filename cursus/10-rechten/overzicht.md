# Overzicht hoofdstuk

Hoofdstuk 10 in één blik: wie mag wat met een bestand of map, hoe wijzig je dat, en hoe laat je een groep veilig samenwerken. Eerst de basis (rwx en octaal), dan chmod en chown, de standaardrechten (umask), de speciale bits en tot slot ACL's.

## Lezen, schrijven, uitvoeren
`ls -l` toont per bestand drie sets van drie rechten, gevolgd door de eigenaar en de groep.

```output
 -   rwx   rw-   r--    1  student  it
 │    │     │     │        │        │
 │    │     │     │        │        └ groepseigenaar (2e naam)
 │    │     │     │        └ userowner (1e naam)
 │    │     │     └ others: lezen
 │    │     └ groep: lezen en schrijven
 │    └ eigenaar: lezen, schrijven, uitvoeren
 └ type: - bestand · d map · l link · b/c apparaat · p pipe · s socket
```

| Recht | Op een bestand | Op een map | Octaal |
|---|---|---|---|
| `r` read | inhoud lezen | inhoud tonen (`ls`) | 4 |
| `w` write | inhoud wijzigen | bestanden aanmaken, hernoemen, verwijderen | 2 |
| `x` execute | uitvoeren als programma of script | erin gaan (`cd`) en bestanden bereiken | 1 |

* **Octaal rekenen:** tel de waarden op per set. `rwx` = 4+2+1 = **7** · `rw-` = **6** · `r--` = **4**. Dus `rwxrw-r--` = **764**.
* **Nieuw bestand:** je wordt de eigenaar, de groep is je **primaire groep**.
* **Mappen:** zonder `x` kan je er weinig mee. Gangbaar: `rwx` (alles), `r-x` (alleen lezen), `---` (geen toegang).

| Octaal | rwx | Betekenis |
|---|---|---|
| 0 | `---` | niets |
| 4 | `r--` | lezen |
| 5 | `r-x` | lezen en uitvoeren |
| 6 | `rw-` | lezen en schrijven |
| 7 | `rwx` | alles |

::: warning Geef niet zomaar rechten
Rechten zijn je eerste verdedigingslinie. Vraag je bij een `Permission denied` eerst af waarom iemand toegang nodig heeft, in plaats van meteen `777` te geven.
:::

## Rechten wijzigen met chmod
Twee manieren, afhankelijk van wat je wil doen.

| Manier | Voorbeeld | Wanneer |
|---|---|---|
| Letters | `chmod a+x test` · `chmod g-w test` · `chmod go-rx test` | snelle aanpassing van een of twee rechten |
| Octaal | `chmod 600 config` · `chmod 744 config` | alles in één keer herschrijven |

* Wie: `u` (user) · `g` (group) · `o` (others) · `a` (alle drie).
* Wat: `+` toevoegen · `-` weghalen · `=` exact instellen.

## Eigenaar wijzigen
Hiervoor heb je `sudo` nodig. `-R` werkt recursief.

| Commando | Doet |
|---|---|
| `sudo chgrp -R it course/` | groepseigenaar wijzigen |
| `sudo chown teacher rights.jpg` | enkel de eigenaar wijzigen |
| `sudo chown teacher:root config folder` | eigenaar én groep wijzigen |
| `sudo chown :it config` | enkel de groep wijzigen |

## Standaardrechten: umask
De umask bepaalt welke rechten je **niet** krijgt bij nieuwe bestanden en mappen.

| | Maximum | Met umask `0002` |
|---|---|---|
| Bestand | 666 (nooit `x`, afgedwongen door de kernel) | 664 `rw-rw-r--` |
| Map | 777 | 775 `rwxrwxr-x` |

* **Rekenregel:** trek de umask af van 777 (map). Bij een bestand laat je de `x`-bits altijd weg.
* `umask` toont de waarde · `umask 027` stelt in · `umask -S` toont in letters · `umask u=rwx,g=rx,o=` stelt in met letters.
* **Enkel voor deze sessie.** Permanent: zet `umask 027` (of een andere waarde) in `~/.profile`.
* **Systeembreed:** de PAM-module `pam_umask` stelt de umask in bij het inloggen. De startwaarde `022` wordt geërfd van het proces dat je sessie start. Door `USERGROUPS_ENAB yes` in `/etc/login.defs` krijgt een gewone gebruiker met een eigen primaire groep daarna `002` (groepsbits = eigenaarbits). Root en `sudo` houden `022`.

| Umask | Bestand | Map | Gebruik |
|---|---|---|---|
| `002` | `rw-rw-r--` | `rwxrwxr-x` | standaard voor `student` |
| `022` | `rw-r--r--` | `rwxr-xr-x` | standaard voor root |
| `027` | `rw-r-----` | `rwxr-x---` | anderen krijgen niets |
| `077` | `rw-------` | `rwx------` | alleen jij |

::: warning Standaard leesbaar voor anderen
Nieuwe bestanden zijn standaard leesbaar voor alle gebruikers. Pas de rechten aan voor je er gevoelige gegevens in bewaart.
:::

## Samenwerken in een gedeelde map
Het scenario: Liam en Jacob moeten samen bestanden in `/shares/ict` kunnen bewerken.

**Stappen**
1. Geef elke gebruiker een **eigen primaire groep** (`usermod -g liam liam`). Een gedeelde primaire groep opent ook elkaars homefolders.
2. Maak een groep voor de samenwerking (`groupadd ict`) en voeg beide gebruikers toe met `usermod -aG ict liam`.
3. Maak de map, geef ze aan de groep en geef de groep schrijfrechten: `sudo mkdir -p /shares/ict` · `sudo chgrp ict /shares/ict` · `sudo chmod g+w /shares/ict`.
4. Zet de **setgid-bit** op de map: `sudo chmod g+s /shares/ict`.

Zonder setgid krijgt een bestand van Jacob zijn primaire groep (`jacob`), en kan Liam het niet wijzigen. Met setgid krijgt alles in de map de groep `ict`, en nieuwe submappen erven de setgid-bit.

## Speciale bits
| Bit | Zet je met | Op bestand | Op map | In `ls -l` |
|---|---|---|---|---|
| **setuid** | `chmod u+s` · 4xxx | uitvoeren als de **eigenaar** | geen effect | `s` bij user |
| **setgid** | `chmod g+s` · 2xxx | uitvoeren als de **groep** | nieuwe bestanden erven de groep | `s` bij group |
| **sticky** | `chmod o+t` · 1xxx | geen effect | enkel eigen bestanden verwijderen of hernoemen | `t` bij others |

* Kleine `s` of `t`: de `x` eronder staat aan. **Hoofdletter** `S` of `T`: de `x` staat uit.
* **Combineren:** tel de waarden op en zet het cijfer vooraan. setgid + sticky = 2+1 = 3, dus `chmod 3770`.
* **Verwijderen:** `chmod 0777` haalt alleen de sticky-bit weg. Alle speciale bits weg: `chmod 00775`, met een extra nul.
* **Voorbeelden:** `/tmp` is `drwxrwxrwt` (sticky). `/bin/passwd` is `-rwsr-xr-x` (setuid, 4755). Daarom mag een gewone gebruiker zijn wachtwoord wijzigen in `/etc/shadow`.

::: info Sticky en gedeelde bestanden
Met de sticky-bit kan Liam de bestanden van Jacob niet meer verwijderen. Wil je ook dat hij ze niet kan overschrijven, dan helpt `sudo sysctl fs.protected_regular=1`. Permanent maak je dat in `/usr/lib/sysctl.d/99-protect-links.conf`.
:::

::: danger Setuid
Setuid op een programma geeft het de rechten van de eigenaar. Dat is een ernstig beveiligingsrisico en bijna altijd een slecht idee.
:::

## ACL's: rechten per gebruiker of groep
ACL's laten je een bestand delen met één gebruiker of groep, zonder de gewone eigenaar of groep te wijzigen.

| Commando | Doet |
|---|---|
| `sudo apt install acl` | pakket installeren (op Ubuntu staat ACL-ondersteuning standaard aan) |
| `getfacl memo` | ACL's tonen |
| `setfacl -m u:teacher:rw memo` | ACL voor een gebruiker toevoegen of wijzigen |
| `setfacl -m g:it:rw memo` | ACL voor een groep toevoegen of wijzigen |
| `setfacl -m m:r memo` | de **mask** (maximum aan rechten) wijzigen |
| `setfacl -x g:it memo` | één ACL verwijderen |
| `setfacl -b memo` | alle ACL's verwijderen |
| `setfacl -m d:g:it:rwx memos` | **default**-ACL op een map, die nieuwe bestanden en mappen erven (ook `-d`) |

* **Herkennen:** `ls -l` toont een **`+`** achter de rechten.
* **Wie mag wijzigen:** enkel de eigenaar. In de ACL staan geeft je dat recht niet.
* **ACL's gaan voor** op de gewone rechten, behalve voor de rechten van de eigenaar. Als `user::r--` is, blijft het bij lezen, ook met een ACL `u:student:rw`.
* **Gebruiker-ACL wint van groep-ACL:** zit iemand in een gebruiker-ACL én in een groep-ACL, dan tellen alleen de gebruikersrechten.
* **Groepen tellen op:** zit je in twee groepen met `r--` en `rwx`, dan heb je `rwx`.
* **Mask:** het maximum voor alle ACL's en voor de groepsrechten. Zet je de mask op `r--`, dan toont `getfacl` bij de rest `#effective:r--`. Na een wijziging van een ACL wordt de mask automatisch bijgewerkt.
* **Mappen:** de gebruiker of groep heeft ook `x` op de map zelf nodig, anders komt hij er niet in. Een default-ACL werkt dus alleen als die rechten er zijn.

## Valkuilen
::: warning De vaakst gemaakte fouten
1. **`chmod -R 777`** als snelle oplossing. Je opent alles voor iedereen.
2. **Geen `x` op een map:** bestanden erin zijn onbereikbaar, ook al zijn ze leesbaar.
3. **Setgid vergeten** op een gedeelde map: bestanden krijgen de primaire groep van de maker.
4. **Sticky-bit zonder `fs.protected_regular=1`:** verwijderen kan niet meer, maar overschrijven wel.
5. **umask in de terminal ingesteld:** is weg na het afsluiten. Zet het in `~/.profile`.
6. **Een ACL die niet werkt:** controleer de mask en of de gebruiker ook `x` heeft op de map.
:::

## Test jezelf
::: details 1. Wat betekent -rwxr-x--- en wat is dat in octaal?
Eigenaar: lezen, schrijven, uitvoeren. Groep: lezen en uitvoeren. Anderen: niets. Octaal 750.
:::

::: details 2. Welke rechten krijgt een nieuw bestand bij umask 027?
Een bestand: 777 − 027 = 750, zonder `x` dus 640 (`rw-r-----`). Een map krijgt 750 (`rwxr-x---`).
:::

::: details 3. Waarom krijgen nieuwe bestanden nooit uitvoerrechten?
De kernel zet `x` nooit zelf op nieuwe bestanden (maximum 666), uit veiligheid. Je geeft het bewust met `chmod`.
:::

::: details 4. Wat is het verschil tussen chgrp en chown?
`chgrp` wijzigt enkel de groep. `chown` wijzigt de eigenaar en/of de groep, bv. `chown teacher:it bestand`.
:::

::: details 5. Wat doet setgid op een map?
Nieuwe bestanden en mappen erven de groep van die map. Nieuwe submappen krijgen zelf ook de setgid-bit.
:::

::: details 6. Waarvoor dient de sticky-bit, en waar zie je hem al?
Gebruikers kunnen in die map alleen hun eigen bestanden verwijderen of hernoemen. Je ziet hem op `/tmp` (`drwxrwxrwt`).
:::

::: details 7. Met welk commando zet je setgid en sticky tegelijk, met rechten 770?
`chmod 3770 map` (2 + 1 = 3). Is `x` voor others uit, dan zie je `drwxrws--T`.
:::

::: details 8. Waarom kan een gewone gebruiker zijn wachtwoord wijzigen, terwijl hij /etc/shadow niet kan lezen?
`/bin/passwd` heeft de setuid-bit (4755) en draait daardoor als root, de eigenaar.
:::

::: details 9. Hoe geef je gebruiker teacher lees- en schrijfrechten op memo, zonder iets aan eigenaar of groep te wijzigen?
`setfacl -m u:teacher:rw memo`. Controleren met `getfacl memo`. Je ziet ook een `+` in `ls -l`.
:::

::: details 10. Je zet de mask op r--. Wat gebeurt er met de ACL u:teacher:rw?
De effectieve rechten van teacher worden `r--`. De mask is een maximum voor alle ACL's.
:::
