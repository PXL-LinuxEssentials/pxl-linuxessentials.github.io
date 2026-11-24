# Overzicht hoofdstuk

Hoofdstuk 09 in één blik: gebruikers, wachtwoorden, van gebruiker wisselen en groepen beheren. Eerst wat de bestanden zeggen, dan de commando's, en de valkuilen die het vaakst fout lopen.

## Wie ben ik, en waar staat dat?
Alle configuratie staat in tekstbestanden. Gebruikers en groepen zijn daarop geen uitzondering.

| Commando | Toont |
|---|---|
| `whoami` | de huidige gebruiker |
| `who` · `users` · `w` | wie er is ingelogd (elk commando geeft een andere uitvoer) |
| `id [gebruiker]` | uid, gid en alle groepen |
| `groups [gebruiker]` | enkel de groepen |

| Bestand | Bevat |
|---|---|
| `/etc/passwd` | gebruikersaccounts, leesbaar voor iedereen (`man 5 passwd`) |
| `/etc/shadow` | geëncrypte wachtwoorden, enkel met sudo te lezen |
| `/etc/group` | groepen en hun leden |
| `/etc/default/useradd` | standaardwaarden voor `useradd` |
| `/etc/skel` | sjabloon: inhoud wordt gekopieerd naar elke nieuwe homefolder |

Een regel in `/etc/passwd`: zeven velden gescheiden door `:`

```output
teacher:x:1001:1001:Teacher Account:/home/teacher:/bin/bash
naam : wachtwoord in shadow : uid : gid (primair) : commentaar : homefolder : shell
```

::: info Uid's
De eerste regel is root met uid 0. Gewone gebruikers beginnen bij uid 1000 (student = 1000).
:::

## Gebruikers aanmaken, wijzigen, verwijderen
| Commando | Doet |
|---|---|
| `sudo useradd -m -d /home/teacher -c "Teacher Account" teacher` | `-m` maakt de homefolder aan · `-d` pad (optioneel, standaard `/home/naam`) · `-c` commentaar |
| `sudo usermod -c "Tekst" x` | commentaar wijzigen |
| `sudo usermod -s /bin/bash x` | shell wijzigen |
| `sudo userdel -r x` | gebruiker verwijderen, `-r` verwijdert ook de homefolder |
| `useradd -D` | standaardwaarden tonen |
| `sudo useradd -D --shell /bin/bash` | standaard shell voor nieuwe gebruikers wijzigen (aanrader, anders `/bin/sh`) |

* **Profielbestanden uit `/etc/skel`:** `.bashrc` bij elke nieuwe bash-shell · `.bash_logout` bij uitloggen · `.profile` bij inloggen.
* **Geen login toestaan:** zet de shell op `/sbin/nologin` (toont een beleefd bericht) of `/bin/false` (sluit stil af).

::: warning Altijd sudo
`useradd` en `usermod` beïnvloeden het hele systeem: altijd met `sudo`.
:::

## Wachtwoorden en van gebruiker wisselen
| Commando | Doet |
|---|---|
| `passwd` | je eigen wachtwoord wijzigen (zonder sudo) |
| `sudo passwd teacher` | wachtwoord van een andere gebruiker instellen |
| `sudo tail -1 /etc/shadow` | geëncrypte wachtwoorden bekijken. Zonder sudo: Permission denied |

::: warning sudo passwd
`sudo passwd` zonder gebruikersnaam wijzigt het wachtwoord van root, niet van jezelf. Een te kort of te simpel wachtwoord wordt geweigerd.
:::

Bij `su` en `su -` is altijd het wachtwoord van de doelgebruiker nodig.

| Wisselen | Resultaat |
|---|---|
| `su - teacher` | profiel geladen · je zit in `/home/teacher` |
| `su teacher` | rechten van teacher, maar profiel niet geladen · je blijft in de huidige map |
| `sudo su - teacher` | teacher worden zonder diens wachtwoord. Je moet lid zijn van de groep `sudo`, jouw eigen wachtwoord volstaat |
| `sudo su - root` | root worden zonder het root-wachtwoord (in `/root`). Ook hier moet je lid zijn van de groep `sudo` |
| `exit` · `logout` | terug naar de vorige gebruiker / uitloggen |

::: warning Het koppelteken
Het koppelteken in `su -` maakt het verschil. Wees voorzichtig als root: die heeft toegang tot alle bestanden en services.
:::

## Groepen beheren
```output
adm:x:4:syslog,student      # naam : x : gid : leden (gescheiden door komma's)
```

| Commando | Doet |
|---|---|
| `sudo groupadd it` | groep aanmaken |
| `sudo groupmod -n ict it` | groep `it` hernoemen naar `ict` |
| `sudo groupdel it` | groep verwijderen |
| `sudo usermod -a -G it teacher` | teacher toevoegen aan extra groep `it` (grote `G`) |
| `sudo usermod -g it teacher` | de primaire groep wijzigen (kleine `g`) |

::: danger Vergeet -a niet
Vergeet je `-a` bij `usermod -G`, dan vervangt dit alle extra groepen. Was de gebruiker de enige in de groep `sudo`, dan is er geen beheerder meer.
:::

**Een gebruiker uit een extra groep halen, vier manieren:**

| Manier | Opmerking |
|---|---|
| `sudo usermod -r -G it x` | `-r` = *remove*: haalt x uit de groep it |
| `sudo deluser x it` | enkel op Debian-gebaseerde distributies (zoals Ubuntu) |
| `sudo usermod -G g1,g2 x` | zonder `-a`: geef alle extra groepen op die moeten blijven (gescheiden door komma, zonder spaties). Wat je weglaat, verdwijnt. Bv. x zit in sudo, it en ict en moet uit it: `-G sudo,ict` |
| `/etc/group` bewerken | verwijder de naam uit de ledenlijst van de groep |

## Primaire groep en opnieuw inloggen
Een wijziging in groepslidmaatschap merkt de gebruiker pas na opnieuw inloggen. Het commando `id student` toont de nieuwe situatie, maar `id` en `groups` zonder naam tonen wat de sessie nu gebruikt.

::: warning Drie valkuilen
1. Nieuwe bestanden krijgen de oude primaire groep zolang je niet opnieuw bent ingelogd.
2. `usermod -g` past zelf de groep aan van bestanden in de homefolder. Bestanden elders niet (zie hoofdstuk rechten).
3. De primaire groep staat in `/etc/passwd` (4e veld) en wordt de groep van nieuwe bestanden.
:::

Terug naar de oude primaire groep: `sudo usermod -g student student` schrijft de nieuwe gid in het 4e veld van `/etc/passwd`.

```output
voor:  student:x:1000:1001:...:/home/student:/bin/bash     # 1001 = it
na:    student:x:1000:1000:...:/home/student:/bin/bash     # 1000 = student
```

```bash
student@linux-ess:~$ sudo usermod -g it student
student@linux-ess:~$ id student        ⟵ gid=1999(it): nieuwe situatie
student@linux-ess:~$ id                ⟵ gid=1000(student): de sessie weet het nog niet
student@linux-ess:~$ touch test        ⟵ groep student (oud)
```
Uitloggen en opnieuw inloggen (ssh), dan:
```bash
student@linux-ess:~$ touch test2       ⟵ groep it (nieuw)
```

## Test jezelf
::: details 1. Welk commando toont je uid, gid en groepen, en wat is de uid van root?
`id`. Root heeft uid 0.
:::

::: details 2. Maak gebruiker pxl aan met homefolder en commentaar "Docent".
`sudo useradd -m -c "Docent" pxl`
:::

::: details 3. Wat is het gevaar van sudo usermod -G it student? (voer NIET uit)
Omdat er niet `-a` bijstaat, verdwijnt student uit alle andere extra groepen, ook `sudo`.
:::

::: details 4. Verschil tussen su en su -?
Met het koppelteken wordt het profiel geladen en kom je in de homefolder van de nieuwe gebruiker.
:::

::: details 5. Waarom kan een gewone gebruiker /etc/shadow niet lezen?
Daarin staan de geëncrypte wachtwoorden van alle gebruikers. Enkel root (of een gebruiker met sudo-rechten) mag dat.
:::

::: details 6. Je wijzigt je primaire groep. Waarom krijgt een nieuw bestand toch nog de oude groep?
De sessie kent de wijziging pas na uitloggen en opnieuw inloggen.
:::
