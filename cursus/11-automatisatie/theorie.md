# 11. Automatisatie


## Bash scripts
Scripting is een geweldige manier om eenvoudige taken of commandoreeksen te automatiseren. Stel je voor dat je een back-up wilt maken. Meestal betekent dit het maken van een 'tar'-archief van bepaalde bestanden en mappen, daarna dit 'tar'-bestand de juiste naam geven en vervolgens het 'tar'-bestand naar een bepaalde map verplaatsen. Het handmatig uitvoeren van deze commando's is gevoelig voor fouten en tijdrovend. Een betere manier zou zijn om deze commando's in een script te bundelen, zodat we in plaats daarvan één commando kunnen uitvoeren die alle hierboven beschreven stappen uitvoert.

In Linux gebruiken we vaak bash scripts. bash verwijst naar de standaard shell die we gebruiken als gebruiker in Ubuntu. Er zijn verschillende soorten shells maar dit valt buiten het bereik van deze cursus.

::: info Scope van dit hoofdstuk
We concentreren ons op de basissyntax van een shellscript. Meer geavanceerde onderwerpen zoals if statements, loops, opties en argumenten vallen buiten het bereik van deze cursus.
:::



### Hello world
Om te beginnen met ons eerste bash-script maken we een nieuw bestand met de naam helloworld.sh en voegen we wat inhoud toe met 'nano'.

```bash
student@linux-ess:~$ nano helloworld.sh
```

We geven het bestand de volgende inhoud:

```bash
#!/bin/bash
# Author: Linus Torvalds
echo "hello world"  # Print text to the screen
echo "this is our first bash script"
```

De eerste regel in dit script wordt de shebang genoemd en is een speciale regel die ervoor zorgt dat het script in een bash-shell wordt uitgevoerd. Daarna kunnen we verschillende regels van allerlei commando's hebben die in opeenvolgende volgorde worden uitgevoerd.

het gebruik van het # teken wordt geïnterpreteerd als het begin van commentaar. Resterende code op de lijn dat zich bevindt na dit teken wordt niet uitgevoerd.

In het bovenstaande voorbeeld zullen we 2 echo-commando's uitvoeren.

Om dit bash-script uit te voeren (zonder een interpreter te moeten opgeven), moeten we execute-rechten toevoegen:

```bash
student@linux-ess:~$ ls -l helloworld.sh
-rw-rw-r-- 1 student student 371 Nov 11 15:55 helloworld.sh
student@linux-ess:~$ chmod u+x helloworld.sh
student@linux-ess:~$ ls -l helloworld.sh
-rwxrw-r-- 1 student student 371 Nov 11 15:55 helloworld.sh
```

Hierna kunnen we het script uitvoeren (zonder een interpreter op te geven):

```bash
student@linux-ess:~$ ./helloworld.sh
hello world
this is our first bash script
```

Indien we het execute recht niet geven, maar wel leesrechten, dan kunnen we het script toch nog uitvoeren door de interpreter mee te geven:

```bash
student@linux-ess:~$ bash helloworld.sh
hello world
this is our first bash script
```

Hoewel het script zich in de huidige werkmap bevindt, moeten we het specificeren met: ./helloworld.sh Een andere manier om het uit te voeren, is door het volledige pad op te geven: /home/student/helloworld.sh

Alleen scripts die uitvoerbaar zijn en zijn opgeslagen in een map die is opgegeven in de variabele $PATH, kunnen worden uitgevoerd zonder het volledige pad op te geven.

### De variabele PATH
Linux heeft meerdere plaatsen waar binaire bestanden worden opgeslagen. Deze worden vaak gebundeld in de PATH-variabele.

Als we een opdracht uitvoeren zonder het pad op te geven waar de opdracht is opgeslagen, wordt er binnen elk pad van de variabele PATH gezocht naar deze opdracht.

```bash
student@linux-ess:~$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
```

::: info Paden gescheiden door dubbele punt
Elk pad in de `PATH`-variabele is van het volgende gescheiden door een dubbele punt (`:`).
:::

```bash
student@linux-ess:~$ echo $PATH | tr ':' '\n'
/usr/local/sbin
/usr/local/bin
/usr/sbin
/usr/bin
/sbin
/bin
/usr/games
/usr/local/games
/snap/bin
```

De variabele PATH wordt ingesteld en gewijzigd in meerdere scripts. Het begint met een systeembrede instelling in /etc/environment:

```bash
student@linux-ess:~$ cat /etc/environment
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin"  
student@linux-ess:~$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
```

We kunnen dit bestand dus wijzigen als we de PATH-variabele voor elke gebruiker op het systeem willen wijzigen. De wijziging is zichtbaar voor een gebruiker wanneer hij zich aanmeldt.

Maar als we de PATH-variabele voor één gebruiker willen wijzigen, kunnen we dit doen vanuit het bestand ~/.profile. De wijziging is zichtbaar voor een gebruiker wanneer hij zich aanmeldt:

```bash
student@linux-ess:~$ grep -C1 "HOME/bin" .profile
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi
```

::: tip ~/bin automatisch in PATH
De map `~/bin` wordt automatisch aan `PATH` toegevoegd als ze bestaat (zie `.profile`). Maak ze aan voor je eigen scripts — maar log daarna **opnieuw in** zodat de wijziging actief wordt.
:::

```bash
student@linux-ess:~$ mkdir bin
### logout & login ###
student@linux-ess:~$ echo $PATH
/home/student/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
```

Zoals we al hebben gezien kun je het commando which gebruiken om erachter te komen of het commando gevonden wordt en waar precies.

```bash
student@linux-ess:~$ which reboot
/usr/sbin/reboot
```

### Datum met shell embedding
Laten we ons script uitbreiden met wat handige logica om te gebruiken om een bepaald commando in een ander commando uit te voeren. We bewerken de inhoud van het script als volgt:

```bash
student@linux-ess:~$ nano helloworld.sh
```

Nieuwe inhoud van `helloworld.sh`:

```bash
#!/bin/bash
# Author: Linus Torvalds
echo "hello world"  # Print text to the screen
echo "this is our first bash script"
echo "the date of today is $(date)"
```

Wanneer we dit script uitvoeren, krijgen we de volgende uitvoer:

```bash
student@linux-ess:~$ ./helloworld.sh
hello world
this is our first bash script
the date of today is Tue Jun 28 22:04:09 CEST 2035
```

Het concept dat we hier hebben gebruikt, heet shell embedding. De $(...) syntaxis opent een nieuwe (sub)shell en voert een commando uit. De uitvoer van het date-commando wordt dan direct gebruikt in het echo commando.

Als je de datum liever in de Belgische notatie hebt, kan je onderstaande doen:

```bash
student@linux-ess:~$ locale -a
C
C.utf8
en_US.utf8
POSIX
student@linux-ess:~$ sudo locale-gen nl_BE.utf8
Generating locales (this might take a while)...
  nl_BE.UTF-8... done
Generation complete.
student@linux-ess:~$ locale -a
C
C.utf8
en_US.utf8
nl_BE.utf8
POSIX
student@linux-ess:~$ date
Tue Dec  3 08:35:51 AM UTC 2035
student@linux-ess:~$ LC_TIME=nl_BE.utf8 date
di 03 dec 2035 08:36:18 UTC
```

Indien je deze locale in de toekomst wilt behouden, kan je het onderstaande doen:

```bash
student@linux-ess:~$ sudo update-locale LC_TIME=nl_BE.UTF-8
student@linux-ess:~$ sudo reboot
```


### Variabelen
We kunnen ook gebruik maken van variabelen om data te hergebruiken:

```bash
student@linux-ess:~$ nano vars.sh
```

Inhoud van `vars.sh`:

```bash
#!/bin/bash
CUSTOMDIR=testdir
echo "customdir is set to $CUSTOMDIR"
mkdir ~/$CUSTOMDIR
touch ~/$CUSTOMDIR/testfile
ls -l ~/$CUSTOMDIR/*
```

We kunnen het script uitvoeren zonder eerst de uitvoerbit (chmod u+x) in te stellen, maar dan moeten we de interpreter (hier bash) specificeren om te definiëren in welke taal het script is geschreven

```bash
student@linux-ess:~$ bash vars.sh
customdir is set to testdir
-rw-r----- 1 student student 0 Nov 11 15:52 /home/student/testdir/testfile
```


### Systeemvariabelen
We kunnen ook gebruik maken van variabelen die op het systeem zijn ingesteld: nano sysvars.sh

```bash
#!/bin/bash
echo "hello $USER"
echo "your homefolder is $HOME"
```

Maak het uitvoerbaar en voer het uit:

```bash
student@linux-ess:~$ chmod u+x sysvars.sh
student@linux-ess:~$ ./sysvars.sh
hello student
your homefolder is /home/student
```

Laten we enkele van de dingen combineren die we tot nu toe hebben geleerd.

Laten we een nieuw script maken met de naam countfiles.sh:

```bash
student@linux-ess:~$ nano countfiles.sh
```

Inhoud van `countfiles.sh`:

```bash
#!/bin/bash
echo "hello $USER"
echo "your homefolder has $(ls -A1 ~ | wc -l) files/folders."
```

Wanneer we het uitvoeren, krijgen we het volgende resultaat:

```bash
student@linux-ess:~$ bash countfiles.sh
hello student
your homefolder has 12 files/folders.
```

In een ander voorbeeld wordt een bestand gemaakt met de huidige datum in de bestandsnaam:

```bash
student@linux-ess:~$ nano datefile.sh
```

Inhoud van `datefile.sh`:

```bash
#!/bin/bash
# Dit zal een variabele maken met de huidige datum als waarde
createdate=$(date +"%Y-%m-%d_%H:%M:%S")
touch ~/${createdate}-superfile && echo "File ${createdate}-superfile created/touched in homedir."
```

Wanneer we het uitvoeren, krijgen we het volgende resultaat:

```bash
student@linux-ess:~$ bash datefile.sh
File 2025-11-11_10:38:13-superfile created/touched in homedir.
```

::: warning Variabelesyntax met $ en accolades
Gebruik altijd een dollarteken voor een variabelenaam (`echo $createdate`). Als je tekst direct na de variabele plakt zonder spatie, **moet** je accolades gebruiken: `echo ${createdate}superfile`.
:::



### Gebruikersinvoer lezen
Soms kan het nuttig zijn om gebruikersinput te vragen. We plaatsen het antwoord van de gebruiker in een variabele, zodat we het later in het script kunnen hergebruiken: nano list5.sh

```bash
#!/bin/bash
echo "Geef het absolute pad van de map die je wilt controleren:"
read folder
echo "De geselecteerde map is $folder." 
```

Laten we dit script uitbreiden om het wat meer functionaliteit te geven en enkele van de concepten te combineren die we eerder hebben geleerd:

```bash
#!/bin/bash
echo "Geef het absolute pad van de map die je wil controleren:"
read folder
echo "De geselecteerde map is $folder. De map bevat $(ls -A1 $folder | wc -l) bestanden/mappen." 
echo "De eerste 5 worden getoond:"
ls -A1 $folder | head -5
```

Laten we eens kijken wat het doet:

```bash
student@linux-ess:~$ ./list5.sh
Enter Geef het absolute pad van de map die je wil controleren:
/home/student
De geselecteerde map is /home/student. De map bevat 23 bestanden/mappen.
De eerste 5 worden getoond:
2035-11-11-superfile
auth.log
.bash_history
.bash_logout
.bashrc
```

### Een parameter gebruiken
We gaan het simpel houden, dus we zullen niet meer dan negen parameters gebruiken. In ons voorbeeld zullen we er slechts twee gebruiken ($1 en $2), maar weet dat de methode hetzelfde blijft voor alle negen ($1 - $9). Als kanttekening kan ik je vertellen dat $0 ook bestaat en het commando bevat waarmee het script is uitgevoerd.

```bash
student@linux-ess:~$ nano params.sh
student@linux-ess:~$ cat params.sh
echo Param one is: $1
echo Param two is: $2
student@linux-ess:~$ chmod u+x params.sh
student@linux-ess:~$ ./params.sh first 2nd
Param one is: first
Param two is: 2nd
```

## At

### Eerst de tijdzone controleren
Indien de tijd een uur voorloopt betekent dit dat jouw tijdzone foutief is. Je kan dit oplossen met timedatectl:

```bash
student@linux-ess:~$ date
Tue 03 dec 2035 16:27:38 CET
student@linux-ess:~$ timedatectl
               Local time: Tue 2035-12-03 16:28:06 UTC
           Universal time: Tue 2035-12-03 16:28:06 UTC
                 RTC time: Tue 2035-12-03 16:28:05
                Time zone: Etc/UTC (UTC, +0000)
System clock synchronized: no
              NTP service: active
          RTC in local TZ: no
student@linux-ess:~$ sudo timedatectl set-timezone Europe/Brussels
student@linux-ess:~$ date
Tue 03 dec 2035 17:28:58 CET
student@linux-ess:~$ timedatectl
               Local time: Tue 2035-12-03 17:29:14 CET
           Universal time: Tue 2035-12-03 16:29:14 UTC
                 RTC time: Tue 2035-12-03 16:29:14
                Time zone: Europe/Brussels (CET, +0100)
System clock synchronized: yes
              NTP service: active
          RTC in local TZ: no
```

### Een taak plannen met at
Je kan het commando at gebruiken om een script/commando op een bepaald tijdstip uit te voeren. Is `at` nog niet geïnstalleerd, dan doe je eerst `sudo apt install at`.

Voor het at-commando echoën we een uitvoer in het at-commando zoals getoond in onderstaand voorbeeld:

```bash
student@linux-ess:~$ echo ./datefile.sh | at 14:00
warning: commands will be executed using /bin/sh
job 1 at Sat Nov 12 14:00:00 2035
student@linux-ess:~$ echo 'echo "hello world" > /tmp/hello.txt' | at now + 1 minutes
warning: commands will be executed using /bin/sh
job 2 at Mon Nov 14 10:36:00 2035
student@linux-ess:~$ at -l
2       Mon Nov 14 10:36:00 2035 a student
1       Sat Nov 12 14:00:00 2035 a student
```

Je kan controleren wat er is gepland met de commando's atq of at -l en verwijderen wanneer dat nodig is met de commando's atrm, at -d of at -r:

```bash
student@linux-ess:~$ at -l
2       Mon Nov 14 10:36:00 2035 a student
1       Sat Nov 12 14:00:00 2035 a student
student@linux-ess:~$ at -d 2
student@linux-ess:~$ at -l
1       Sat Nov 12 14:00:00 2035 a student
```

Je kan controleren welk commando je meegegeven hebt met at -c:

```bash
student@linux-ess:~$ at -l
1       Sat Nov 12 14:00:00 2035 a student
student@linux-ess:~$ at -c 1
 
#!/bin/sh
# atrun uid=1000 gid=1000
...
cd /home/student || {
         echo 'Execution directory inaccessible' >&2
         exit 1
}
/home/student/bin/datefile.sh

```

Kijk voor meer info in de manpage van 'at'.



## Crontab
Met het cron commando is het mogelijk om je scripts/commando's te plannen om op regelmatige basis te draaien. Cron werkt anders, het maakt gebruik van een bestand waarin we de commando's/scripts plaatsen die we willen uitvoeren en specificeren wanneer de runs moeten gebeuren. Om je crontab-bestand te openen geef je het commando crontab -e.

In het onderstaande voorbeeld gaan we elke minuut wat tekst naar een bestand echoën.

```bash
.---------------- minute (0 - 59)  
|  .------------- hour (0 - 23)  
|  |  .---------- day of month (1 - 31)  
|  |  |  .------- month (1 - 12) OF jan,feb,mar,apr ...  
|  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OF sun,mon,tue,wed,thu,fri,sat  
|  |  |  |  |  
*  *  *  *  *   echo Command ran on $(date) >> /tmp/crontest  
```

Verwijder gewoon de lijn van de crontab-file om dit te stoppen. Kijk voor meer info in de manpage van cron.

::: info Editor kiezen bij eerste gebruik van crontab
De eerste keer dat je `crontab -e` opent, wordt gevraagd welke editor je wilt gebruiken. Kies optie `1` voor nano — de eenvoudigste keuze.
:::

```bash
student@linux-ess:~$ crontab -e
no crontab for student - using an empty one
 
Select an editor.  To change later, run 'select-editor'.
  1. /bin/nano        <---- easiest
  2. /usr/bin/vim.tiny
  3. /bin/ed
 
Choose 1-3 [1]: 1
crontab: installing new crontab
...
# m h  dom mon dow   command
* * * * * echo Command ran on $(date) >> /tmp/crontest
 
student@linux-ess:~$ crontab -l
...
# m h  dom mon dow   command
* * * * * echo Command ran on $(date) >> /tmp/crontest
 
student@linux-ess:~$ cat /tmp/crontest
Command ran on Sat Nov 12 11:02:01 AM UTC 2035
Command ran on Sat Nov 12 11:03:01 AM UTC 2035
Command ran on Sat Nov 12 11:04:01 AM UTC 2035
```

Als we een script moeten uitvoeren als een andere gebruiker of met verhoogde rechten (als root), kunnen we gebruik maken van het algemene crontab bestand in /etc. In dit bestand is er een extra kolom om de gebruiker aan te geven waaronder het script moet worden uitgevoerd.

Je hebt verhoogde rechten nodig om dit bestand te bewerken (sudo).

In het volgende voorbeeld zullen we elke vrijdag om 23:30 een back-up script uitvoeren:

```bash
student@linux-ess:~$ sudo nano /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.
 
SHELL=/bin/sh
# You can also override PATH, but by default, newer versions inherit it from the environment
#PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
 
# Example of job definition:
#.---------------- minute (0 - 59)
#|  .------------- hour (0 - 23)
#|  |  .---------- day of month (1 - 31)
#|  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
#|  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
#|  |  |  |  |
#*  *  *  *  * user-name command to be executed
17  *  *  *  *   root    cd / && run-parts --report /etc/cron.hourly
25  6  *  *  *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47  6  *  *  7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52  6  1  *  *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
30 23  *  *  5   root    /scripts/backuphomefolders.sh
```

::: info cron.daily / cron.weekly / cron.monthly
De mappen `cron.daily`, `cron.weekly` en `cron.monthly` kunnen scripts bevatten die automatisch door cron worden uitgevoerd op de respectieve tijdstippen.
:::

```bash
student@linux-ess:~$ ls /etc/cron.daily/
apport  apt-compat  dpkg  logrotate  man-db
```

In Linux wordt het systeem beheerd met systemd. En systemd heeft ook een implementatie voor het herhalen van taken, namelijk timers. Maar dat valt buiten het bestek van deze cursus.