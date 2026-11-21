# Oefeningen op software

In deze oefeningen gebruiken we `apt` (en niet `apt-get` en `apt-cache`, wat oudere commando's zijn)

## Oefening 1
Werk de lokale apt-cache bij. Zo krijg je de laatste informatie van de repositories.

::: details Oplossing tonen
```
sudo apt update
```
:::

## Oefening 2
Upgrade alle pakketten, die reeds geïnstalleerd zijn met apt, naar de nieuwste versie.

::: details Oplossing tonen
```
sudo apt upgrade
```
:::

## Oefening 3
Zoek met apt naar een pakket dat iets te maken heeft met `'usage and stats'`. Je ziet `btop` als één van de resultaten. Installeer het pakket en voer de app uit.

::: details Oplossing tonen
```
apt search "usage and stats"
```
```
sudo apt install btop
```
```
btop
```
:::

## Oefening 4
Zoek met apt naar een pakket dat iets te maken heeft met `'colorful'` en met `'cat'`. We plaatsen dan `'.*'` tussen de twee woorden: `'colorful.*cat'`. Je ziet `lolcat` als één van de resultaten. Installeer het pakket en voer de volgende opdrachten uit: `cat .bash_history`  en   `lolcat .bash_history`

::: details Oplossing tonen
```
apt search "colorful.*cat"
```
```
sudo apt install lolcat
```
```
cd
```
```
cat .bash_history
```
```
lolcat .bash_history
```
:::

## Oefening 5
Zoek met `apt search` naar neofetch. Installeer het pakket met apt en voer uit. Indien je het niet vindt installeer je fastfetch.

::: details Oplossing tonen
_Zoek en installeer (kies één van beide):_
```
apt search neofetch
```
```
sudo apt install neofetch
```
```
sudo apt install fastfetch
```
_Voer uit:_
```
neofetch
```
```
fastfetch
```
:::

## Oefening 6
Zoek met apt naar `"the matrix"` en zoek in de eerste 5 gepresenteerde packages naar het pakket dat lijkt op de weergave van de matrixfilm en installeer dit. Voer deze app uit.

::: details Oplossing tonen
```
apt search "the matrix"
```
```
sudo apt install cmatrix
```
```
cmatrix
```
:::

## Oefening 7
Verwijder het pakket `btop` van het systeem. Je zou het niet meer moeten kunnen uitvoeren.

::: details Oplossing tonen
```
sudo apt remove btop
```
:::

## Oefening 8
Toon een lijst van alle pakketten die zijn geïnstalleerd met apt. In de lijst zie je één vermelding voor `caca-utils`. Zo niet, installeer dit pakket en controleer opnieuw. Zoek in de manpage van apt hoe je wat info van deze pakketten kunt zien. Je zal zien dat dit pakket verschillende hulpprogramma's bevat. Probeer de laatste twee. Tip: Je kunt op `enter` drukken om verschillende dingen te zien. Gebruik `ctrl+c` om een hulpprogramma af te sluiten.

::: details Oplossing tonen
```
apt list --installed
```
```
sudo apt install caca-utils
```
_Zoek in de manpage naar `show`:_
```
man apt
```
```
apt show caca-utils
```
_Probeer de laatste twee tools:_
```
cacademo
```
```
cacafire
```
:::

## Oefening 9
Zoek naar een snap pakket via de omschrijving `"resource monitor"`.

::: details Oplossing tonen
```
snap search "resource monitor"
```
:::

## Oefening 10
Installeer de snap `bashtop`. (Bestaat die niet meer in de snap store? Neem dan `btop` of een andere resource monitor uit oefening 9.)

::: details Oplossing tonen
```
sudo snap install bashtop
```
:::

## Oefening 11
Voer `bashtop` uit.

::: details Oplossing tonen
```
bashtop
```
:::

## Oefening 12
We krijgen geen info over de schijven. Dit komt omdat de snap machtigingen nodig heeft om verbonden te zijn met de mount-plug.

Lees de informatie over de snap `bashtop` om een oplossing te vinden. Voer de opdracht uit om het probleem op te lossen. Voer `bashtop` opnieuw uit.

::: details Oplossing tonen
```
snap info bashtop
```
```
sudo snap connect bashtop:mount-observe
```
```
bashtop
```
:::

## Oefening 13
Toon een lijst met geïnstalleerde snaps.

::: details Oplossing tonen
```
snap list
```
:::

## Oefening 14
Verwijder de snap `bashtop`.

::: details Oplossing tonen
```
sudo snap remove bashtop
```
:::

## Oefening 15
Toon een lijst met geïnstalleerde snaps.

::: details Oplossing tonen
```
snap list
```
:::

## Oefening 16
Toon de geschiedenis van wijzigingen in snap en controleer of de snap verwijderd is.

::: details Oplossing tonen
```
snap changes
```
:::

## Oefening 17
Controleer of de snap `asciiquarium` bestaat. Lees wat informatie over de snap, installeer deze en voer deze uit.

::: details Oplossing tonen
```
snap search asciiquarium
```
```
snap info asciiquarium
```
```
sudo snap install asciiquarium
```
```
asciiquarium
```
_Afsluiten met `Ctrl+C` of `q`._
:::

## Oefening 18
Zip de homedirectory van de gebruiker student (met alle bestanden en mappen) in een bestand genaamd `/tmp/myhomefolder.zip`. Bekijk de inhoud van het zipbestand om het resultaat te controleren.

::: details Oplossing tonen
```
sudo apt install zip unzip
```
```
zip -r /tmp/myhomefolder.zip /home/student
```
```
unzip -l /tmp/myhomefolder.zip
```
:::

## Oefening 19
Zoek in de manpage van `zip` om erachter te komen hoe je een bestand uit je zipbestand kunt verwijderen. Verwijder het bestand `.bash_history` uit het zipbestand `/tmp/myhomefolder.zip`. Controleer de inhoud van het zipbestand.

::: details Oplossing tonen
_Zoek in de manpage naar `delete`:_
```
man zip
```
```
zip -d /tmp/myhomefolder.zip home/student/.bash_history
```
```
unzip -l /tmp/myhomefolder.zip
```
:::

## Oefening 20
Maak een map met de naam `zipdemo` in de tijdelijke map (`/tmp`). Pak het zipbestand `myhomefolder.zip` uit in de map `/tmp/zipdemo`. Gebruik `tree` om te controleren of het proces met succes is voltooid.

::: details Oplossing tonen
```
mkdir -p /tmp/zipdemo
```
```
unzip /tmp/myhomefolder.zip -d /tmp/zipdemo
```
```
tree /tmp/zipdemo
```
:::

## Oefening 21
Maak een tarball genaamd `/tmp/myhomefolder.tar.gz` met de bestanden en mappen van de homedirectory van de gebruiker student. Bekijk de inhoud van de tarfile om het resultaat te controleren. Maak een map met de naam `tardemo` in de tijdelijke map (`/tmp`). Pak de tarball `myhomefolder.tar.gz` uit in de directory `/tmp/tardemo`.

::: details Oplossing tonen
_Maak de tarball:_
```
tar -czf /tmp/myhomefolder.tar.gz /home/student
```
```
tar -tf /tmp/myhomefolder.tar.gz
```
```
mkdir /tmp/tardemo
```
```
tar -xzf /tmp/myhomefolder.tar.gz -C /tmp/tardemo
```
:::

## Oefening 22
Extra uitdaging: Probeer het bestand `.bashrc` uit de tarball te verwijderen (oefening 21). Doorzoek de manpage van `tar` om een oplossing te vinden. Controleer de inhoud van de tarball aan het einde van de oefening.

::: details Oplossing tonen
_`--delete` werkt niet op een gecomprimeerd `.tar.gz` — eerst uitpakken, dan verwijderen, dan opnieuw inpakken:_
```
gunzip /tmp/myhomefolder.tar.gz
```
```
tar --delete -f /tmp/myhomefolder.tar home/student/.bashrc
```
```
gzip /tmp/myhomefolder.tar
```
```
tar -tf /tmp/myhomefolder.tar.gz | grep -E "\.bashrc$" || echo "verwijderd"
```
:::

## Oefening 23
Probeer Google Chrome te installeren op je Ubuntu Desktop met de command line interface. Zoals je kunt zien wanneer je naar een download zoekt, vind je alleen een `.deb` pakket om te downloaden. Gebruik dit pakket met `dpkg` om Google Chrome te installeren.

Moeilijker: Probeer dit `.deb` pakket te downloaden met `wget` om de volledige installatie in je CLI te voltooien.

::: details Oplossing tonen
_Download met wget:_
```
wget -O /tmp/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```
_Installeer met dpkg en los afhankelijkheden op:_
```
sudo dpkg -i /tmp/google-chrome.deb || sudo apt -f install
```
:::
