# Oefeningen op Automatisatie

## Oefening 1

Maak een map met de naam `bin` in je thuismap.

::: details Oplossing tonen
```bash
mkdir ~/bin
```
:::

## Oefening 2

Log uit en log weer in. Dit zorgt ervoor dat de map `bin` is toegevoegd aan de variabele `PATH`. Weet je ook waarom de map aan de variabele `PATH` is toegevoegd? (Hint: `.profile`)

```
student@linux-ess:~$ echo $PATH
/home/student/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
```

::: details Oplossing tonen
```bash
echo "$PATH"
```

De reden staat in `~/.profile`: als de map `~/bin` bestaat, wordt ze automatisch aan `PATH` toegevoegd:

```bash
grep -C1 "HOME/bin" ~/.profile
```

```
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi
```
:::

## Oefening 3

Maak een script genaamd `show.sh` dat vraagt om een pad naar een map. Probeer de gebruikersnaam bij de vraag te betrekken (zie het voorbeeld). Gebruik het commando `env` om te zoeken naar de juiste systeemvariabele.

Toon een lijst met alle bestanden in de gegeven map.

Maak het script uitvoerbaar en controleer of het werkt.

Voorbeeld:
```
student@linux-ess:~/bin$ show.sh
Beste student, geef aub een map op:
/etc/ssl
certs  openssl.cnf  private
```

::: details Oplossing tonen
```bash
nano ~/bin/show.sh
```

```bash
#!/bin/bash
echo "Beste $USER, geef aub een map op:"
read dir
ls "$dir"
```

```bash
chmod +x ~/bin/show.sh
show.sh
```
:::

## Oefening 4

Wijzig het vorige script. Zoek in de manpage van `echo` hoe je de cursor achter de vraag kunt houden.

Voorbeeld:
```
student@linux-ess:~/bin$ show.sh
Beste student, geef aub een map op: /etc/ssl
certs  openssl.cnf  private
```

::: details Oplossing tonen
```bash
nano ~/bin/show.sh
```

```bash
#!/bin/bash
echo -n "Beste $USER, geef aub een map op: "
read dir
ls "$dir"
```
:::

## Oefening 5

Wijzig het vorige script. Vang drie parameters op in het script en voeg deze toe aan het commando `ls`. Test het script met de parameters `-l`, `-a` en `-h`.

Voorbeeld:
```
student@linux-ess:~/bin$ show.sh -l -a -h
Beste student, geef aub een map op: /etc/ssl
total 44K
drwxr-xr-x  4 root root 4.0K Nov  4 14:19 .
drwxr-xr-x 97 root root 4.0K Nov 12 13:41 ..
drwxr-xr-x  2 root root  16K Aug  9 11:58 certs
-rw-r--r--  1 root root  13K Jul  4 11:20 openssl.cnf
drwx------  2 root root 4.0K Jul  4 11:20 private
```

::: details Oplossing tonen
```bash
nano ~/bin/show.sh
```

```bash
#!/bin/bash
echo -n "Beste $USER, geef aub een map op: "
read dir
ls $1 $2 $3 "$dir"
```
:::

## Oefening 6

Probeer het script uit te voeren terwijl je je in een andere map bevindt dan de `bin`-map. Werkt het door alleen de naam op te geven (zonder pad)?

Maak een nieuwe map `myscripts` in je thuismap. Verplaats `show.sh` naar `myscripts`. Probeer het script opnieuw uit te voeren vanuit een andere map. Werkt het? Los dit op door het pad toe te voegen aan de juiste variabele en zorg ervoor dat dit pad ook na een herstart gekend is. Log uit en opnieuw in om te testen. Gebruik ook het commando `which` om te controleren of het werkt.

::: details Oplossing tonen
```bash
mkdir ~/myscripts
mv ~/bin/show.sh ~/myscripts/
```

```bash
echo 'PATH="$PATH:$HOME/myscripts"' >> ~/.profile
```

```bash
# log uit en opnieuw in, of:
source ~/.profile
which show.sh    # toont: /home/student/myscripts/show.sh
```
:::

## Oefening 7

Wijzig het vorige script. Druk eerst de huidige datum af in de notatie zoals in het voorbeeld. Zoek in de manpage van `date` om het juiste formaat te vinden.

Voorbeeld:
```
student@linux-ess:~/myscripts$ show.sh
Saturday, 12 November 2022
Beste student, geef aub een map op: /
bin   dev  home  lib32  libx32      media  opt   root  sbin  srv       sys  usr
boot  etc  lib   lib64  lost+found  mnt    proc  run   snap  swap.img  tmp  var
```

::: details Oplossing tonen
```bash
nano ~/myscripts/show.sh
```

```bash
#!/bin/bash
date +"%A, %d %B %Y"
echo -n "Beste $USER, geef aub een map op: "
read dir
ls $1 $2 $3 "$dir"
```
:::

## Oefening 8

Maak een taak die binnen vijf minuten éénmalig zal uitvoeren. De taak moet een overzicht van alle ingelogde gebruikers opslaan in het bestand `/tmp/userlist`. Log, naast de huidige ssh-verbinding met de server, ook in op de server zelf. Bekijk na 5 minuten het bestand `/tmp/userlist`.

Voorbeeld:
```
student@linux-ess:~/myscripts$ cat /tmp/userlist
 17:10:15 up 14:42,  2 users,  load average: 0.20, 0.16, 0.10
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
student  tty1     -                17:08    2:13   0.11s  0.05s -bash
student  pts/0    192.168.75.1     15:04    7.00s  0.25s  0.02s w
```

::: details Oplossing tonen
```bash
echo 'w > /tmp/userlist' | at now + 5 minutes
```

```bash
# controleer na 5 minuten:
cat /tmp/userlist
```

**Werkt het niet?** Controleer of de `atd` service actief is:
```bash
sudo systemctl status atd
```
:::

## Oefening 9

Maak een persoonlijke cronjob die bij elke herstart de tekst `Herstart om` gevolgd door de datum en tijd opslaat in het bestand `~/rebootlog`. Doorzoek de manpage van het crontab-bestand (sectie *File Format*) en zoek naar de tekst `reboot`.

::: tip
Als je `date` formatteert in crontab: het `%`-teken heeft een speciale betekenis in crontab. Je moet dit escapen met een backslash (`\%`).
:::

::: details Oplossing tonen
```bash
crontab -e
```

Voeg toe:
```
@reboot echo Herstart om $(date +"\%F \%T") >> $HOME/rebootlog
```
:::

## Oefening 10

Maak een cronjob die elke zondag om 23:59 een back-up maakt van alle homefolders (reguliere gebruikers én root) naar de map `/backups`. Sla de back-up op als `/backups/homefolders.tar.gz`. Maak een script voor de taak en plaats het in `/scripts`.

::: tip
Om de cronjob te testen, pas je de tijd en dag-van-de-week tijdelijk aan naar precies 1 minuut in de toekomst. Wacht een minuut en controleer of de tarball bestaat.
:::

::: details Oplossing tonen
```bash
sudo mkdir /scripts /backups
sudo nano /scripts/backuphomefolders.sh
```

```bash
#!/bin/bash
tar -czf /backups/homefolders.tar.gz /home /root
```

```bash
sudo chmod a+x /scripts/backuphomefolders.sh
```

Voeg toe aan `/etc/crontab`:
```bash
echo '59 23 * * 0  root  /scripts/backuphomefolders.sh' | sudo tee -a /etc/crontab
```

Test:
```bash
ls -lh /backups/homefolders.tar.gz
tar -tzf /backups/homefolders.tar.gz
```
:::
