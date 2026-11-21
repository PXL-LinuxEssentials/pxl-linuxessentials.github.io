# 08. Filters

## Filters en bestandsbewerkingen
Bij het werken met (tekst)bestanden willen we vaak bewerkingen uitvoeren om de inhoud van het bestand te manipuleren om een specifieke uitvoer te krijgen.

Bijvoorbeeld: We hebben een enorm logbestand dat alle login pogingen voor onze applicatie registreert waaronder de gebruikersnamen, ip-adressen, tijdstempels, locatie, ISP-info, metadata, ... Misschien willen we snel alle onjuiste aanmeldingsadressen van gebruiker X opzoeken en zien vanaf welke IP-adressen hij verbinding maakte. We zouden het bestand regel voor regel handmatig kunnen doorlopen om het te controleren, maar vaak is dat proces lang en vervelend. Wat we willen doen, is commando's gebruiken om de gegevens te filteren, manipuleren en structureren tot het gewenste resultaat. Om dit te doen, kunnen we een brede set filter- en structuurcommando's gebruiken die we aan elkaar kunnen koppelen met behulp van pipes.

Voor de voorbeelden in dit hoofdstuk gebruiken we een logbestand gevuld met gegevens. Om dit bestand te downloaden, kan je het volgende commando uitvoeren:

```bash
student@linux-ess:~$ wget https://vwgert.github.io/data/auth.log
--2024-10-31 11:09:32--  https://vwgert.github.io/data/auth.log
Resolving vwgert.github.io (vwgert.github.io)... 185.199.110.153, 185.199.108.153, 185.199.109.153, ...
Connecting to vwgert.github.io (vwgert.github.io)|185.199.110.153|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1730 (1.7K) [text/plain]
Saving to: ‘auth.log’
 
auth.log                      100%[=================================================>]   1.69K  --.-KB/s    in 0s
 
2024-10-31 11:09:32 (32.0 MB/s) - ‘auth.log’ saved [1730/1730]
student@linux-ess:~$ cat auth.log
Jun 09 11:11:11 linux-ess: Server listening on 0.0.0.0 port 22.
Jun 09 11:11:11 linux-ess: Server listening on :: port 22.
Jun 09 12:32:24 linux-ess: Accepted publickey for: johndoe from 85.245.107.42 port 54259 ssh2: RSA SHA256:K18kPGZrTiz7g
Jun 10 21:38:01 linux-ess: Failed password for: student from 192.168.0.1 port 37362 ssh2
Jun 10 21:39:01 linux-ess: Failed password for: johndoe from 192.168.0.2 port 37849 ssh2
Jun 10 21:42:01 linux-ess: Accepted password for: student from 84.298.138.41 port 48785 ssh2
Jun 14 14:12:33 linux-ess: Accepted password for: johndoe from 192.168.0.3 port 38654 ssh2
Jun 14 14:14:12 linux-ess: Accepted publickey for: student from 85.245.107.42 port 48298 ssh2: RSA SHA256:Keo89erjOEkmo
Jun 15 17:42:18 linux-ess: Failed password for: janedoe from 192.168.0.10 port 48239 ssh2
Jun 17 18:22:22 linux-ess: Accepted password for: janedoe from 192.168.0.10 port 43448 ssh2
Jun 19 22:43:23 linux-ess: Failed password for: johndoe from 85.245.107.42 port 22834 ssh2: RSA SHA256:eoKmezlE3iOp38Dj
Jun 22 08:04:00 linux-ess: Accepted password for: johndoe from 192.168.0.99 port 38299 ssh2
Jun 22 21:11:11 linux-ess: Failed password for: doeg from 192.168.0.10 port 44293 ssh2
Jun 22 21:11:11 linux-ess: Failed password for: doeg from 192.168.0.10 port 48987 ssh2
Jun 22 21:11:11 linux-ess: Failed password for: doeg from 192.168.0.10 port 22658 ssh2
Jun 22 21:11:12 linux-ess: Failed password for: doeg from 192.168.0.10 port 34598 ssh2
Jun 22 21:11:12 linux-ess: Failed password for: doeg from 192.168.0.10 port 87568 ssh2
Jun 22 21:11:12 linux-ess: Failed password for: doeg from 192.168.0.10 port 77898 ssh2
Jun 22 21:11:12 linux-ess: Accepted password for: doeg from 192.168.0.10 port 44293 ssh2
```

## Pipes gebruiken
Een pipe (|) is een specifiek symbool dat we kunnen gebruiken om commando's aan elkaar te koppelen. Het pipesymbool neemt de stdout van het vorige commando en stuurt deze door naar de stdin van het volgende commando:

```bash
student@linux-ess:~$ head -3 auth.log | tail -2
Jun 09 11:11:11 linux-ess: Server listening on :: port 22.
Jun 09 12:32:24 linux-ess: Accepted publickey for: johndoe from 85.245.107.42 port 54259 ssh2: RSA SHA256:K18kPGZrTiz7g
```

In het bovenstaande voorbeeld wordt het commando head -3 uitgevoerd dat de eerste 3 regels van het bestand auth.log neemt. De uitvoer met de eerste 3 regels van het bestand wordt vervolgens gebruikt als invoer voor het commando tail -2, wat resulteert in het nemen van de onderste 2 regels van de eerste 3 regels van het bestand auth.log. Dit betekent dat het resultaat de tweede en derde regel van het bestand is.

Je kan zoveel pipes gebruiken als je wil in een opdrachtregel. Het zal gewoon de uitvoer van een opdracht blijven doorgeven aan de invoer van de volgende opdracht, enzovoort:

```bash
student@linux-ess:~$ cat auth.log | head | tail -3 | head -2 | tail -1
Jun 15 17:42:18 linux-ess: Failed password for: janedoe from 192.168.0.10 port 48239 ssh2
```

## Schrijf naar bestand (tee)
Soms wil je de resultaten tijdelijk naar een apart bestand schrijven terwijl je met pipes blijft werken om een bepaald eindresultaat te krijgen. Dit commando stuurt de stdin door naar de stdout maar slaat de stdin ook op in een bestand dat als argument wordt geleverd:

```bash
student@linux-ess:~$ tail -3 auth.log | tee temp_log | tail -1
Jun 22 21:11:12 linux-ess: Accepted password for: doeg from 192.168.0.10 port 44293 ssh2
student@linux-ess:~$ cat temp_log
Jun 22 21:11:12 linux-ess: Failed password for: doeg from 192.168.0.10 port 87568 ssh2
Jun 22 21:11:12 linux-ess: Failed password for: doeg from 192.168.0.10 port 77898 ssh2
Jun 22 21:11:12 linux-ess: Accepted password for: doeg from 192.168.0.10 port 44293 ssh2
```

Tee wordt ook vaak gebruikt om resultaten in een bestand te plaatsen waar je niet de juiste privileges hebt en sudo moet gebruiken:

```bash
student@linux-ess:~$ tail -1 auth.log > /filteredlogfile
-bash: /filteredlogfile: Permission denied
student@linux-ess:~$ sudo tail -1 auth.log > /filteredlogfile
-bash: /filteredlogfile: Permission denied
student@linux-ess:~$ tail -1 auth.log | tee /filteredlogfile
Jun 22 21:11:12 linux-ess: Accepted password for: doeg from 192.168.0.10 port 44293 ssh2
tee: /filteredlogfile: Permission denied
student@linux-ess:~$ tail -1 auth.log | head -1 | sudo tee /filteredlogfile                  # dit lukt dus wel
Jun 22 21:11:12 linux-ess: Accepted password for: doeg from 192.168.0.10 port 44293 ssh2
student@linux-ess:~$ cat /filteredlogfile
Jun 22 21:11:12 linux-ess: Accepted password for: doeg from 192.168.0.10 port 44293 ssh2
```

Als je aan het uitvoerbestand wilt toevoegen in plaats van het te overschrijven, kan je de optie -a gebruiken

```bash
student@linux-ess:~$ head -1 auth.log | sudo tee -a /filteredlogfile
Jun 09 11:11:11 linux-ess: Server listening on 0.0.0.0 port 22.
student@linux-ess:~$ cat /filteredlogfile
Jun 22 21:11:12 linux-ess: Accepted password for: doeg from 192.168.0.10 port 44293 ssh2
Jun 09 11:11:11 linux-ess: Server listening on 0.0.0.0 port 22.
```


## Filteren van uitvoer
### Inhoudsfilters gebruiken (grep)
We willen vaak door de inhoud van een bestand bladeren en een overzicht verkrijgen van de regels die een welbepaalde string of patroon bevatten. Dit is waar het grepcommando om de hoek komt kijken. `grep`` is een van de meest gebruikte filtercommando's in Linux-systemen. We kunnen het als volgt als zelfstandig commando gebruiken:

```bash
student@linux-ess:~$ grep jane auth.log
Jun 15 17:42:18 linux-ess: Failed password for: janedoe from 192.168.0.10 port 48239 ssh2
Jun 17 18:22:22 linux-ess: Accepted password for: janedoe from 192.168.0.10 port 43448 ssh2
```

Of we kunnen het gebruiken als een pipe:

```bash
student@linux-ess:~$ cat auth.log | grep jane
Jun 15 17:42:18 linux-ess: Failed password for: janedoe from 192.168.0.10 port 48239 ssh2
Jun 17 18:22:22 linux-ess: Accepted password for: janedoe from 192.168.0.10 port 43448 ssh2
```

Beide commando's geven hetzelfde resultaat. Wat we kunnen zien is dat het grep commando de inhoud van het bestand filtert op basis van een string of patroon (in dit geval de string jane).

::: warning Grep is hoofdlettergevoelig
`grep` is standaard een hoofdlettergevoelig commando en toont alleen de regels in het bestand met dat specifieke trefwoord. Het zoeken naar de string `failed` in enkel kleine letters zal dus 0 regels retourneren:
:::

```bash
student@linux-ess:~$ grep failed auth.log
student@linux-ess:~$
```

Er is echter de optie -i om grep hoofdletterongevoelig te maken:

```bash
student@linux-ess:~$ grep -i failed auth.log
Jun 10 21:38:01 linux-ess: Failed password for: student from 192.168.0.1 port 37362 ssh2
Jun 10 21:39:01 linux-ess: Failed password for: johndoe from 192.168.0.2 port 37849 ssh2
Jun 15 17:42:18 linux-ess: Failed password for: janedoe from 192.168.0.10 port 48239 ssh2
Jun 19 22:43:23 linux-ess: Failed password for: johndoe from 85.245.107.42 port 22834 ssh2: RSA SHA256:eoKmezlE3iOp38Dj
Jun 22 21:11:11 linux-ess: Failed password for: doeg from 192.168.0.10 port 44293 ssh2
Jun 22 21:11:11 linux-ess: Failed password for: doeg from 192.168.0.10 port 48987 ssh2
Jun 22 21:11:11 linux-ess: Failed password for: doeg from 192.168.0.10 port 22658 ssh2
Jun 22 21:11:12 linux-ess: Failed password for: doeg from 192.168.0.10 port 34598 ssh2
Jun 22 21:11:12 linux-ess: Failed password for: doeg from 192.168.0.10 port 87568 ssh2
Jun 22 21:11:12 linux-ess: Failed password for: doeg from 192.168.0.10 port 77898 ssh2
```

Een andere interessante optie is -v die alle regels zonder de string/patroon retourneert:

```bash
student@linux-ess:~$ cat auth.log | grep -i -v failed
Jun 09 11:11:11 linux-ess: Server listening on 0.0.0.0 port 22.
Jun 09 11:11:11 linux-ess: Server listening on :: port 22.
Jun 09 12:32:24 linux-ess: Accepted publickey for: johndoe from 85.245.107.42 port 54259 ssh2: RSA SHA256:K18kPGZrTiz7g
Jun 10 21:42:01 linux-ess: Accepted password for: student from 84.298.138.41 port 48785 ssh2
Jun 14 14:12:33 linux-ess: Accepted password for: johndoe from 192.168.0.3 port 38654 ssh2
Jun 14 14:14:12 linux-ess: Accepted publickey for: student from 85.245.107.42 port 48298 ssh2: RSA SHA256:Keo89erjOEkmo
Jun 17 18:22:22 linux-ess: Accepted password for: janedoe from 192.168.0.10 port 43448 ssh2
Jun 22 08:04:00 linux-ess: Accepted password for: johndoe from 192.168.0.99 port 38299 ssh2
Jun 22 21:11:12 linux-ess: Accepted password for: doeg from 192.168.0.10 port 44293 ssh2
````

Wetende dat we meerdere pipes (|) in een commando kunnen gebruiken, kunnen we ook meerdere grep-commando's combineren. Stel je het scenario voor waarin we alleen succesvolle inlogmomenten willen vinden die door de gebruiker janedoe zijn gemaakt. We zouden dit als volgt kunnen doen:

```bash
student@linux-ess:~$ cat auth.log | grep -iv failed | grep janedoe
Jun 17 18:22:22 linux-ess: Accepted password for: janedoe from 192.168.0.10 port 43448 ssh2
```

of (er zijn hier meerdere juiste antwoorden)

```bash
student@linux-ess:~$ cat auth.log | grep janedoe | grep Accepted
Jun 17 18:22:22 linux-ess: Accepted password for: janedoe from 192.168.0.10 port 43448 ssh2
```

Soms willen we misschien meer zien dan alleen de lijn die de string/het patroon bevat. Stel je voor dat we wat meer context willen zien over waar het bestand zich bevindt. We kunnen het grep-commando aanpassen om regels voor en/of na het resultaat als volgt weer te geven:

```bash
student@linux-ess:~$ cat example.log
this is line one
this is line two
this is line three
this is line four
this is line five
student@linux-ess:~$ grep -A1 three example.log
this is line three
this is line four
student@linux-ess:~$ grep -B2 four example.log
this is line two
this is line three
this is line four
student@linux-ess:~$ grep -C1 three example.log
this is line two
this is line three
this is line four
```

::: warning Filters werken alleen op stdout
Filters zoals `grep` werken alleen op de uitvoerstroom (stdout) en **niet** op de foutstroom (stderr). Om ook door foutmeldingen te zoeken moeten we de twee stromen samenvoegen:
:::

```bash
student@linux-ess:~$ find /etc/ssl -name "*.c??"
/etc/ssl/openssl.cnf
/etc/ssl/certs/ca-certificates.crt
find: ‘/etc/ssl/private’: Permission denied
student@linux-ess:~$ find /etc/ssl -name "*.c??" | tr 'abcde' 'ABCDE'
/EtC/ssl/opEnssl.Cnf
/EtC/ssl/CErts/CA-CErtifiCAtEs.Crt
find: ‘/etc/ssl/private’: Permission denied
student@linux-ess:~$ find /etc/ssl -name "*.c??" |& tr 'abcde' 'ABCDE'
/EtC/ssl/opEnssl.Cnf
/EtC/ssl/CErts/CA-CErtifiCAtEs.Crt
finD: ‘/EtC/ssl/privAtE’: PErmission DEniED
```

Of een ander voorbeeld waarbij we alleen de foutopsporingsbestanden uit de sys-map willen zien die kernel in de naam hebben. We zien hier dat het alle foutregels afdrukt omdat de grep-filter niet werkt op de foutstroom

```bash
student@linux-ess:~$ find /sys -iname "*kernel*" | grep debug
find: '/sys/kernel/tracing': Permission denied
find: '/sys/kernel/debug': Permission denied
find: '/sys/fs/pstore': Permission denied
find: '/sys/fs/bpf': Permission denied
/sys/fs/cgroup/sys-kernel-debug.mount
```

De oplossing is opnieuw om de twee stromen samen te voegen:

```bash
student@linux-ess:~$ find /sys -iname "*kernel*" |& grep debug
find: '/sys/kernel/debug': Permission denied
/sys/fs/cgroup/sys-kernel-debug.mount
```

## Inhoudsstructuur gebruiken (cut, sort, uniq)
### Kolommen gebruiken (cut)
Met behulp van het commando cut kunnen we regels in een bestand splitsen in kolommen. Om dit te doen, moeten we een scheidingsteken definiëren (dit is een karakter dat het begin van een nieuwe kolom definieert), bijvoorbeeld een spatie- of :-teken. Vervolgens kunnen we selecteren welke kolommen (=fields) de opdracht moet weergeven:

```bash
student@linux-ess:~$ cat auth.log
Jun 09 11:11:11 linux-ess: Server listening on 0.0.0.0 port 22.
Jun 09 11:11:11 linux-ess: Server listening on :: port 22.
Jun 09 12:32:24 linux-ess: Accepted publickey for: johndoe from 85.245.107.42 port 54259 ssh2: RSA SHA256:K18kPGZrTiz7g>
Jun 10 21:38:01 linux-ess: Failed password for: student from 192.168.0.1 port 37362 ssh2
Jun 10 21:39:01 linux-ess: Failed password for: johndoe from 192.168.0.2 port 37849 ssh2
Jun 10 21:42:01 linux-ess: Accepted password for: student from 84.298.138.41 port 48785 ssh2
Jun 14 14:12:33 linux-ess: Accepted password for: johndoe from 192.168.0.3 port 38654 ssh2
Jun 14 14:14:12 linux-ess: Accepted publickey for: student from 85.245.107.42 port 48298 ssh2: RSA SHA256:Keo89erjOEkmo>Jun 15 17:42:18 linux-ess: Failed password for: janedoe from 192.168.0.10 port 48239 ssh2
Jun 17 18:22:22 linux-ess: Accepted password for: janedoe from 192.168.0.10 port 43448 ssh2
Jun 19 22:43:23 linux-ess: Failed password for: johndoe from 85.245.107.42 port 22834 ssh2: RSA SHA256:eoKmezlE3iOp38Dj>Jun 22 08:04:00 linux-ess: Accepted password for: johndoe from 192.168.0.99 port 38299 ssh2
Jun 22 21:11:11 linux-ess: Failed password for: doeg from 192.168.0.10 port 44293 ssh2
Jun 22 21:11:11 linux-ess: Failed password for: doeg from 192.168.0.10 port 48987 ssh2
Jun 22 21:11:11 linux-ess: Failed password for: doeg from 192.168.0.10 port 22658 ssh2
Jun 22 21:11:12 linux-ess: Failed password for: doeg from 192.168.0.10 port 34598 ssh2
Jun 22 21:11:12 linux-ess: Failed password for: doeg from 192.168.0.10 port 87568 ssh2
Jun 22 21:11:12 linux-ess: Failed password for: doeg from 192.168.0.10 port 77898 ssh2
Jun 22 21:11:12 linux-ess: Accepted password for: doeg from 192.168.0.10 port 44293 ssh2
student@linux-ess:~$ head -3 auth.log | cut -d":" -f1
Jun 09 11
Jun 09 11
Jun 09 12
```

Zoals je in het bovenstaande voorbeeld kunt zien, hebben we het :-teken als scheidingsteken gebruikt. Vervolgens gebruikten we de optie -f om enkel de eerste kolom weer te geven. Een volledige regel in dit logboekbestand ziet er als volgt uit:

```bash
student@linux-ess:~$ head -1 auth.log
Jun 09 11:11:11 linux-ess: Server listening on 0.0.0.0 port 22.
```

Dit betekent dat de eerste kolom eindigt op het :-teken in de tijdnotatie (na het uur). De tweede kolom bestaat uit het minutendeel van de tijdnotatie, de derde kolom uit de seconden van de tijdnotatie en de hostnaam enzovoort. We kunnen de opdracht ook vertellen om meerdere kolommen weer te geven:

```bash
student@linux-ess:~$ head -3 auth.log | cut -d":" -f1,2,3
Jun 09 11:11:11 linux-ess
Jun 09 11:11:11 linux-ess
Jun 09 12:32:24 linux-ess
```

Een ander mooi voorbeeld van waar we dit kunnen gebruiken is het /etc/passwd bestand waar we eenvoudig alle gebruikersnamen en hun homefolder locaties kunnen filteren:

```bash
student@linux-ess:~$ cat /etc/passwd | grep bash
root:x:0:0:root:/root:/bin/bash
student:x:1000:1000:student:/home/student:/bin/bash
student@linux-ess:~$ cat /etc/passwd | grep bash  | cut -d":" -f1,6
root:/root
student:/home/student
```

::: info
Merk op dat de homefolder van de gebruiker `root` geen subfolder is van `/home`, maar van de root van het bestandssysteem (`/`).
:::

### Sorteren (sort & uniq)
Als we de regels van een bestand willen sorteren, kunnen we het commando sort gebruiken. Met het commando uniq worden alleen de unieke waarden getoond.

```bash
student@linux-ess:~$ cat auth.log | grep -v listening
Jun 09 12:32:24 linux-ess: Accepted publickey for: johndoe from 85.245.107.42 port 54259 ssh2: RSA SHA256:K18kPGZrTiz7g>
Jun 10 21:38:01 linux-ess: Failed password for: student from 192.168.0.1 port 37362 ssh2
Jun 10 21:39:01 linux-ess: Failed password for: johndoe from 192.168.0.2 port 37849 ssh2
Jun 10 21:42:01 linux-ess: Accepted password for: student from 84.298.138.41 port 48785 ssh2
Jun 14 14:12:33 linux-ess: Accepted password for: johndoe from 192.168.0.3 port 38654 ssh2
Jun 14 14:14:12 linux-ess: Accepted publickey for: student from 85.245.107.42 port 48298 ssh2: RSA SHA256:Keo89erjOEkmo>Jun 15 17:42:18 linux-ess: Failed password for: janedoe from 192.168.0.10 port 48239 ssh2
Jun 17 18:22:22 linux-ess: Accepted password for: janedoe from 192.168.0.10 port 43448 ssh2
Jun 19 22:43:23 linux-ess: Failed password for: johndoe from 85.245.107.42 port 22834 ssh2: RSA SHA256:eoKmezlE3iOp38Dj>Jun 22 08:04:00 linux-ess: Accepted password for: johndoe from 192.168.0.99 port 38299 ssh2
Jun 22 21:11:11 linux-ess: Failed password for: doeg from 192.168.0.10 port 44293 ssh2
Jun 22 21:11:11 linux-ess: Failed password for: doeg from 192.168.0.10 port 48987 ssh2
Jun 22 21:11:11 linux-ess: Failed password for: doeg from 192.168.0.10 port 22658 ssh2
Jun 22 21:11:12 linux-ess: Failed password for: doeg from 192.168.0.10 port 34598 ssh2
Jun 22 21:11:12 linux-ess: Failed password for: doeg from 192.168.0.10 port 87568 ssh2
Jun 22 21:11:12 linux-ess: Failed password for: doeg from 192.168.0.10 port 77898 ssh2
Jun 22 21:11:12 linux-ess: Accepted password for: doeg from 192.168.0.10 port 44293 ssh2
student@linux-ess:~$ cat auth.log | grep -v listening | cut -d ':' -f5 | cut -d ' ' -f2 | sort | uniq
doeg
janedoe
johndoe
student
```

::: warning
Om `uniq` te gebruiken moet je de gegevens **altijd eerst sorteren** met `sort`!
:::

::: tip AND-operator met grep
Om de AND-operator toe te passen kun je twee `grep`-commando's achter elkaar pipen, of een regex gebruiken:
:::

```bash
cat auth.log | grep "port 44293"
Jun 22 21:11:11 linux-ess: Failed password for: doeg from 192.168.0.10 port 44293 ssh2
Jun 22 21:11:12 linux-ess: Accepted password for: doeg from 192.168.0.10 port 44293 ssh2
student@linux-ess:~$ cat auth.log | grep -i "accepted" | grep "port 44293"
Jun 22 21:11:12 linux-ess: Accepted password for: doeg from 192.168.0.10 port 44293 ssh2
student@linux-ess:~$ cat auth.log | grep -i "accepted.*port 44293"
Jun 22 21:11:12 linux-ess: Accepted password for: doeg from 192.168.0.10 port 44293 ssh2
```


## Tellingen gebruiken (wc)
Als we de regels, woorden of bytes van een document willen tellen, kunnen we het commando wc gebruiken:

```bash
student@linux-ess:~$ wc auth.log
  17  245 1731 auth.log
```

Het eerste getal is het aantal regels, het tweede getal het aantal woorden en het derde getal het aantal bytes(karakters) van de bestandsinhoud.

We kunnen ook maar één van de opties opvragen:

```bash
student@linux-ess:~$ wc -l auth.log # numer of lines
17 auth.log
student@linux-ess:~$ wc -w auth.log # number of words
245 auth.log
student@linux-ess:~$ wc -c auth.log # number of bytes
1731 auth.log
student@linux-ess:~$ wc -m auth.log # number of characters
1731 auth.log
```

  
## Output manipuleren
### Vertalen (tr)
Met het commando tr kunnen we bepaalde karakters vertalen naar andere karakters. Er zijn 2 argumenten voor nodig:

Het karakter (of een reeks karakters) dat moet worden vervangen
Het karakter (of de reeks karakters) die de vorige set moet vervangen
We kunnen hieronder een eenvoudig voorbeeld zien:

```bash
student@linux-ess:~$ head -3 auth.log | tr 'e' 'E'
Jun 09 11:11:11 linux-Ess: SErvEr listEning on 0.0.0.0 port 22.
Jun 09 11:11:11 linux-Ess: SErvEr listEning on :: port 22.
Jun 09 12:32:24 linux-Ess: AccEptEd publickEy for: johndoE from 85.245.107.42 port 54259 ssh2: RSA SHA256:K18kPGZrTiz7g>
```

alle letters e in de uitvoer worden vertaald naar de hoofdletter E. Zoals gezegd in de bovenstaande uitleg kunnen we ook bereiken of sets van karakters gebruiken:

```bash
student@linux-ess:~$ head -3 auth.log | tr 'abcdklmn' 'ABCDKLMN'
JuN 09 11:11:11 LiNux-ess: Server ListeNiNg oN 0.0.0.0 port 22.
JuN 09 11:11:11 LiNux-ess: Server ListeNiNg oN :: port 22.
JuN 09 12:32:24 LiNux-ess: ACCepteD puBLiCKey for: johNDoe froM 85.245.107.42 port 54259 ssh2: RSA SHA256:K18KPGZrTiz7g>
student@linux-ess:~$ head -3 auth.log | tr 'a-z' 'A-Z'
JUN 09 11:11:11 LINUX-ESS: SERVER LISTENING ON 0.0.0.0 PORT 22.
JUN 09 11:11:11 LINUX-ESS: SERVER LISTENING ON :: PORT 22.
JUN 09 12:32:24 LINUX-ESS: ACCEPTED PUBLICKEY FOR: JOHNDOE FROM 85.245.107.42 PORT 54259 SSH2: RSA SHA256:K18KPGZRTIZ7G>
````

Het zijn niet alleen gewone karakters die we kunnen vervangen. We kunnen speciale tekens zoals newlines of tabs als volgt gebruiken:

```bash
student@linux-ess:~$ cat example.log
this is line one
this is line two
this is line three
this is line four
this is line five
student@linux-ess:~$ od -c example.log
0000000   t   h   i   s       i   s       l   i   n   e       o   n   e
0000020  \n   t   h   i   s       i   s       l   i   n   e       t   w
0000040   o  \n   t   h   i   s       i   s       l   i   n   e       t
0000060   h   r   e   e  \n   t   h   i   s       i   s       l   i   n
0000100   e       f   o   u   r  \n   t   h   i   s       i   s       l
0000120   i   n   e       f   i   v   e  \n
0000131
student@linux-ess:~$ cat example.log | tr '\n' '-'
this is line one-this is line two-this is line three-this is line four-this is line five-
```

In het bovenstaande voorbeeld worden alle newlines gewijzigd in spaties.

Stel je voor dat we een aantal gegevens hebben die meerdere voorkomens van een specifiek karakter hebben en we willen dat er maar één wordt weergegeven (= squeeze). We kunnen de optie -s gebruiken om terugkerende karakters te verwijderen:

```bash
student@linux-ess:~$ head -3 auth.log | tr -s '1'
Jun 09 1:1:1 linux-ess: Server listening on 0.0.0.0 port 22.
Jun 09 1:1:1 linux-ess: Server listening on :: port 22.
Jun 09 12:32:24 linux-ess: Accepted publickey for: johndoe from 85.245.107.42 port 54259 ssh2: RSA SHA256:K18kPGZrTiz7g>
```

Ten slotte hebben we de optie -d die elk van de karakters die we in de tekst definiëren verwijdert:

```bash
student@linux-ess:~$ head -3 auth.log | tr -d ':'
Jun 09 111111 linux-ess Server listening on 0.0.0.0 port 22.
Jun 09 111111 linux-ess Server listening on  port 22.
Jun 09 123224 linux-ess Accepted publickey for johndoe from 85.245.107.42 port 54259 ssh2 RSA SHA256K18kPGZrTiz7g>
```


### Stream editor (sed)
sed is een geavanceerde stream-editor die bewerkingsfuncties kan uitvoeren met behulp van regular expressions. Herinner je je het commando rename nog? We kunnen hier dezelfde syntax als bij regular expressions gebruiken:

```bash
student@linux-ess:~$ tail -4 auth.log | sed 's/Failed/Incorrect/'
Jun 22 21:11:12 linux-ess: Incorrect password for: doeg from 192.168.0.10 port 34598 ssh2
Jun 22 21:11:12 linux-ess: Incorrect password for: doeg from 192.168.0.10 port 87568 ssh2
Jun 22 21:11:12 linux-ess: Incorrect password for: doeg from 192.168.0.10 port 77898 ssh2
Jun 22 21:11:12 linux-ess: Accepted password for: doeg from 192.168.0.10 port 44293 ssh2
```

In het bovenstaande voorbeeld wordt de string Failed voor elke regel één keer gewijzigd in Incorrect.

::: tip
`sed` past wijzigingen standaard **alleen toe in de uitvoer** — het bestand zelf wordt niet aangepast. Gebruik de optie `-i` om het bestand zelf te wijzigen:
:::

```bash
student@linux-ess:~$ tail -4 auth.log > lastfourlines
student@linux-ess:~$ cat lastfourlines
Jun 22 21:11:12 linux-ess: Failed password for: doeg from 192.168.0.10 port 34598 ssh2
Jun 22 21:11:12 linux-ess: Failed password for: doeg from 192.168.0.10 port 87568 ssh2
Jun 22 21:11:12 linux-ess: Failed password for: doeg from 192.168.0.10 port 77898 ssh2
Jun 22 21:11:12 linux-ess: Accepted password for: doeg from 192.168.0.10 port 44293 ssh2 
student@linux-ess:~$ sed -i 's/Failed/Incorrect/' lastfourlines
student@linux-ess:~$ cat lastfourlines
Jun 22 21:11:12 linux-ess: Incorrect password for: doeg from 192.168.0.10 port 34598 ssh2
Jun 22 21:11:12 linux-ess: Incorrect password for: doeg from 192.168.0.10 port 87568 ssh2
Jun 22 21:11:12 linux-ess: Incorrect password for: doeg from 192.168.0.10 port 77898 ssh2
Jun 22 21:11:12 linux-ess: Accepted password for: doeg from 192.168.0.10 port 44293 ssh2
```

::: warning
`sed` vervangt een patroon standaard **slechts één keer per regel**. Zoals je in het onderstaande voorbeeld ziet, blijft de tweede `example` ongewijzigd:
:::

```bash
student@linux-ess:~$ echo "example this is an example" | sed 's/example/test/'
test this is an example
```

Alleen het eerste voorkomen van example wordt gewijzigd in test. Als we willen dat het sed-commando elk voorkomen in een regel verandert, moeten we de g (global) flag gebruiken zoals hieronder te zien is:

```bash
student@linux-ess:~$ echo "example this is an example" | sed 's/example/test/g'
test this is an test
```

Er is ook een i-flag die de regex (=zoekstring) hoofdletterongevoelig maakt:

```bash
student@linux-ess:~$ echo "example this is an Example" | sed 's/example/test/g'
test this is an Example
student@linux-ess:~$ echo "example this is an Example" | sed 's/example/test/gi'
test this is an test
```

We kunnen sed ook gebruiken om bepaalde tekst te maskeren:

```bash
student@linux-ess:~$ head -2 auth.log
Jun 09 11:11:11 linux-ess: Server listening on 0.0.0.0 port 22.
Jun 09 11:11:11 linux-ess: Server listening on :: port 22.
student@linux-ess:~$ head -2 auth.log | sed 's/..:..:../00:00:00/'
Jun 09 00:00:00 linux-ess: Server listening on 0.0.0.0 port 22.
Jun 09 00:00:00 linux-ess: Server listening on :: port 22.
student@linux-ess:~$ head -2 auth.log | sed 's/..:..:..//'
Jun 09  linux-ess: Server listening on 0.0.0.0 port 22.
Jun 09  linux-ess: Server listening on :: port 22.
```

Ten slotte zullen we kijken naar de d-flag die elke lijn met de string verwijdert:

```bash
student@linux-ess:~$ tail -4 auth.log
Jun 22 21:11:12 linux-ess: Failed password for: doeg from 192.168.0.10 port 34598 ssh2
Jun 22 21:11:12 linux-ess: Failed password for: doeg from 192.168.0.10 port 87568 ssh2
Jun 22 21:11:12 linux-ess: Failed password for: doeg from 192.168.0.10 port 77898 ssh2
Jun 22 21:11:12 linux-ess: Accepted password for: doeg from 192.168.0.10 port 44293 ssh2
student@linux-ess:~$ tail -4 auth.log | sed '/Failed/d'
Jun 22 21:11:12 linux-ess: Accepted password for: doeg from 192.168.0.10 port 44293 ssh2
```




## Regular expressions
In de voorbeelden van grep, bovenaan deze pagina, hebben we alleen eenvoudige strings gebruikt om bepaalde regels in een bestand te vinden. Soms willen we filteren op dynamische content. Stel je voor dat je alle logins vindt vanaf een ip-adres met '192' gevolgd door andere tekens, of gebruikers wil die 'doe' als achternaam hebben. In deze gevallen zullen we zoeken naar tekenreeksen via een bepaald patroon. Om dit te bereiken moeten we een dynamische syntax gebruiken die een reguliere expressie wordt genoemd.

regular expressions kunnen veranderen in een echt konijnenhol. We zullen ons alleen richten op de meest gebruikte cases en een paar praktische voorbeelden, maar weet dat er een hele regex wereld te verkennen is die buiten deze cursus valt!

Het commando grep kan verschillende soorten regex patronen gebruiken. Standaard gebruikt het basic regular expressions (BRE) maar voor veel gevallen willen we dit uitbreiden naar extended regular expressions (ERE). Om dit te doen, moeten we de optie -E gebruiken in het commando grep. Dit geeft ons veel meer functionaliteiten als het gaat om het bouwen van dynamische zoekopdrachten. Veel van de onderstaande commando's werken niet zonder de optie -E!

Voor de voorbeelden die in deze sectie worden gebruikt, gebruiken we een apart bestand dat je kan downloaden met behulp van het onderstaande commando:

```bash
student@linux-ess:~$ wget https://vwgert.github.io/data/regexlist.txt
--2024-10-31 15:00:43--  https://vwgert.github.io/data/regexlist.txt
Resolving vwgert.github.io (vwgert.github.io)... 185.199.108.153, 185.199.111.153, 185.199.109.153, ...
Connecting to vwgert.github.io (vwgert.github.io)|185.199.108.153|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 318 [text/plain]
Saving to: ‘regexlist.txt’
 
regexlist.txt              100%[========================================>]     318  --.-KB/s    in 0s
 
2024-10-31 15:00:43 (14.7 MB/s) - ‘regexlist.txt’ saved [318/318]
student@linux-ess:~$ cat regexlist.txt
Charlotte
Lawrence
Max
Stan
Emma
Sara
John
Kelly
Ian
Ellen
Tim
Robin
Nora
Tom
Caroline
Michael
john.doe@pxl.b
john.doe@pxl.be
p
pl
px
pxl
pxxl
pxxxl
pxxxxl
128
32
64
htp://www.pxl.be
http://www.pxl.be
https://www.pxl.be
192.168.1.19
192.168.5.117
172.16.0.4
127.0.0.1
pxe
pxe boot
This is a test.
This has been tested
```

Of je kan het hieronder downloaden en scp-en naar je Linux server met `scp -i "<pad naar ssh-key>" <pad naar regexlist.txt> <username>@<server-ip>:`

::: warning
Opgelet! Vergeet de dubbele punt niet achteraan de commandoregel!
:::

<a href="/downloads/regexlist.txt" download style="display:inline-flex;align-items:center;gap:0.5em;padding:0.45rem 1.2rem;border-radius:6px;background:var(--vp-c-brand-1);color:#fff;text-decoration:none;font-weight:600;font-size:0.95rem;border:1.5px solid var(--vp-c-brand-1);">⬇ Download regexlist.txt</a>

Om te beginnen zullen we een aantal speciale symbolen gebruiken die we eerder hebben gebruikt. We hebben de impact van een sterretje (*) gezien in het hoofdstuk over file globbing. Een sterretje heeft een vergelijkbare functionaliteit in een regex, maar er zijn belangrijke verschillen:

In file globbing betekent een *-teken 0, één of meerdere willekeurige karakters
In een regex betekent een *-teken 0, één of meerdere van het vorige karakter
Neem het voorbeeld hieronder. We verwachten dat alleen de 'pxl'-varianten verschijnen, maar zoals we in de uitvoer kunnen zien, wordt alle bestandsinhoud weergegeven. Dit komt omdat elke regel overeenkomt met de regex nul, één of meerdere voorkomens van de letter p:

```bash
student@linux-ess:~$ cat regexlist.txt | grep "p*"                                 # or grep "p*" regexlist.txt
Charlotte
Lawrence
Max
Stan
Emma
Sara
John
Kelly
Ian
Ellen
Tim
Robin
Nora
Tom
Caroline
Michael
john.doe@pxl.b
john.doe@pxl.be
p
pl
px
pxl
pxxl
pxxxl
pxxxxl
128
32
64
htp://www.pxl.be
http://www.pxl.be
https://www.pxl.be
192.168.1.19
192.168.5.117
172.16.0.4
127.0.0.1
pxe
pxe boot
This is a test.
This has been tested
```

Als we de regels willen filteren met een p en het volgende teken kan 0,1 of meerdere voorkomens van x zijn, wordt dit gedaan met behulp van de volgende syntaxis:

```bash
student@linux-ess:~$ grep "px*" regexlist.txt
john.doe@pxl.b
john.doe@pxl.be
p
pl
px
pxl
pxxl
pxxxl
pxxxxl
htp://www.pxl.be
http://www.pxl.be
https://www.pxl.be
pxe
pxe boot
```

::: info Patroon hoeft niet aan het begin te staan
De gefilterde regels hoeven niet met het patroon te beginnen — `grep` zoekt het patroon op elke positie in de regel.
:::

Vanwege het feit dat we geen karakters achter de x plaatsen, konden we dit karakter ook gewoon weglaten:

```bash
student@linux-ess:~$ grep "p" regexlist.txt
john.doe@pxl.b
john.doe@pxl.be
p
pl
px
pxl
pxxl
pxxxl
pxxxxl
htp://www.pxl.be
http://www.pxl.be
https://www.pxl.be
pxe
pxe boot
```

Nu vertellen we de regex om regels te vinden die een p bevatten, gevolgd door nul, één of meerdere karakters 'x'. Dit is precies waarom pl verschijnt (het bevat nul voorkomens van het karakter x):

```bash
student@linux-ess:~$ grep "px*l" regexlist.txt
john.doe@pxl.b
john.doe@pxl.be
pl
pxl
pxxl
pxxxl
pxxxxl
htp://www.pxl.be
http://www.pxl.be
https://www.pxl.be
```

Stel je voor dat we een regex zouden willen gebruiken die één of meerdere voorkomens van een karakter bevat in plaats van nul, één of meer. Dit kunnen we doen met het +-teken. Als we dit gebruiken zullen we zien dat de regel met de tekst pl niet meer in de resultaten staat:

```bash
student@linux-ess:~$ grep -E "px+l" regexlist.txt                                # or   grep "px\+l" regexlist.txt
john.doe@pxl.b
john.doe@pxl.be
pxl
pxxl
pxxxl
pxxxxl
htp://www.pxl.be
http://www.pxl.be
https://www.pxl.be
```

::: tip
Zonder de optie `-E` moet je het plusteken escapen: `grep "px\+l" regexlist.txt`
:::

Om nog een stap verder te gaan, hoe zit het met precies 3 voorkomens? We kunnen dit eenvoudig als volgt doen:

```bash
student@linux-ess:~$ grep -E "px{3}l" regexlist.txt                             # or   grep "px\{3\}l" regexlist.txt
pxxxl
```

De {3} betekent hier ook het aantal keer dat het voorafgaand karakter moet voorkomen.

::: tip
Zonder de optie `-E` moet je de accolades escapen: `grep "px\{3\}l" regexlist.txt`
:::

Stel je nu voor dat we willen controleren op regels die beginnen of eindigen met een specifiek karakter of string. We beginnen met regels die beginnen met een specifiek karakter:

```bash
student@linux-ess:~$ grep -i "^[cms]" regexlist.txt
Charlotte
Max
Stan
Sara
Caroline
Michael
```

In het bovenstaande voorbeeld wordt een ^-teken gebruikt dat het begin van een regel aangeeft. Vervolgens gebruiken we vierkante haken [ ] die we kunnen gebruiken om karakters op te geven die als het begin van de regel kunnen worden gebruikt. In dit geval de letters c, m en s. We kunnen ook een bereik gebruiken:

```bash
student@linux-ess:~$ grep "^[0-9]" regexlist.txt
128
32
64
192.168.1.19
192.168.5.117
172.16.0.4
127.0.0.1
student@linux-ess:~$ grep "^[a-z]" regexlist.txt
john.doe@pxl.b
john.doe@pxl.be
p
pl
px
pxl
pxxl
pxxxl
pxxxxl
htp://www.pxl.be
http://www.pxl.be
https://www.pxl.be
pxe
pxe boot
```

::: warning
Een bereik zoals `[a-z]` is **hoofdlettergevoelig**! Gebruik `[a-zA-Z]` als je ook hoofdletters wil meenemen.
:::

Bij het gebruik van vierkante haakjes kunnen we ook het opgegeven patroon uitsluiten door aan het begin (binnen de haakjes) een hoedje (^) op te geven:

```bash
student@linux-ess:~$ grep "[^a-zA-Z0-9:/.]" regexlist.txt                   # no letters, numbers, colon, slash or dot  
john.doe@pxl.b
john.doe@pxl.be
pxe boot
This is a test.
This has been tested
```

Om te controleren op regels die eindigen op een specifiek karakter kunnen we een $-teken gebruiken:

```bash
student@linux-ess:~$ grep "e$" regexlist.txt
Charlotte
Lawrence
Caroline
john.doe@pxl.be
htp://www.pxl.be
http://www.pxl.be
https://www.pxl.be
pxe
student@linux-ess:~$ grep "[0-9]$" regexlist.txt
128
32
64
192.168.1.19
192.168.5.117
172.16.0.4
127.0.0.1
```

En hoe zit het met het matchen van precies 1 willekeurig karakter? Een . vertaalt zich naar precies één willekeurig karakter:

```bash
student@linux-ess:~$ grep -i "t.m" regexlist.txt
Tim
Tom


student@linux-ess:~$ grep "^...\." regexlist.txt
192.168.1.19
192.168.5.117
172.16.0.4
127.0.0.1
```

Dit vertaalt zich naar: begin met drie willekeurige karakters (`^...`), gevolgd door een gewoon punt (`\.`).

::: tip
Het punt is escaped als `\.` zodat het letterlijk wordt geïnterpreteerd en niet als "willekeurig karakter". Vergeet dit niet als je een punt als letterlijk teken bedoelt!
:::


We kunnen dit ook combineren met de begin- & eindregex:

Als we de regels willen filteren met ofwel één patroon ofwel een ander patroon, kunnen we het teken |-gebruiken:

```bash
student@linux-ess:~$ grep -E "^M|n$" regexlist.txt                                  # or    grep "^M\|n$" regexlist.txt
Max
Stan
John
Ian
Ellen
Robin
Michael
```

Hier zoeken we naar regels die beginnen met een hoofdletter M of eindigen met een kleine letter n

::: tip
Zonder de optie `-E` moet je het pipeteken escapen: `grep "^M\|n$" regexlist.txt`
:::

We zouden hetzelfde kunnen doen door de optie -e meerdere keren te gebruiken:

```bash
student@linux-ess:~$ grep -e "^M" -e "n$" regexlist.txt
Max
Stan
John
Ian
Ellen
Robin
Michael
```

Als we regels willen filteren die ineens aan meerdere patronen voldoen, kunnen we het commando grep meerdere keren gebruiken:

```bash
student@linux-ess:~$ grep "^E" regexlist.txt | grep "a$"                            # or    grep "^E.*a$" regexlist.txt
Emma
```

Hier zoeken we naar regels die eindigen op een a en ook beginnen met een E

Als we regels willen filteren die alleen de zoekstring als een volledig woord hebben, gebruiken we de optie -w:

```bash
student@linux-ess:~$ grep "test" regexlist.txt
This is a test.
This has been tested
student@linux-ess:~$ grep -w "test" regexlist.txt
This is a test.
```

In het laatste commando zoeken we naar regels met test als één woord

## sed en Extended Regular Expressions
Natuurlijk kunnen we onze kennis van regular expressions gebruiken met sed, maar als je uitgebreide regular expressions wilt gebruiken, moet je de optie -E opgeven:

```bash
student@linux-ess:~$ grep -C2 www regexlist.txt
32
64
htp://www.pxl.be
http://www.pxl.be
https://www.pxl.be
192.168.1.19
192.168.5.117
student@linux-ess:~$ grep -C2 www regexlist.txt | sed -E 's_https?://.*_url masked_'
32
64
htp://www.pxl.be
url masked
url masked
192.168.1.19
192.168.5.117
```

::: tip
Omdat we slashes (`/`) gebruiken in de regex zelf, kiezen we een ander scheidingsteken voor `sed` — hier underscores (`_`). Zonder de optie `-E` zou je het `?`-teken moeten escapen als `\?`.
:::

```bash
student@linux-ess:~$ grep -C2 www regexlist.txt | sed 's_https\?://.*_url masked_'
32
64
htp://www.pxl.be
url masked
url masked
192.168.1.19
192.168.5.117
```

Nog enkele patroonvoorbeelden
Een regex maken die controleert op een IPv4-adres:

```bash
student@linux-ess:~$ cat regexlist.txt | grep -E "^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$"
192.168.1.19
192.168.5.117
172.16.0.4
127.0.0.1
```

::: info
- Deze regex valideert **geen geldig IPv4-adres** — ze controleert niet of het om een publiek/privé adres gaat, of of de nummers in het bereik 1–255 liggen.
- De syntaxis `{1,3}` betekent dat het vorige karakter **tussen de 1 en 3 keer** moet voorkomen.
- De `^` aan het begin en `$` aan het einde zorgen ervoor dat er **niets anders op dezelfde regel** mag staan.
:::

Een regex maken die controleert op een geldige e-mailadresindeling:

```bash
student@linux-ess:~$ grep -E "^.+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}" regexlist.txt
john.doe@pxl.be
```

Een regex maken die controleert op een geldige URL-indeling:

```bash
student@linux-ess:~$ grep -E "https?://.+\." regexlist.txt
http://www.pxl.be
https://www.pxl.be
```

::: tip
Dit voorbeeld controleert **niet** op geldige domeinnamen — het matcht elk `https?://` gevolgd door tekst en een punt.
:::

::: info
Het vraagteken (`?`) in een regex betekent dat het **vorige karakter optioneel** is (nul of één keer). Zo matcht `https?://` zowel `http://` als `https://`.
:::

We kunnen ook gebruik maken van Grouping om te werken met strings in plaats van slechts één karakter. Zo kunnen we bijvoorbeeld zeggen dat een volledige string optioneel is in plaats van enkel het voorafgaand karakter:

```bash
student@linux-ess:~$ grep -E "pxe( boot)?" regexlist.txt
pxe
pxe boot
```

We kunnen ook een grouping gebruiken om een herhaling te specifiëren van een bepaalde expressie. Zo zijn de twee onderstaande regular expressions hetzelfde:

```bash
student@linux-ess:~$ grep -E "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" regexlist.txt
192.168.1.19
192.168.5.117
172.16.0.4
127.0.0.1
student@linux-ess:~$ grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}$"  regexlist.txt
192.168.1.19
192.168.5.117
172.16.0.4
127.0.0.1
student@linux-ess:~$ grep -E "([0-9]{1,3}\.?){4}"  regexlist.txt
192.168.1.19
192.168.5.117
172.16.0.4
127.0.0.1
```
