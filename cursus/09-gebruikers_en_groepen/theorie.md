# 09. Gebruikers en groepen

Een Linux-systeem is een systeem voor **meerdere gebruikers**. Elke gebruiker heeft een eigen account, een eigen homefolder en eigen rechten. In dit hoofdstuk leer je gebruikers en groepen aanmaken, aanpassen en verwijderen.

We werken momenteel als de gebruiker `student`. Dat bevestig je met `whoami`. Wie er nog meer is ingelogd, zie je met `who`, `users` of `w`. Elk commando toont iets anders:

```bash
student@linux-ess:~$ whoami     # welke gebruiker ben ik?
student@linux-ess:~$ who        # wie is ingelogd, op welke terminal en sinds wanneer?
student@linux-ess:~$ users      # alleen de namen van de ingelogde gebruikers
student@linux-ess:~$ w          # wie is ingelogd en wat doen ze op dit moment?
```

## Gebruikersbeheer

### /etc/passwd
Zoals we eerder zagen, staat de systeemconfiguratie in configuratiebestanden. Dat geldt ook voor gebruikers: ze staan in het bestand `/etc/passwd`. Elke regel is één account, met velden gescheiden door dubbele punten:

```bash
student@linux-ess:~$ tail /etc/passwd
pollinate:x:105:1::/var/cache/pollinate:/bin/false
sshd:x:106:65534::/run/sshd:/usr/sbin/nologin
syslog:x:107:113::/home/syslog:/usr/sbin/nologin
uuidd:x:108:114::/run/uuidd:/usr/sbin/nologin
tcpdump:x:109:115::/nonexistent:/usr/sbin/nologin
tss:x:110:116:TPM software stack,,,:/var/lib/tpm:/bin/false
landscape:x:111:117::/var/lib/landscape:/usr/sbin/nologin
usbmux:x:112:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
student:x:1000:1000:student:/home/student:/bin/bash
lxd:x:999:100::/var/snap/lxd/common/lxd:/bin/false
```

Het eerste account is het root-account:

```bash
student@linux-ess:~$ head -1 /etc/passwd
root:x:0:0:root:/root:/bin/bash
```

De regel van `student` bestaat uit zeven velden:

| Veld | Voorbeeld | Betekenis |
|---|---|---|
| 1 | `student` | gebruikersnaam |
| 2 | `x` | het wachtwoord staat niet hier, maar in `/etc/shadow` |
| 3 | `1000` | gebruikers-id (**UID**) |
| 4 | `1000` | id van de **primaire groep** (**GID**) |
| 5 | `student` | commentaar (vaak de volledige naam) |
| 6 | `/home/student` | homefolder |
| 7 | `/bin/bash` | standaardshell |

Meer informatie vind je met `man 5 passwd`.

### Gebruikers toevoegen (useradd)
Een gebruiker maak je aan met `useradd`. Dit systeembeheercommando moet je met `sudo` uitvoeren. Zo maak je de gebruiker `teacher` aan:

```bash
student@linux-ess:~$ sudo useradd -m -d /home/teacher -c "Teacher Account" teacher
[sudo] password for student:
student@linux-ess:~$ tail -3 /etc/passwd
student:x:1000:1000:student:/home/student:/bin/bash
lxd:x:999:100::/var/snap/lxd/common/lxd:/bin/false
teacher:x:1001:1001:Teacher Account:/home/teacher:/bin/sh
```

| Optie | Betekenis |
|---|---|
| `-m` | maak de homefolder ook echt aan (met de juiste rechten) |
| `-d pad` | pad van de homefolder |
| `-c "tekst"` | commentaarveld |

::: info -d is optioneel
Zonder `-d` wordt de homefolder `/home/<gebruikersnaam>`.
:::

`teacher` krijgt als shell `/bin/sh`. Dat is de standaardwaarde van `useradd` (zie *Standaardwaarden* hieronder). Het wachtwoord stellen we later in.

Zoals je ziet in `/etc/passwd` en in de map `/home`, bestaat de gebruiker nu:

```bash
student@linux-ess:~$ tail -1 /etc/passwd
teacher:x:1001:1001:Teacher Account:/home/teacher:/bin/sh
student@linux-ess:~$ ls -l /home
total 8
drwxr-x--- 5 student student 4096 Nov  4 16:04 student
drwxr-x--- 2 teacher teacher 4096 Nov  7 20:28 teacher
```

Elke gebruiker heeft een gebruikers-id (het derde veld in `/etc/passwd`). Die en de groepen bekijk je met `id`:

```bash
student@linux-ess:~$ id teacher     # uid, primaire groep (gid) en alle groepen
uid=1001(teacher) gid=1001(teacher) groups=1001(teacher)
```

### Standaardwaarden
`useradd` gebruikt standaardwaarden. Die bekijk je met:

```bash
student@linux-ess:~$ useradd -D     # standaardwaarden tonen
GROUP=100
HOME=/home
INACTIVE=-1
EXPIRE=
SHELL=/bin/sh
SKEL=/etc/skel
CREATE_MAIL_SPOOL=no
```

Ze staan in `/etc/default/useradd`. Je past ze aan door dat bestand te bewerken of met `useradd -D <optie>`.

::: tip Standaardshell wijzigen naar bash
De standaardshell is `/bin/sh`. Zet dit op `/bin/bash`, zodat elke nieuwe gebruiker bash krijgt:
```bash
sudo useradd -D --shell /bin/bash     # nieuwe standaardshell voor alle volgende gebruikers
```
:::

### /etc/skel
Homefolders worden standaard aangemaakt onder `/home`. Ze beginnen niet leeg: de inhoud van `/etc/skel` (*skeleton*) wordt naar elke **nieuwe** homefolder gekopieerd. Zet je dus iets in `/etc/skel`, dan krijgt elke gebruiker die je daarna aanmaakt het ook.

```bash
student@linux-ess:~$ ls -a /etc/skel
.  ..  .bash_logout  .bashrc  .profile
student@linux-ess:~$ sudo ls -a /home/teacher/
.  ..  .bash_logout  .bashrc  .profile
```

### Standaard profielbestanden
* `.bashrc`: wordt uitgevoerd telkens wanneer een nieuwe shell (bash) start
* `.bash_logout`: wordt uitgevoerd wanneer de gebruiker uitlogt (wist het scherm)
* `.profile`: wordt uitgevoerd wanneer de gebruiker inlogt

### Gebruikers bewerken en verwijderen (usermod & userdel)
Met `usermod` pas je een bestaand account aan. Zo wijzig je het commentaarveld:

```bash
student@linux-ess:~$ grep student /etc/passwd
student:x:1000:1000:student:/home/student:/bin/bash
student@linux-ess:~$ sudo usermod -c "Student Account" student     # commentaarveld wijzigen
student@linux-ess:~$ grep student /etc/passwd
student:x:1000:1000:Student Account:/home/student:/bin/bash
```

En zo wijzig je de shell van een gebruiker:

```bash
student@linux-ess:~$ tail -3 /etc/passwd
student:x:1000:1000:Student Account:/home/student:/bin/bash
lxd:x:999:100::/var/snap/lxd/common/lxd:/bin/false
teacher:x:1001:1001:Teacher Account:/home/teacher:/bin/sh
student@linux-ess:~$ sudo usermod -s /bin/bash teacher     # shell wijzigen
student@linux-ess:~$ tail -3 /etc/passwd
student:x:1000:1000:Student Account:/home/student:/bin/bash
lxd:x:999:100::/var/snap/lxd/common/lxd:/bin/false
teacher:x:1001:1001:Teacher Account:/home/teacher:/bin/bash
```

Alle opties staan in `man usermod`.

Een gebruiker verwijder je met `userdel`:

```bash
student@linux-ess:~$ sudo userdel -r teacher     # -r verwijdert ook de homefolder
```

Voer dit nu nog niet uit: we gebruiken `teacher` verder in dit hoofdstuk.

::: warning Zonder -r blijft de homefolder staan
`userdel teacher` verwijdert alleen het account. De homefolder en de bestanden erin blijven achter.
:::

**Een account waarmee je niet kan inloggen:** zet de shell op `/usr/sbin/nologin` of `/bin/false`. Het verschil: `nologin` toont eerst een vriendelijk bericht dat inloggen niet kan, `false` sluit meteen af zonder iets te zeggen.

### Gebruikerswachtwoorden instellen
Je eigen wachtwoord wijzig je met `passwd` (zonder `sudo`):

```bash
student@linux-ess:~$ passwd
Changing password for student.
Current password:
New password:
Retype new password:
passwd: password updated successfully
```

::: info Wachtwoordvereisten
Je wachtwoord moet lang en complex genoeg zijn, anders wordt het niet aanvaard.
:::

::: warning sudo passwd wijzigt het root-wachtwoord
`sudo passwd` zonder gebruikersnaam wijzigt het wachtwoord van **root**, niet dat van jezelf!
:::

We maakten `teacher` aan zonder wachtwoord. Dat stel je in met `passwd` met `sudo` en de gebruikersnaam als argument:

```bash
student@linux-ess:~$ sudo passwd teacher     # wachtwoord van teacher instellen
New password:
Retype new password:
passwd: password updated successfully
```

Wachtwoorden staan om veiligheidsredenen in `/etc/shadow`. Gewone gebruikers kunnen dat bestand niet lezen:

```bash
student@linux-ess:~$ tail -1 /etc/shadow
tail: cannot open '/etc/shadow' for reading: Permission denied
student@linux-ess:~$ sudo tail -1 /etc/shadow
teacher:$y$j9T$Vtf.U//c4/N/CB8LzHfnl0$5iCgijrpqXfaA3v18w/nAL2rl8BmiBYX5rn5rf.j6B7:19171:0:99999:7:::
```

Het wachtwoord staat er niet leesbaar, maar als **hash** (een eenrichtings-versleuteling). Het begin van de hash zegt welk algoritme gebruikt werd: `$y$` is **yescrypt**, de standaard op Ubuntu. Andere voorkomende voorbeelden zijn `$6$` (sha512) en `$5$` (sha256).

### Veranderen van gebruiker (su)
Uitloggen doe je met `logout` of `exit`. Je kan daarna inloggen als een andere gebruiker. Met `su` (*substitute user*) werk je tijdelijk als een andere gebruiker:

```bash
student@linux-ess:~$ whoami; pwd
student
/home/student
student@linux-ess:~$ su - teacher     # werk als teacher (wachtwoord van teacher nodig)
Password:
teacher@linux-ess:~$ whoami; pwd
teacher
/home/teacher
teacher@linux-ess:~$ exit             # terug naar student
logout
student@linux-ess:~$ whoami; pwd
student
/home/student
```

Root kan elke gebruiker worden **zonder** diens wachtwoord te kennen:

```bash
student@linux-ess:~$ sudo su - teacher     # als root naar teacher, geen wachtwoord van teacher nodig
teacher@linux-ess:~$ whoami; pwd
teacher
/home/teacher
teacher@linux-ess:~$ exit
logout
```

::: tip sudo su voor root zonder wachtwoord
Om root te worden zonder het root-wachtwoord te kennen, gebruik je `sudo su -`:
:::

```bash
student@linux-ess:~$ sudo su - root     # root worden met je eigen wachtwoord
root@linux-ess:~# whoami
root
root@linux-ess:~# pwd
/root
root@linux-ess:~# exit
logout
```

Wees voorzichtig met commando's als root. Root kan alle bestanden, mappen en services van het systeem aanpassen, dus een fout of misbruik kan grote gevolgen hebben.

::: info su - vs su
Met de min (`-`) laadt `su` het profiel van de nieuwe gebruiker en kom je in zijn homefolder terecht. Zonder min krijg je wel de rechten van de nieuwe gebruiker, maar blijf je in de huidige map en wordt het profiel **niet** geladen.
:::

```bash
student@linux-ess:~$ sudo su root          # zonder min: je blijft in /home/student
root@linux-ess:/home/student# whoami; pwd
root
/home/student
root@linux-ess:/home/student# exit
exit
student@linux-ess:~$ sudo su - root        # met min: je komt in /root
root@linux-ess:~# whoami; pwd
root
/root
root@linux-ess:~# exit
logout
```

## Groepsmanagement
Groepen laten toe om rechten aan **meerdere gebruikers tegelijk** te geven. Elke gebruiker heeft één **primaire groep** en kan lid zijn van nul of meer **extra groepen**.

### Groepsinfo van een gebruiker bekijken (id, groups)
De groepen van een gebruiker bekijk je met `id` en `groups`:

```bash
student@linux-ess:~$ id student         # uid, primaire groep (gid) en alle groepen, met nummers
uid=1000(student) gid=1000(student) groups=1000(student),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd)
student@linux-ess:~$ groups student     # alleen de groepsnamen
student : student adm cdrom sudo dip plugdev lxd
```

### /etc/group
De groepen staan in `/etc/group`. Je kan dat bestand ook rechtstreeks bewerken in plaats van commando's te gebruiken.

```bash
student@linux-ess:~$ grep student /etc/group
adm:x:4:syslog,student
cdrom:x:24:student
sudo:x:27:student
dip:x:30:student
plugdev:x:46:student
lxd:x:110:student
student:x:1000:
```

Elke regel heeft vier velden: `groepsnaam : x : GID : leden`. De leden zijn gescheiden door een komma. Bij `student:x:1000:` is de lijst leeg: `student` is lid via zijn **primaire** groep (veld 4 in `/etc/passwd`), die hier niet wordt herhaald.

### Groepen toevoegen (groupadd)
Een nieuwe groep maak je met `groupadd`:

```bash
student@linux-ess:~$ sudo groupadd ict     # groep ict aanmaken
student@linux-ess:~$ tail -3 /etc/group
student:x:1000:
teacher:x:1001:
ict:x:1002:
```

Een groep verwijder je met `groupdel`.

### Groepen bewerken (groupmod)
Met `groupmod` wijzig je een groep, bijvoorbeeld de naam:

```bash
student@linux-ess:~$ sudo groupmod -n it ict     # groep ict hernoemen naar it
student@linux-ess:~$ tail -3 /etc/group
student:x:1000:
teacher:x:1001:
it:x:1002:
```

### Groepslidmaatschappen bewerken (usermod & deluser)
Een gebruiker voeg je toe aan een extra groep met `usermod`:

```bash
student@linux-ess:~$ sudo usermod -a -G it teacher     # -a: toevoegen aan de extra groep it
student@linux-ess:~$ id teacher
uid=1001(teacher) gid=1001(teacher) groups=1001(teacher),1002(it)
student@linux-ess:~$ groups teacher
teacher : teacher it
student@linux-ess:~$ grep it /etc/group
it:x:1002:teacher
```

::: warning Vergeet de optie -a niet
Zonder `-a` (*append*) wordt de gebruiker **enkel** lid van de opgegeven extra groep en uit **alle andere extra groepen** verwijderd. Dat is een ernstig probleem als de gebruiker de enige in de groep `sudo` was!
:::

Een gebruiker verwijderen uit een extra groep kan op meerdere manieren:

- `usermod -G` **zonder** `-a`, met alle extra groepen waarin hij moet blijven
- het bestand `/etc/group` met de hand bewerken en de gebruikersnaam uit de ledenlijst halen
- `usermod -r -G <groep> <gebruiker>`:

```bash 
student@linux-ess:~$ sudo usermod -r -G it teacher     # -r: verwijderen uit de extra groep it
student@linux-ess:~$ id teacher
uid=1001(teacher) gid=1001(teacher) groups=1001(teacher)
student@linux-ess:~$ grep it /etc/group
it:x:1002:
```

- `deluser <gebruiker> <groep>` (alleen op Debian-gebaseerde distributies zoals Ubuntu):

```bash
student@linux-ess:~$ sudo deluser teacher it     # teacher uit de groep it halen
student@linux-ess:~$ id teacher
uid=1001(teacher) gid=1001(teacher) groups=1001(teacher)
student@linux-ess:~$ grep it /etc/group
it:x:1002:
```

### Primaire groep en extra groepen
De **primaire groep** van een gebruiker staat in `/etc/passwd`. Nieuwe bestanden en mappen van die gebruiker krijgen die groep als groepseigenaar.

Een wijziging van het groepslidmaatschap geldt pas bij de **volgende login**. Een lopende sessie behoudt de groepen waarmee ze gestart is.

In het voorbeeld hieronder wijzigen we de primaire groep van `student` naar `it`:

* `grep` en `id student` tonen meteen de nieuwe groep, want ze lezen de configuratie.
* `id` en `groups` zonder naam tonen wat **onze lopende sessie** nog gebruikt: de oude groep.
* Een nieuw bestand (`test`) krijgt daarom nog de oude primaire groep `student`.

```bash
student@linux-ess:~$ grep student /etc/passwd
student:x:1000:1000:Student Account:/home/student:/bin/bash
student@linux-ess:~$ id
uid=1000(student) gid=1000(student) groups=1000(student),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd)
student@linux-ess:~$ ls -l
total 16
drwxr-xr-x 5 student student 4096 Nov  9 15:04 Documents
drwxr-xr-x 2 student student 4096 Oct 28 14:54 Downloads
drwxr-xr-x 6 student student 4096 Oct 23 12:22 linuscraft
drwx------ 5 student student 4096 Oct 19 15:07 snap
student@linux-ess:~$ sudo usermod -g it student     # primaire groep wijzigen naar it
[sudo] password for student:
student@linux-ess:~$ grep student /etc/passwd       # de configuratie is meteen aangepast
student:x:1000:1999:Student Account:/home/student:/bin/bash
student@linux-ess:~$ id student                     # toont de configuratie: nieuwe groep
uid=1000(student) gid=1999(it) groups=1999(it),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd)
student@linux-ess:~$ id                             # toont onze sessie: nog de oude groep
uid=1000(student) gid=1000(student) groups=1000(student),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd)
student@linux-ess:~$ groups student
student : it adm cdrom sudo dip plugdev lxd
student@linux-ess:~$ groups
student adm cdrom sudo dip plugdev lxd
student@linux-ess:~$ ls -l                          # usermod -g heeft de bestanden in de homefolder aangepast
total 16
drwxr-xr-x 5 student it 4096 Nov  9 15:04 Documents
drwxr-xr-x 2 student it 4096 Oct 28 14:54 Downloads
drwxr-xr-x 6 student it 4096 Oct 23 12:22 linuscraft
drwx------ 5 student it 4096 Oct 19 15:07 snap
student@linux-ess:~$ touch test                     # nieuw bestand: nog de oude primaire groep
student@linux-ess:~$ ls -l
total 16
drwxr-xr-x 5 student it      4096 Nov  9 15:04 Documents
drwxr-xr-x 2 student it      4096 Oct 28 14:54 Downloads
drwxr-xr-x 6 student it      4096 Oct 23 12:22 linuscraft
drwx------ 5 student it      4096 Oct 19 15:07 snap
-rw-r--r-- 1 student student    0 Nov 18 14:02 test
```

`usermod -g` heeft dus de bestaande bestanden in de homefolder meegenomen naar de nieuwe groep, maar het nieuwe bestand `test` kreeg nog de oude groep. Pas na uitloggen en opnieuw inloggen gebruikt de sessie de nieuwe groep:

```bash
ssh student@ip-address                  # opnieuw inloggen
student@linux-ess:~$ touch test2        # nieuw bestand: nu de nieuwe primaire groep
student@linux-ess:~$ ls -l
total 16
drwxr-xr-x 5 student it      4096 Nov  9 15:04 Documents
drwxr-xr-x 2 student it      4096 Oct 28 14:54 Downloads
drwxr-xr-x 6 student it      4096 Oct 23 12:22 linuscraft
drwx------ 5 student it      4096 Oct 19 15:07 snap
-rw-r--r-- 1 student student    0 Nov 18 14:02 test
-rw-r--r-- 1 student it         0 Nov 18 14:04 test2
student@linux-ess:~$ groups
it adm cdrom sudo dip plugdev lxd
student@linux-ess:~$ id
uid=1000(student) gid=1999(it) groups=1999(it),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd)
```

Het bestand `test` met de oude groep corrigeer je in het hoofdstuk over rechten met `chgrp`.
