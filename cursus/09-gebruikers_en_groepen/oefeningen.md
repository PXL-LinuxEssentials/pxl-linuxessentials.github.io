# Oefeningen op Gebruikers

## Oefening 1

Het bestand `/etc/passwd` bevat per gebruiker één regel, verdeeld in 7 velden gescheiden door een `:`. Geef een beschrijving van elk veld:

::: details Oplossing tonen
```
Field 1: gebruikersnaam
Field 2: wachtwoordveld (meestal 'x' → echte hash staat in /etc/shadow)
Field 3: UID (User ID)
Field 4: primaire GID (Group ID)
Field 5: GECOS/omschrijving (volledige naam e.d.)
Field 6: homedirectory
Field 7: inlogshell (bijv. /bin/bash)
```
:::

## Oefening 2

In de begindagen van Unix bevatte `/etc/passwd` ook een gecodeerde versie van het wachtwoord. Omdat iedereen dit bestand kan lezen, was dit een beveiligingsprobleem. Daarom werden wachtwoorden verplaatst naar een apart bestand dat alleen toegankelijk is voor de root-gebruiker.

Wat is de naam van het bestand met de gecodeerde wachtwoorden?

::: details Oplossing tonen
```
/etc/shadow
```
:::

## Oefening 3

Maak een gebruiker met de volgende kenmerken:

- Gebruikersnaam: `john`
- Gebruikers-ID: `1111`
- Primaire Groep-ID: `100` (= users)
- Beschrijving: `John Doe`
- Home-dir: `/home/john`
- Shell: `/bin/bash`

::: details Oplossing tonen
```
sudo useradd -u 1111 -g 100 -c "John Doe" -d /home/john -s /bin/bash -m john
```

*`-m` maakt de homefolder aan (gevuld met de standaardbestanden uit `/etc/skel`)*
:::

## Oefening 4

Controleer de gewijzigde bestanden: wat is er gewijzigd in het bestand `/etc/passwd`?

::: details Oplossing tonen
*Er is één regel voor `john` toegevoegd.*

```
grep '^john:' /etc/passwd
```
:::

## Oefening 5

Wat is er veranderd in het bestand `/etc/shadow`?

Na het aanmaken staat het wachtwoord op `!`, wat betekent dat er nog niet kan worden ingelogd. Stel het wachtwoord van John in op `Januari`.

::: details Oplossing tonen
*Er is een regel voor `john` toegevoegd, met `!` in het wachtwoordveld.*

```
sudo grep '^john:' /etc/shadow
```

```
sudo passwd john
```

*Typ `Januari` twee keer wanneer gevraagd.*

```
sudo grep '^john:' /etc/shadow
```
:::

## Oefening 6

Wat is er gewijzigd in het bestand `/etc/group`?

::: details Oplossing tonen
```
grep 'john' /etc/group
```

*Bij aanmaak met primaire GID 100 wordt `/etc/group` doorgaans niet aangepast, tenzij je john aan extra (secundaire) groepen toevoegt.*
:::

## Oefening 7

Wat is er veranderd in de directory `/home`?

::: details Oplossing tonen
```
ls /home
```
```
ls -ld /home/john
```
```
sudo ls -la /home/john
```

*`/home/john` is aangemaakt en gevuld met de standaardbestanden uit `/etc/skel`.*
:::

## Oefening 8

Log in als John en voer het commando `id` uit.

::: details Oplossing tonen
```
su - john
```
```
id
```

*Of zonder in te loggen:*

```
id john
```
:::

## Oefening 9

Verwijder de gebruiker John van je systeem met `userdel -r john`. Wat is er gewijzigd in het bestand `/etc/passwd`?

::: details Oplossing tonen
```
sudo userdel -r john
```

*De regel voor `john` is verwijderd:*

```
grep '^john:' /etc/passwd || echo "john niet gevonden in /etc/passwd"
```
:::

## Oefening 10

Wat is er veranderd in het bestand `/etc/shadow`?

::: details Oplossing tonen
```
sudo grep '^john:' /etc/shadow || echo "john niet gevonden in /etc/shadow"
```

*De regel voor `john` is verwijderd.*
:::

## Oefening 11

Wat is er veranderd in het bestand `/etc/group`?

::: details Oplossing tonen
```
grep 'john' /etc/group || echo "Geen vermeldingen van john in /etc/group"
```

*Normaal geen wijziging (tenzij john lid was van extra groepen).*
:::

## Oefening 12

Bestaat de directory `/home/john` nog?

::: details Oplossing tonen
```
[ -d /home/john ] && echo "bestaat" || echo "bestaat niet"
```

*Door de optie `-r` bij `userdel` wordt de homefolder mee verwijderd.*
:::

## Oefening 13

Maak een gebruiker `sarah`, door enkel de gebruikersnaam op te geven én aan te geven dat ze een homefolder moet hebben.

::: details Oplossing tonen
```
sudo useradd -m sarah
```
:::

## Oefening 14

Bekijk de gewijzigde bestanden. Wat is er gewijzigd in het bestand `/etc/passwd`?

::: details Oplossing tonen
```
grep '^sarah:' /etc/passwd
```
:::

## Oefening 15

Wat is er veranderd in het bestand `/etc/shadow`?

::: details Oplossing tonen
```
sudo grep '^sarah:' /etc/shadow
```

*Een nieuwe entry met `!` in het wachtwoordveld — inloggen is nog niet mogelijk tot er een wachtwoord is ingesteld.*
:::

## Oefening 16

Wat is er veranderd in het bestand `/etc/group`?

::: details Oplossing tonen
```
grep '^sarah:' /etc/group
```

*Op Ubuntu/Debian wordt standaard een privégroep `sarah` aangemaakt als primaire groep.*
:::

## Oefening 17

Wat is er veranderd in de directory `/home`?

::: details Oplossing tonen
```
ls -ld /home/sarah
```
:::

## Oefening 18

Geef de gebruiker Sarah een wachtwoord.

::: details Oplossing tonen
```
sudo passwd sarah
```
:::

## Oefening 19

Probeer in te loggen als Sarah.

::: details Oplossing tonen
```
su - sarah
```
:::

## Oefening 20

Verwijder de gebruiker Sarah, maar behoud haar thuismap.

::: details Oplossing tonen
```
sudo userdel sarah
```

*Zonder `-r` blijft de homefolder `/home/sarah` bestaan.*
:::

## Oefening 21

Verwijder de thuismap van Sarah.

::: details Oplossing tonen
```
sudo rm -r /home/sarah
```
:::

---

# Oefeningen op Groepen

## Oefening 1

Elk Linux-systeem is een multi-user systeem waarbij gebruikers in groepen zijn ingedeeld. Groepen worden gedefinieerd in `/etc/group`.

Zoek de groeps-ID op van de volgende groepen:

| Groep | Groep-ID |
|---|---|
| root | ? |
| adm | ? |
| lp | ? |
| users | ? |
| jouw primaire groep | ? |

::: details Oplossing tonen
```
grep '^root:' /etc/group | cut -d: -f3
```
```
grep '^adm:' /etc/group | cut -d: -f3
```
```
grep '^lp:' /etc/group | cut -d: -f3
```
```
grep '^users:' /etc/group | cut -d: -f3
```

*Jouw primaire groep (nummer en naam):*

```
id -g
```
```
id -gn
```
:::

## Oefening 2

Maak een groep met de naam `ict` en groep-id `1200`.

::: details Oplossing tonen
```
sudo groupadd -g 1200 ict
```
:::

## Oefening 3

Wijzig de naam van de groep `ict` in `helpdesk`.

::: details Oplossing tonen
```
sudo groupmod -n helpdesk ict
```
:::

## Oefening 4

Voeg jezelf toe aan de groep `helpdesk` als secundaire groep.

::: details Oplossing tonen
```
sudo usermod -aG helpdesk "$USER"
```
:::

## Oefening 5

Controleer of het systeem weet dat je aan deze groep bent toegevoegd.

::: details Oplossing tonen
```
id
```

*De nieuwe groep verschijnt pas na opnieuw inloggen in een nieuwe shell.*
:::

## Oefening 6

Log uit en opnieuw in met jouw gebruiker.

::: details Oplossing tonen
*Sluit je sessie volledig af en log opnieuw in. Voor groepslidmaatschap is volledig herinloggen het zekerst.*
:::

## Oefening 7

Controleer of het systeem nu weet dat je aan de groep bent toegevoegd.

::: details Oplossing tonen
```
id
```
```
groups
```
:::

## Oefening 8

Verwijder jezelf uit de groep `helpdesk`.

::: details Oplossing tonen
```
sudo deluser "$USER" helpdesk
```
:::

## Oefening 9

Voeg jezelf toe aan de groep `helpdesk` als **primaire** groep.

::: details Oplossing tonen
```
sudo usermod -g helpdesk "$USER"
```
:::

## Oefening 10

Zorg ervoor dat het systeem weet dat dit je nieuwe primaire groep is.

::: details Oplossing tonen
*Log opnieuw in, daarna:*

```
id
```
:::

## Oefening 11

Maak een lege map en een leeg bestand aan in je homefolder.

::: details Oplossing tonen
```
mkdir ~/lege_map
```
```
touch ~/leeg_bestand
```
:::

## Oefening 12

Voer `ls -l` uit in je homefolder. Wat valt je op aan de twee nieuwe items?

::: details Oplossing tonen
```
ls -l ~
```

*De nieuwe map en het nieuwe bestand behoren toe aan jouw gebruiker én aan jouw huidige primaire groep `helpdesk`. Nieuwe bestanden en mappen nemen de primaire groep van de aanmaker over.*
:::

## Oefening 13

Geef jezelf je eigen primaire groep terug.

::: details Oplossing tonen
```
sudo usermod -g "$USER" "$USER"
```

*De primaire groep heeft op Ubuntu/Debian doorgaans dezelfde naam als de gebruikersnaam.*
:::

## Oefening 14

Verwijder de groep `helpdesk`.

::: details Oplossing tonen
```
sudo groupdel helpdesk
```
:::
