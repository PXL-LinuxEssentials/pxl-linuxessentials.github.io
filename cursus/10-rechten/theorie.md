# 10. Rechten

Vanaf het begin werd Unix (en dus Linux) gebouwd als een multiuser besturingssysteem. Als je meerdere gebruikers op hetzelfde systeem hebt, heb je een manier nodig om te voorkomen dat gebruikers toegang krijgen tot bestanden van andere gebruikers en om te voorkomen dat gewone gebruikers toegang krijgen tot bestanden en programma's die alleen voor de systeembeheerder zijn bedoeld. Aan de andere kant moeten gebruikers ook bestanden met anderen kunnen delen, zodat ze effectief kunnen samenwerken. Als systeembeheerder is het kunnen blokkeren of verlenen van toegang tot bestanden een van de belangrijkste stappen om een systeem veilig te houden.

Zoals je in het vorige hoofdstuk hebt gezien, wordt je systeem al geleverd met een verstandige set van file permissions. Als gewone gebruiker heb je volledige controle over je eigen homefolder. Je kan bestanden en mappen maken, bewerken en verwijderen in je eigen homefolder (/home/student). Als je een bestand buiten je home-directory probeert te maken of te wijzigen, krijg je een foutmelding (permission denied). De enige uitzondering is de directory /tmp. Bijvoorbeeld: Je kan de gebruikersdatabase zien in /etc/passwd maar niet bewerken als een gewone gebruiker. Soms mag een gewone gebruiker de inhoud van een bepaald bestand of een bepaalde map niet eens zien. Bv: /etc/shadow bevat de wachtwoorden van gebruikers, daarom mag je het niet eens lezen.

Machtigingsfouten zijn een veelvoorkomende bron van problemen. Het begrijpen en manipuleren van file permissions is een cruciale stap om een competente Linux-beheerder te worden.

 Alleen omdat je het kunt, betekent niet dat je het moet doen. Houd er bij het troubleshooten van permission errors altijd rekening mee dat machtigingen je eerste verdedigingslinie zijn tegen kwaadwillende actoren. Vraag jezelf altijd af waarom een programma of een gebruiker toegang moet hebben en ga voorzichtig te werk. Verleen niet alleen machtigingen om van een bepaalde foutmelding af te komen!


## Octale notaties
Wanneer je de uitgebreide informatie voor een bestand bekijkt met ls met de optie -l , zie je drie sets van drie machtigingen die op het bestand zijn toegepast. De mogelijke machtigingen zijn: read, write en execute. Toestemming om de inhoud van een bestand te lezen, toestemming om de inhoud van een bestand te wijzigen en toestemming om een bestand uit te voeren als een script of programma. Wanneer een toestemming niet wordt verleend, vind je een - in de positie van de geweigerde toestemming.

```bash
student@linux-ess:~/course$ ls -l
total 4
-rw-rw-r-- 1 student student    0 okt  2 19:36 config
drwxrwxr-x 2 student student 4096 okt  2 19:36 folder
-rw-rw-r-- 1 student student    0 okt  2 19:36 rights.jpg
-rw-rw-r-- 1 student student    0 okt  2 19:36 test.txt
```

Het eerste teken is een - (min) voor een regulier bestand en een d voor een map. Er zijn ook een aantal speciale karakters: b voor block bestanden, c voor character apparaat bestanden, p voor pipe bestanden, l voor symbolisch gelinkte bestanden en s voor socket bestanden.

Mappen in Linux hebben dezelfde set van permissies. Maar omdat je execute-rechten nodig hebt om toegang te krijgen tot bestanden in de map, kan je weinig zonder. De algemene permissies zijn rwx voor een map waar je alles kunt doen, r-x voor een alleen-lezen directory en natuurlijk --- wanneer je de toegang volledig wilt blokkeren.

Er zijn drie sets omdat er drie verschillende sets mensen zijn waarop permissies kunnen worden toegepast. De eerste set beschrijft de machtigingen voor de eigenaar van het bestand (de eerste naam achter de permissies), de tweede is van toepassing op iedereen die lid is van de groep die eigenaar is van het bestand (de tweede naam). De laatste set is voor iedereen die niet onder één van de eerste twee categorieën valt. Dus in het kort: De drie sets zijn van toepassing op userowner, groupowner en others, in die volgorde.

Wanneer een gebruiker een bestand maakt, wordt hij automatisch de eigenaar van dat bestand. De groep die eigenaar is van het bestand wordt bepaald door de primaire groep van de gebruiker. Standaard is de primary group van een gebruiker een groep met dezelfde naam als de gebruikersnaam, daarom zie je vaak dat owner en groupowner dezelfde naam hebben (zoals student student in het bovenstaande voorbeeld). De map /dev, die de bestanden bevat die je hardware vertegenwoordigen, is één van de plaatsen waar je bestanden vindt die eigendom zijn van de root-gebruiker met een andere groep als eigenaar.

```bash
student@linux-ess:~$ ls -l /dev/[ns][drv]*
crw-rw---- 1 root root   237, 0 Nov 11 10:44 /dev/nvme0
brw-rw---- 1 root disk   259, 0 Nov 11 10:44 /dev/nvme0n1
brw-rw---- 1 root disk   259, 1 Nov 11 10:44 /dev/nvme0n1p1
brw-rw---- 1 root disk   259, 2 Nov 11 10:44 /dev/nvme0n1p2
brw-rw---- 1 root disk   259, 3 Nov 11 10:44 /dev/nvme0n1p3
brw-rw---- 1 root disk     8, 0 Nov 11 10:44 /dev/sda
brw-rw---- 1 root cdrom   11, 0 Nov 11 10:43 /dev/sr0
```

File permissions worden op schijf geschreven als een veld met bits in de eigenschappen van het bestand. Een bit is ingesteld op 1 wanneer een toestemming wordt verleend, 0 wanneer dat niet het geval is. Dus rwxrw-r-- wordt 111110100. Omdat mensen niet erg goed zijn in het ontleden van binaire sequenties, worden ze weergegeven als octale getallen, getallen van 0 tot 7 (000 tot 111 in binair). Om het octale getal te berekenen, onthoud dat lezen 4 waard is, bewerken 2 en uitvoeren 1. Voeg die toe die je nodig hebt en je krijgt de octale notatie. Het bovenstaande voorbeeld wordt 764 (rwx = 4+2+1=7, rw- = 4+2+0=6, r-- = 4+0+0=4).

| Binair | Octaal | Toegangsrechten (rwx) | Korte beschrijving                                                                                |
| ------ | ----- | ---------------------- | ------------------------------------------------------------------------------------------------- |
| 000    | 0     | ---                    | Geen rechten: kan niet lezen, schrijven of uitvoeren.                                             |
| 001    | 1     | --x                    | Alleen uitvoeren: kan als programma worden uitgevoerd. (heeft ook r nodig om te draaien)          |
| 010    | 2     | -w-                    | Alleen schrijven: kan worden gewijzigd, maar niet gelezen.                                        |
| 011    | 3     | -wx                    | Schrijven en uitvoeren: wijzigen en als programma uitvoeren. (heeft ook r nodig om uit te voeren) |
| 100    | 4     | r--                    | Alleen lezen: kan worden bekeken, maar niet gewijzigd of uitgevoerd.                              |
| 101    | 5     | r-x                    | Lezen en uitvoeren: bekijken en als programma uitvoeren.                                          |
| 110    | 6     | rw-                    | Lezen en schrijven: bekijken en wijzigen.                                                         |
| 111    | 7     | rwx                    | Volledige rechten: bekijken, wijzigen en uitvoeren.                                               |


## Rechten wijzigen (chmod)
Om de machtigingen op een bestand te wijzigen, kan je het commando chmod gebruiken.

Om machtigingen van een bestand toe te voegen of weg te halen, kan je de volgende methode gebruiken, waarbij rwx staat voor de rechten die je wilt toevoegen of weghalen, en ugo staat voor respectievelijk userowner (gebruikerseigenaar), groupowner (groepseigenaar) en others (andere). Als je a opgeeft voor het aanduiden voor wie je de rechten wilt wijzigen, wordt deze voor alle drie gewijzigd:

```bash
student@linux-ess:~$ touch test  
student@linux-ess:~$ ls -l test
-rw-rw-r-- 1 student student 0 Nov 11 13:11 test
student@linux-ess:~$ chmod a+x test  
student@linux-ess:~$ ls -l test   
-rwxrwxr-x 1 student student 0 okt  2 19:36 test  
student@linux-ess:~$ chmod g-w test  
student@linux-ess:~$ ls -l test   
-rwxr-xr-x 1 student student 0 okt  2 19:36 test  
student@linux-ess:~$ chmod go-rx test
student@linux-ess:~$ ls -l test 
-rwx------ 1 student student 0 okt  2 19:36 test
```

Wanneer je de machtigingen volledig herschrijft, kan je chmod ook gebruiken met de octale notatie:

```bash
student@linux-ess:~$ touch config  
student@linux-ess:~$ ls -l config  
-rw-rw-r-- 1 student student    0 okt  2 19:36 config
student@linux-ess:~$ chmod 600 config 
student@linux-ess:~$ ls -l config
-rw------- 1 student student    0 okt  2 19:36 config
student@linux-ess:~$ chmod 744 config
student@linux-ess:~$ ls -l config
-rwxr--r-- 1 student student    0 okt  2 19:36 config
```

De laatste optie is sneller wanneer je machtigingen volledig moet herschrijven (omdat je de bestaande machtigingen niet hoeft te controleren, maar gewoon overschrijven). De eerste kan praktisch zijn voor het aanbrengen van snelle wijzigingen, zoals het uitvoerbaar maken van een bestand.

![chmod-777](./assets/chmod-777.svg)

## Van eigenaar veranderen (chgrp, chown)
Naast het wijzigen van de machtigingen van een bestand, moet je ook wijzigen op wie deze machtigingen van toepassing zijn, door de gebruiker of groep te wijzigen die eigenaar is van het bestand. Je hebt sudo nodig om bestanden toe te wijzen aan verschillende gebruikers/groepen.

Om de groepseigenaar van een bestand of map te wijzigen, kan je het commando chgrp gebruiken. Om dit recursief te wijzigen, gebruik je de optie -R

```bash
student@linux-ess:~$ ls -l course/
total 4
-rwxr--r-- 1 student student    0 okt  2 19:36 config
drwxrwxr-x 2 student student 4096 okt  2 19:36 folder
-rw-rw-r-- 1 student student    0 okt  2 19:36 rights.jpg
-rw-rw-rw- 1 student student    0 okt  2 19:36 test.txt
student@linux-ess:~$ sudo chgrp -R it course/
student@linux-ess:~$ ls -l course/
total 4
-rwxr--r-- 1 student it    0 okt  2 19:36 config
drwxrwxr-x 2 student it 4096 okt  2 19:36 folder
-rw-rw-r-- 1 student it    0 okt  2 19:36 rights.jpg
-rw-rw-rw- 1 student it    0 okt  2 19:36 test.txt
student@linux-ess:~$ ls -ld course/
drwxrwxr-x 3 student it 4096 okt  2 19:36 course/
```

Het chown commando is veelzijdiger, hiermee kun je van eigenaar en/of groep veranderen. Het heeft dezelfde -R optie om een hele file-tree te wijzigen.

```bash
student@linux-ess:~/course$ sudo chown teacher rights.jpg #verander de eigenaar
student@linux-ess:~/course$ ls -l rights.jpg
-rw-rw-r-- 1 teacher it    0 okt  2 19:36 rights.jpg
student@linux-ess:~/course$ sudo chown teacher:root config folder #verander de eigenaar en de groep
student@linux-ess:~/course$ ls -l 
total 4
-rwxr--r-- 1 teacher root    0 okt  2 19:36 config
drwxrwxr-x 2 teacher root 4096 okt  2 19:36 folder
-rw-rw-r-- 1 teacher it        0 okt  2 19:36 rights.jpg
-rw-rw-rw- 1 student it        0 okt  2 19:36 test.txt
student@linux-ess:~/course$ sudo chown :it config #verander de groep
student@linux-ess:~/course$ ls -l config
-rwxr--r-- 1 teacher    it        0 okt  2 19:36 config
```

## Default permissions (umask)
Een andere belangrijke instelling is de default permissions. Welke rechten worden toegepast wanneer je nieuwe bestanden en mappen maakt?

De maximale rechten voor nieuwe bestanden is 666, dus -rw-rw-rw-. Nieuwe bestanden worden nooit gemaakt met uitvoerrechten. Dit wordt afgedwongen door de kernel. Het is natuurlijk mogelijk om de execute bit toe te voegen na het maken van bestanden met behulp van chmod, maar het vereist altijd een bewuste beslissing om veiligheidsredenen. Mappen hebben deze beperking niet, omdat een map zonder een execute bit vrij nutteloos is.

```bash
student@linux-ess:~/course$ touch file
student@linux-ess:~/course$ mkdir folder
```

```bash
student@linux-ess:~/course$ ls -l
total 4
-rw-rw-r-- 1 student student    0 okt 15 15:56 file
drwxrwxr-x 2 student student 4096 okt 15 15:56 folder
```

Zoals je kan zien, krijgen we niet de verwachte -rw-rw-rw- voor het bestand, noch drwxrwxrwx voor de map. Dit komt omdat de meeste distributies strenger zijn dan de Linux-kernel toestaat. Het gebruik van de kernel-standaard zou betekenen dat gemaakte bestanden en mappen bewerkbaar zijn door elke gebruiker op het systeem.

::: warning Bestanden zijn leesbaar voor anderen
Standaard zijn nieuw gemaakte bestanden leesbaar voor alle gebruikers op het systeem. Sla gevoelige bestanden niet zomaar op zonder de rechten aan te passen.
:::

De exacte configuratie van machtigingen voor nieuwe bestanden en mappen wordt ingesteld door de umask. Dit is een waarde die het masker definieert dat wordt toegepast op alle nieuw gemaakte bestanden en mappen. Om het huidige masker te zien, gebruik je het commando umask.

```bash
student@linux-ess:~/course$ umask
0002
```

Hoe werkt dit dan? We trekken de umask af van 777 en geven nooit uitvoeringsrechten op een nieuw bestand. Voor een bestand krijg je dus 775 (rwxrwxr-x), maar omdat je nooit de execute bit instelt resulteert dit in 664 of rw-rw-r-- . Voor mappen trekken we ook de umask (hier 002) af van 777, dit resulteert in 775 en hier houden we de uitvoer-bits. Een umask van 000 staat alles toe, een umask van 777 maakt dat een nieuw bestand of map geen rechten heeft. De getallen werken nog steeds hetzelfde (4 voor lezen, 2 voor bewerken, 1 voor uitvoeren), maar deze keer gebruik je ze om bepaalde machtigingsbits te maskeren, of eenvoudiger gezegd: bepaalde machtigingen voor nieuwe bestanden en mappen te weigeren.

Je kan de umask instellen (=wijzigen) met hetzelfde umask commando.

```bash
student@linux-ess:~/course$ umask 000       # 777-000=777 en de x wordt nooit toegepast op nieuwe bestanden
student@linux-ess:~/course$ touch newfile1
student@linux-ess:~/course$ ls -l newfile1
-rw-rw-rw- 1 student student 0 okt 15 16:23 newfile1
 
student@linux-ess:~/course$ umask 027       # Als je meerdere bits wil maskeren, tel ze dan op  (777-027=750)
student@linux-ess:~/course$ touch newfile2
student@linux-ess:~/course$ ls -l newfile2
-rw-r----- 1 student student 0 okt 15 16:24 newfile2
student@linux-ess:~/course$ mkdir newfolder1
student@linux-ess:~/course$ ls -ld newfolder1
drwxr-x--- 2 student student 4096 okt 15 16:25 newfolder1
 
student@linux-ess:~/course$ umask 077 
student@linux-ess:~/course$ mkdir newfolder2
student@linux-ess:~/course$ ls -ld newfolder2
drwx------ 2 student student 4096 okt 15 16:25 newfolder2
```

::: info Umask permanent instellen
Als je de umask instelt met het commando, geldt dit alleen voor de huidige terminalsessie. Wanneer je de terminal sluit, wordt de standaardwaarde hersteld. Om de instelling permanent te maken, voeg je `umask <uw umask>` toe aan het `.profile`-bestand in je homefolder.
:::

Nog een laatste ding om op te letten: als je naar het volgende voorbeeld kijkt, zie je dat bestanden die door de rootgebruiker zijn gemaakt een andere umask-set hebben.

```bash
student@linux-ess:~/course$ touch file
student@linux-ess:~/course$ sudo touch file2
student@linux-ess:~/course$ ls -l
-rw-rw-r-- 1 student student 0 okt 15 16:44 file
-rw-r--r-- 1 root    root    0 okt 15 16:44 file2
```

Dit verschil heeft twee oorzaken:

* **Bestanden die je met `sudo` maakt:** `sudo` gebruikt zelf een standaard umask van `022`. Daardoor krijgen ze geen schrijfrechten voor groep en anderen (`644`), ook al is jouw umask `002`.
* **Je eigen umask (`002`):** die wordt bij het inloggen ingesteld door de PAM-module `pam_umask`, samen met een instelling in `/etc/login.defs`. Je ziet beide hier:

```bash
student@linux-ess:~$ grep -rn -i umask /etc/pam.d/
/etc/pam.d/common-session:26:session optional                   pam_umask.so
/etc/pam.d/common-session-noninteractive:27:session optional                    pam_umask.so
student@linux-ess:~$ grep -i -E 'umask|usergroups' /etc/login.defs
USERGROUPS_ENAB yes
```

In `/etc/login.defs` staat geen `UMASK`-regel meer. Zonder waarde laat `pam_umask` de umask ongemoeid: die erf je dan van het proces dat je sessie start (bij een login is dat `022`). De regel `USERGROUPS_ENAB yes` zorgt ervoor dat `pam_umask` voor een gewone gebruiker met een eigen primaire groep (dezelfde naam als de gebruiker, zoals `student`) de groepsbits gelijk zet aan de eigenaarbits. Zo wordt `022` dus `002`, en dat verklaart waarom `student` bestanden maakt met `rw-rw-r--`. Root houdt `022`. Meer uitleg vind je in `man pam_umask`.

::: info Oudere Ubuntu-versies
In Ubuntu 24.04 en ouder stond in `/etc/login.defs` ook nog `UMASK 022`. In Ubuntu 26.04 is die regel weg. `USERGROUPS_ENAB yes` staat er nog wel, en daardoor krijgt een gewone gebruiker nog steeds `002`.
:::

 Je kan de letternotatie ook gebruiken met umask:

```bash
student@linux-ess:~$ umask
0002
student@linux-ess:~$ umask -S
u=rwx,g=rwx,o=rx
student@linux-ess:~$ touch file3
student@linux-ess:~$ ls -l file3
-rw-rw-r-- 1 student student 0 Nov 11 14:01 file3
student@linux-ess:~$ umask u=rwx,g=rx,o=
student@linux-ess:~$ umask
0027
student@linux-ess:~$ umask -S
u=rwx,g=rx,o=
student@linux-ess:~$ touch file4
student@linux-ess:~$ ls -l file4
-rw-r----- 1 student student 0 Nov 11 14:03 file4
student@linux-ess:~$ mkdir folder4
student@linux-ess:~$ ls -ld folder4
drwxr-x--- 2 student student 4096 Nov 11 14:04 folder4
```


## Samenwerken in een team (setgid)
Als we willen samenwerken, is het belangrijk dat bepaalde gebruikers elkaars bestanden in een gedeeld mapje kunnen wijzigen. De oplossing om deze gebruikers dezelfde primaire groep te geven, is een beveiligingsprobleem omdat dit ook de rechten op hun homefolders verandert:

```bash
student@linux-ess:~$ sudo groupadd it 
student@linux-ess:~$ sudo useradd -m -g it -s /bin/bash liam
student@linux-ess:~$ sudo passwd liam
student@linux-ess:~$ sudo useradd -m -g it -s /bin/bash jacob
student@linux-ess:~$ sudo passwd jacob
student@linux-ess:~$ ls -ld /home/liam  /home/jacob
drwxr-x--- 2 jacob it 4096 Nov 26 15:39 /home/jacob
drwxr-x--- 2 liam  it 4096 Nov 26 15:32 /home/liam
student@linux-ess:~$ sudo ls -l /home/jacob/.profile
-rw-r--r-- 1 jacob it 807 Jan  6  2022 /home/jacob/.profile
student@linux-ess:~$ su - liam
Password:
liam@linux-ess:~$ head -3 /home/jacob/.profile
# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.  
liam@linux-ess:~$ exit
``` 

Zoals je kan zien, kan de gebruiker Liam de bestanden bekijken van de homefolder van de gebruiker Jacob en dat kan de bedoeling niet zijn.

We geven eerst beide gebruikers hun eigen primaire groep:

```bash
student@linux-ess:~$ sudo groupadd liam
student@linux-ess:~$ sudo groupadd jacob
student@linux-ess:~$ sudo usermod -g liam liam
student@linux-ess:~$ sudo usermod -g jacob jacob
student@linux-ess:~$ ls -ld /home/liam  /home/jacob                  # homefolders zijn opnieuw afgeschermd (=privé)
drwxr-x--- 2 jacob jacob 4096 Nov 26 15:39 /home/jacob
drwxr-x--- 2 liam  liam  4096 Nov 26 15:32 /home/liam
student@linux-ess:~$ sudo ls -l /home/jacob/.profile
-rw-r--r-- 1 jacob jacob 807 Jan  6  2022 /home/jacob/.profile
```

::: info Primaire groep en bestandseigendom
Het wijzigen van de primaire groep van een gebruiker verandert ook de groepseigenaar van elk bestand in zijn homefolder.
:::

We maken een groep voor de twee gebruikers om hen rechten te geven op een gedeelde map die we in de volgende stap zullen maken. We voegen de gebruikers ook toe aan deze nieuwe groep:

```bash
student@linux-ess:~$ sudo groupadd ict
student@linux-ess:~$ sudo usermod -aG ict liam
student@linux-ess:~$ sudo usermod -aG ict jacob
student@linux-ess:~$ grep ict /etc/group
ict:x:1005:liam,jacob
``` 

We zullen de map maken die wordt gedeeld tussen de twee gebruikers en geven deze de nodige machtigingen:

```bash
student@linux-ess:~$ sudo mkdir -p /shares/ict
student@linux-ess:~$ ls -ld /shares/ict
drwxr-xr-x 2 root root 4096 Nov 26 15:58 /shares/ict
student@linux-ess:~$ sudo chgrp ict /shares/ict
student@linux-ess:~$ ls -ld /shares/ict
drwxr-xr-x 2 root ict 4096 Nov 26 15:58 /shares/ict
student@linux-ess:~$ sudo chmod g+w /shares/ict
student@linux-ess:~$ ls -ld /shares/ict
drwxrwxr-x 2 root ict 4096 Nov 26 15:58 /shares/ict
```

Zoals je kan zien, hebben leden van de groep ict de toestemming om in de gedeelde map ict te kijken en om bestanden en mappen in deze map te maken/verwijderen

Maar er is een probleem wanneer de gebruikers een bestand maken in de share:

```bash
student@linux-ess:~$ su - jacob
Password:
jacob@linux-ess:~$ cd /shares/ict/
jacob@linux-ess:/shares/ict$ touch testfile
jacob@linux-ess:/shares/ict$ mkdir testdir
jacob@linux-ess:/shares/ict$ ls -l
total 4
drwxrwxr-x 2 jacob jacob 4096 Nov 26 16:12 testdir
-rw-rw-r-- 1 jacob jacob    0 Nov 26 16:11 testfile
jacob@linux-ess:/shares/ict$ exit
logout
student@linux-ess:~$ su - liam
Password:
liam@linux-ess:~$ cd /shares/ict/
liam@linux-ess:/shares/ict$ ls
testdir  testfile
liam@linux-ess:/shares/ict$ echo hallo >> testfile
-bash: testfile: Permission denied
liam@linux-ess:/shares/ict$ ls -ld testdir
drwxrwxr-x 2 jacob jacob 4096 Nov 27 20:44 testdir
liam@linux-ess:/shares/ict$ cd testdir
liam@linux-ess:/shares/ict/testdir$ touch testfile2
touch: cannot touch 'testfile2': Permission denied
liam@linux-ess:/shares/ict$ exit
```

Zoals je kan zien, kunnen ze niet samenwerken aan dezelfde bestanden of in dezelfde mappen

Een oplossing is het gebruik van de speciale bit, genaamd setgid. We kunnen het aan de gedeelde map ict geven met het commando chmod g+s (om te verwijderen zouden we g-s gebruiken):

```bash
student@linux-ess:~$ ls -ld /shares/ict/
drwxrwxr-x 3 root ict 4096 Nov 26 16:12 /shares/ict/
student@linux-ess:~$ sudo chmod g+s /shares/ict            # or sudo chmod 2775 /shares/ict
student@linux-ess:~$ ls -ld /shares/ict/
drwxrwsr-x 3 root ict 4096 Nov 26 16:12 /shares/ict/
```

Zoals je kunt zien in de machtigingen van de groepseigenaar eindigt het nu met een letter s. Een kleine letter s betekent dat er een x onder zit, een hoofdletter S betekent dat er geen x onder zit.

De speciale bit setgid betekent dat bestanden en mappen die in deze map worden gemaakt, dezelfde groepseigenaar krijgen als deze map zelf:

```bash
student@linux-ess:~$ ls -l /shares/ict/ 
total 4
drwxrwxr-x 2 jacob jacob 4096 Nov 26 16:12 testdir
-rw-rw-r-- 1 jacob jacob    0 Nov 26 16:11 testfile
student@linux-ess:~$ su - jacob
Password:
jacob@linux-ess:~$ cd /shares/ict/
jacob@linux-ess:/shares/ict$ echo "This is Jacob's text" > testfile2
jacob@linux-ess:/shares/ict$ mkdir testdir2
jacob@linux-ess:/shares/ict$ ls -l
total 12
drwxrwxr-x 2 jacob jacob 4096 Nov 26 16:12 testdir
drwxrwsr-x 2 jacob ict   4096 Nov 26 16:26 testdir2
-rw-rw-r-- 1 jacob jacob    0 Nov 26 16:11 testfile
-rw-rw-r-- 1 jacob ict     21 Nov 26 16:26 testfile2
jacob@linux-ess:/shares/ict$ exit
logout
student@linux-ess:~$ su - liam
Password:
liam@linux-ess:~$ cd /shares/ict/
liam@linux-ess:/shares/ict$ echo "This is Liam's text" >> testfile2
liam@linux-ess:/shares/ict$ cat testfile2
This is Jacob's text
This is Liam's text
liam@linux-ess:/shares/ict$ exit
```

Zoals je ziet is de groepseigenaar van de nieuwe map en het nieuwe bestand ict en daarom kunnen beide gebruikers nu samenwerken met elkaars bestanden.

Merk ook op dat de subdirectory die wordt aangemaakt ook de setgid-bit ingesteld krijgt!

## De sticky bit
De setgid-bit lost het belangrijkste probleem op van het toegankelijk maken van bestanden in een gedeelde map die door één gebruiker is gemaakt voor andere gebruikers in dezelfde niet-primaire groep. Dit opent echter een ander probleem: elke gebruiker met toegang tot de share kan nu de bestanden van andere gebruikers in deze map verwijderen of hernoemen. In sommige gevallen, zoals een gedeeld project waar mensen aan werken, is dit prima. Maar in gevallen dat je dit niet wilt toestaan, wordt een andere speciale toestemmingsbit gebruikt: de sticky bit. Als je deze bit op een map instelt, kan geen enkele gebruiker (behalve de gebruiker root) bestanden of submappen hernoemen of verwijderen waarvan hij niet de eigenaar is in die map.

Dit principe wordt ook gebruikt in de map /tmp van het systeem, waardoor gebruikers de tijdelijke bestanden van een andere gebruikers niet kunnen verwijderen.

```bash
student@linux-ess:~$ ls -ld /tmp/
drwxrwxrwt 24 root root 4096 nov 27 13:50 /tmp/
```

::: info Sticky bit in ls-uitvoer
De `t` in de 'others' rechtenpositie vervangt de `x` wanneer de sticky bit is ingesteld.
:::

Net als bij andere machtigingsbits gebruik je chmod om de sticky bit toe te voegen of te verwijderen.

```bash
student@linux-ess:~$ su - liam
Password: 
liam@linux-ess:~$ cd /shares/ict/
liam@linux-ess:/shares/ict$ ls -l
total 8
-rw-rw-r-- 1 jacob jacob    0 nov 27 14:59 testdir
drwxrwsr-x 2 jacob ict   4096 nov 27 15:03 testdir2
-rw-rw-r-- 1 jacob jacob    0 nov 27 14:59 testfile
-rw-rw-r-- 1 jacob ict      4 nov 27 15:03 testfile2
liam@linux-ess:/shares/ict$ rm testfile2     #Liam kan Jacob's bestanden verwijderen.
liam@linux-ess:/shares/ict$ ls -l
total 4
-rw-rw-r-- 1 jacob jacob    0 nov 27 14:59 testdir
drwxrwsr-x 2 jacob ict   4096 nov 27 15:03 testdir2
-rw-rw-r-- 1 jacob jacob    0 nov 27 14:59 testfile
liam@linux-ess:/shares/ict$ exit
logout
student@linux-ess:~$ sudo chmod o+t /shares/ict/         # or sudo chmod 3775 /shares/ict/
student@linux-ess:~$ ls -ld /shares/ict/
drwxrwsr-t 3 root ict 4096 nov 27 15:05 /shares/ict/
student@linux-ess:~$ su - liam
Password: 
liam@linux-ess:~$ cd /shares/ict              #Vergeet  sudo sysctl fs.protected_regular=1  niet -> zie lager
liam@linux-ess:/shares/ict$ rm -rf testdir2/  #Liam kan Jacob's bestanden of mappen niet langer verwijderen
rm: cannot remove 'testdir2/': Operation not permitted    
liam@linux-ess:/shares/ict$ exit
logout
student@linux-ess:~$ sudo chmod o-t /shares/ict/         # or sudo chmod 2775 /shares/ict/
student@linux-ess:~$ ls -ld /shares/ict/
drwxrwsr-x 3 root ict 4096 nov 27 15:05 /shares/ict/
```

Binnen het veld met speciale machtigingen is de sticky bit de meest rechtse bit, met een waarde van één. Je kan dit gebruiken als je de machtigingen van een map volledig wilt herschrijven met behulp van de octale notatie. Voeg er gewoon een één toe voor de standaardmodus.

```bash
student@linux-ess:~$ cd /shares/
student@linux-ess:/shares$ sudo mkdir ict2
student@linux-ess:/shares$ sudo chown :ict ict2/         # or sudo chgrp ict ict2/
student@linux-ess:/shares$ ls -ld ict2/
drwxr-xr-x 2 root ict 4096 nov 27 15:16 ict2/
student@linux-ess:/shares$ sudo chmod 1775 ict2/
student@linux-ess:/shares$ ls -ld ict2/
drwxrwxr-t 2 root ict 4096 nov 27 15:16 ict2/
```

Het is ook mogelijk om de speciale bits te combineren. In het onderstaande voorbeeld combineren we de sticky bit met de setgid bit, de tweede bit in de triplet met een waarde van twee. Om de uiteindelijke waarde te krijgen, tel je beide waarden bij elkaar op (setgid+sticky=2+1=3) en plaats je deze voor de octale machtigingen (bijv. 3750) om een viercijferige modus te worden.

```bash
student@linux-ess:/shares$ sudo mkdir ict3
student@linux-ess:/shares$ sudo chown :ict ict3         # or sudo chgrp ict ict3/
student@linux-ess:/shares$ ls -ld ict3
drwxr-xr-x 5 root ict 4096 nov 27 15:20 ict3
student@linux-ess:/shares$ sudo chmod o-rx ict3
student@linux-ess:/shares$ ls -ld ict3
drwxr-x--- 5 root ict 4096 nov 27 15:20 ict3
student@linux-ess:/shares$ sudo chmod 3770 ict3
student@linux-ess:/shares$ ls -ld ict3
drwxrws--T 2 root ict 4096 nov 27 15:20 ict3 #zowel setgid en sticky bit staan aan, wanneer de x voor others niet aan staat, wordt er een hoofdletter T getoont
```

::: tip Speciale bits verwijderen
Om de sticky bit uit te zetten gebruik je een nul. Een driecijferige modus verwijdert ook de sticky bit, maar de setgid bit blijft behouden. Om **alle** speciale machtigingen te verwijderen, voeg je een extra nul toe aan de voorkant (`00xxx`).
:::

```bash
student@linux-ess:/shares$ ls -ld ict3/
drwxrws--T 2 root ict 4096 nov 27 15:20 ict3/
student@linux-ess:/shares$ sudo chmod 0777 ict3/        # or chmod 777
student@linux-ess:/shares$ ls -ld ict3/
drwxrwsrwx 2 root ict 4096 nov 27 15:20 ict3/
student@linux-ess:/shares$ sudo chmod 00775 ict3/
student@linux-ess:/shares$ ls -ld ict3/
drwxrwxr-x 2 root ict 4096 nov 27 15:20 ict3/
``` 

Als je wilt dat de gebruikers van de groep ict samenwerken aan elkaars bestanden en je tegelijkertijd wilt dat ze elkaars bestanden niet kunnen verwijderen, moet je echter de kernelparameter fs.protected_regular=1 instellen.

```bash
student@linux-ess:~$ su - jacob
Password:
jacob@linux-ess:~$ cd /shares/ict/
jacob@linux-ess:/shares/ict$ echo "This is Jacob's new text" > testfile2
jacob@linux-ess:/shares/ict$ exit
student@linux-ess:~$ ls -ld /shares/ict/
drwxrwsr-t 3 root ict 4096 nov 27 15:05 /shares/ict/
student@linux-ess:~$ su - liam
Password: 
liam@linux-ess:~$ cd /shares/ict/
liam@linux-ess:/shares/ict$ ls -l
total 8
-rw-rw-r-- 1 jacob jacob    0 nov 27 14:59 testdir
drwxrwsr-x 2 jacob ict   4096 nov 27 15:03 testdir2
-rw-rw-r-- 1 jacob jacob    0 nov 27 14:59 testfile
-rw-rw-r-- 1 jacob ict      4 nov 27 15:03 testfile2
liam@linux-ess:/shares/ict$ echo text from liam > testfile2     #Liam kan Jacob's bestanden niet veranderen.
-bash: testfile2 Permission denied
liam@linux-ess:/shares/ict$ exit
student@linux-ess:~$ sudo sysctl -a | grep regular
fs.protected_regular = 2
student@linux-ess:~$ sudo sysctl fs.protected_regular=1
fs.protected_regular = 1
student@linux-ess:~$ su - liam
Password: 
liam@linux-ess:~$ cd /shares/ict/
liam@linux-ess:/shares/ict$ echo text from liam > testfile2     #Liam kan Jacob's bestanden veranderen.
liam@linux-ess:~$ cat testfile2
text from liam
```

Als we de kernelparameter in de toekomst willen behouden, moeten we deze parameter wijzigen in het bestand /usr/lib/sysctl.d/99-protect-links.conf


## Een binary (= uitvoerbaar bestand) uitvoeren als de userowner (setuid)
Zoals je misschien hebt gemerkt, is er een derde bit waar we het niet over hebben gehad. Setuid, de meest linkse bit in het veld. Hierdoor kunnen uitvoerbare bestanden worden uitgevoerd met de machtigingen van de eigenaar van het bestand, niet degene die het uitvoert. Dit wordt bijvoorbeeld gebruikt door het passwd commando om gebruikers in staat te stellen hun eigen wachtwoord te wijzigen, omdat een normale gebruiker geen toegang heeft tot het /etc/shadow-bestand. Het instellen van de setuid bit kan ernstige beveiligingsrisico's met zich meebrengen en is bijna altijd een zeer slecht idee.

In het volgende voorbeeld laten we zien waarom een normale gebruiker (zonder rechten) zijn wachtwoord mag wijzigen in de shadow-file dat eigenlijk enkel toegankelijk is voor de gebruiker root.

```bash
student@linux-ess:~$ ls -l /etc/shadow
-rw-r----- 1 root shadow 2456 Nov 28  2022 /etc/shadow
student@linux-ess:~$ ls -l /bin/passwd
-rwsr-xr-x 1 root root 59976 Nov 24  2022 /bin/passwd
student@linux-ess:~$ stat -c '%a %n' /bin/passwd
4755 /bin/passwd 
```


## Overzicht van speciale bits
| Toestemming  | Effect op bestanden                                                                                   | Effect op mappen |
| ------------ | ----------------------------------------------------------------------------------------------------- | ---------------- |
| u+s (setuid) | Het bestand wordt uitgevoerd als de eigenaar van het bestand, niet als de gebruiker die het uitvoerde | Geen effect      |
| g+s (setgid) | Het bestand wordt uitgevoerd als de groep die het bestand bezit                                       | Bestanden die in de directory worden aangemaakt, krijgen dezelfde groepseigenaar als de directory |
| o+t (sticky) | Geen effect                                                                                           | Gebruikers met schrijfrechten voor de directory kunnen alleen bestanden verwijderen die ze zelf bezitten; ze kunnen geen bestanden van anderen verwijderen of geforceerd opslaan |


## Access control lists
De ACL-functie is gemaakt om gebruikers de mogelijkheid te bieden om selectief bestanden en mappen te delen met andere gebruikers en groepen.

Voordat ACL's kunnen worden geïmplementeerd, moeten we het pakket installeren:

```bash
student@linux-ess:~$ sudo apt install acl
```

Wanneer het is geïnstalleerd, moet het worden ingeschakeld wanneer het filesysteem wordt gemount. In onze Ubuntu installatie wordt de ACL-functionaliteit standaard geladen.

```bash
student@linux-ess:~$ sudo tune2fs -l /dev/mapper/ubuntu--vg-ubuntu--lv | grep --color=never "Filesystem\|mount"
Filesystem volume name:   <none>
Last mounted on:          /
Filesystem UUID:          a2d7c681-3183-4d3b-bc5a-3e9cb8411246
Filesystem magic number:  0xEF53
Filesystem revision #:    1 (dynamic)
Filesystem features:      has_journal ext_attr resize_inode dir_index filetype needs_recovery extent 64bit flex_bg sparse_super large_file huge_file dir_nlink extra_isize metadata_csum
Filesystem flags:         signed_directory_hash
Default mount options:    user_xattr acl
Filesystem state:         clean
Filesystem OS type:       Linux
Filesystem created:       Fri May 31 15:43:52 2024
Last mount time:          Sun Dec  1 10:21:35 2024
Maximum mount count:      -1
```

Om ACL's toe te voegen aan een bestand of map, gebruik je het setfacl commando. Wanneer we ACL's hebben ingesteld, kunnen deze worden bekeken met het getfacl commando.

Om ACL's toe te voegen moet je de eigenaar zijn van het bestand of de map. Als je wordt toegevoegd aan een ACL wil dit dus niet zeggen dat je de ACL's ook zelf kunt wijzigen.

ACL-machtigingen hebben voorrang op de reguliere bestandsmachtigingen. Enige uitzondering hierop zijn de rechten van de userowner. Indien de filepermissions van de userowner beknopter zijn dan de ACLs van deze gebruiker, dan zullen deze ACLs niet worden toegepast (dus r--... en ACL u : student : rw zal resulteren in enkel read rechten)

Alle ACL-machtigingen van de groepen waarvan een gebruiker lid is, zijn cumulatief. Dit betekent dat, als we in 2 groepen zitten die worden toegevoegd aan een bestand met ACL's, één met r-- rechten en één met rwx-rechten, we de rwx-rechten hebben.

::: warning Gebruiker-ACL overschrijft groep-ACL
Als je ACL-rechten hebt ingesteld op zowel een gebruiker als op een groep waar die gebruiker in zit, dan worden **alleen de gebruikersrechten** toegepast!
:::

Met het commando setfacl kunnen we ACL's wijzigen (-m) of verwijderen (-x).

```bash
student@linux-ess:~$ touch memo
student@linux-ess:~$ ls -l memo
-rw-rw-r-- 1 student student 0 Nov 11 14:15 memo
student@linux-ess:~$ getfacl memo
# file: memo
# owner: student
# group: student
user::rw-
group::rw-
other::r--
 
student@linux-ess:~$ setfacl -m u:teacher:rw memo
student@linux-ess:~$ setfacl -m g:it:rw memo
student@linux-ess:~$ ls -l memo
-rw-rw-r--+ 1 student student 0 Nov 11 14:15 memo
```

::: info ACL-indicator in ls -l
ACL's worden aangegeven door een `+` aan het einde van de rechtenpermissies in de uitvoer van `ls -l`.
:::

Met getfacl kunnen we de bestaande ACL's op een bestand of map controleren.

```bash
student@linux-ess:~$ getfacl memo
# file: memo
# owner: student
# group: student
user::rw-
user:teacher:rw-
group::rw-
group:it:rw-
mask::rw-
other::r--
```

 Om de gebruiker 'teacher' toegang te geven tot het bestand memo uit de homefolder van 'student' , moeten we enkele machtigingen bewerken. Een mogelijke oplossing zou zijn: setfacl -m u:teacher:rx /home/student. Nu kan de leraar de homefolder van de student openen en bekijken.

 In het vorige voorbeeld zien we ook een regel met de optie mask. Deze optie bepaalt de maximale machtiging en heeft ook voorrang op de reguliere bestandsmachtigingen, behalve voor de eigenaar van het bestand. We kunnen deze parameter als volgt toevoegen:

```bash
student@linux-ess:~$ setfacl -m m:r memo 
student@linux-ess:~$ getfacl memo 
# file: memo
# owner: student
# group: student
user::rw-
user:teacher:rw-                #effective:r--
group::rw-                      #effective:r--                      
group:it:rw-                    #effective:r--
mask::r--
other::r--

student@linux-ess:~$ ls -l memo
-rw-r--r--+ 1 student student 0 Nov 11 14:15 memo
```

 De mask is te zien als groepsrechten bij een ls -l. Merk ook op dat iedereen die in de groep student zit ook geen write-rechten meer heeft!

Als we een ACL-instelling uit het bestand willen verwijderen, kunnen we de optie -x gebruiken:

```bash
student@linux-ess:~$ setfacl -x g:it memo
student@linux-ess:~$ getfacl memo 
# file: memo
# owner: student
# group: student
user::rw-
user:teacher:rw-
group::rw-
mask::rw-
other::r-- 
 
student@linux-ess:~$ ls -l memo
-rw-rw-r--+ 1 student student 0 Nov 11 14:15 memo
```

 We zien hierboven dat de mask van het bestand memo terug op rw- staat. Dit komt omdat we een ACL hebben veranderd en de mask dan automatisch terug wordt gezet zodanig dat alle gebruikers-ACLs en groep-ACLs dan ook kunnen worden toegepast (user : teacher : rw-).

Als we alle ACL-instellingen uit een bestand willen verwijderen, kunnen we de optie -b gebruiken:

```bash
student@linux-ess:~$ setfacl -b memo
student@linux-ess:~$ getfacl memo 
# file: memo
# owner: student
# group: student
user::rw-
group::rw-
other::r--
 
student@linux-ess:~$ ls -l memo
-rw-rw-r-- 1 student student 0 Nov 11 14:15 memo
```

We kunnen ook default ACL's toevoegen door de parameter `d:` toe te voegen of de optie `-d` te gebruiken. De default-instelling zorgt ervoor dat nieuwe subbestanden en submappen dezelfde ACL's krijgen als de opgegeven map.

::: warning Machtigingen vereist voor default ACL's
Default ACL's werken alleen als de groep of gebruiker ook daadwerkelijk de machtigingen heeft om het respectievelijke bestand of de respectievelijke map aan te maken!
:::

```bash
student@linux-ess:~$ mkdir memos
student@linux-ess:~$ ls -ld memos
drwxrwxr-x 2 student student 4096 Nov 11 14:48 memos
student@linux-ess:~$ getfacl memos
# file: memos
# owner: student
# group: student
user::rwx
group::rwx
other::r-x
student@linux-ess:~$ setfacl -m g:it:rwx memos         # We moeten de groep ook rechtstreeks toevoegen aan de map, anders kan de groep niet in de folder geraken
student@linux-ess:~$ setfacl -m d:g:it:rwx memos       # of setfacl -d -m g:it:rwx memos
student@linux-ess:~$ getfacl memos
# file: memos
# owner: student
# group: student
user::rwx
group::rwx
group:it:rwx
other::r-x                 
default:user::rwx
default:group::rwx
default:group:it:rwx
default:mask::rwx
default:other::r-x
 
student@linux-ess:~$ mkdir memos/January
student@linux-ess:~$ getfacl memos/January/
# file: memos/January/
# owner: student
# group: student
user::rwx
group::rwx
group:it:rwx
mask::rwx
other::r-x
default:user::rwx
default:group::rwx
default:group:it:rwx
default:mask::rwx
default:other::r-x
 
student@linux-ess:~$ touch memos/January/24
student@linux-ess:~$ getfacl memos/January/24
# file: memos/January/24
# owner: student
# group: student
user::rw-
group::rwx                      #effective:rw-
group:it:rwx                    #effective:rw-
mask::rw-
other::r--
```