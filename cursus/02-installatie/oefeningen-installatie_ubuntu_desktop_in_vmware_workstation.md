# Oefeningen op Installatie
 
### In deze oefeningen ga je een Ubuntu Desktop omgeving installeren in een Virtuele Machine (VM) om daarna te verkennen


## Oefening 1 - Ubuntu Desktop downloaden
Linux heeft ook een desktopversie. Download [Ubuntu Desktop](https://ubuntu.com/download/desktop).

![Download Ubuntu Desktop](./assets/ubuntu1.png)

## Oefening 2 - Nieuwe Virtuele Machine (VM) aanmaken
Om een nieuwe virtuele machine (VM) aan te maken in VMware Workstation kies je voor het aanmaken van een nieuwe VM. De wizard voor het maken van een nieuwe VM wordt weergegeven.

In het eerste scherm selecteren we de optie Typical:

![VMware Installatie Standaard](./assets/workst1.png)

Vervolgens kiezen we voor I will install the operating system later:

![VMware installeert besturingssysteem later](./assets/workst2.png)

Vervolgens kiezen we voor het besturingssysteem Linux. In de versie dropdown selecteren we Ubuntu 64-bit. Dit is de Linux-distributie die we tijdens de labs zullen gebruiken.

![VMware Ubuntu 64bit](./assets/workst3.png)

In het volgende scherm configureren we de grootte van de virtuele harde schijf voor de VM. We zullen een schijf maken met 30 GB opslagruimte. Houd er rekening mee dat de schijfruimte enkel wordt ingenomen door het opslaan van bestanden (dus groeiend tot maximum 30 GB).

::: warning Sla de VM niet op in de cloud
Sla de bestanden van de VM niet op in een map die gesynchroniseerd wordt met de cloud (OneDrive, Dropbox, Google Drive). Je VM zal crashen en je zal alles in de VM kwijt zijn!
:::

![VMware schijfgrootte](./assets/workst5.png)

We moeten op Customize Hardware klikken om de virtuele machine verder te configureren:

![VMware past hardware aan](./assets/workst6.png)

We moeten het ISO-bestand van de Ubuntu-desktop nog koppelen aan het virtuele cd-rom-station. Klik op CD/DVD, kies voor *Use ISO image file* en blader naar het gedownloade iso-bestand. Stel ook het geheugen in op minimaal 6 GB. Klik daarna op Close:

![VMware Selecteer ISO en geheugen](./assets/workst7.png)

Je kan ook de stappen voor het selecteren van de ISO afzonderlijk bekijken:

![VMware ISO selectie stappen](./assets/workst4.png)

Klik op Finish en de virtuele machine wordt gemaakt.

![VMware afwerking](./assets/workst4b.png)

We kunnen nu de UEFI bios nog instellen. Klik hiervoor op Edit virtual machine settings.

![VMware UEFI stap 1](./assets/workst8.png)

Ga naar het tabblad Options, klik op Advanced en selecteer de optie UEFI. Hier vind je ook de instelling *Side channel mitigations*. Krijg je later bij het starten van de VM telkens een waarschuwing hierover, dan kan je ze hier uitschakelen.

![VMware UEFI stap 2](./assets/uefi2.png)

Je kan de VM nu opstarten door op het groene pijltje te klikken. Hiermee wordt de virtuele machine opgestart en wordt het installatieproces uitgevoerd.

![VMware start VM](./assets/uefi1.png)


## Oefening 3 - Ubuntu Desktop installeren
::: warning
Resulteert het opstarten van de VM in de fout *This host supports Intel VT-x, but Intel VT-x is disabled*, dan moet je de VT-x-optie activeren in de BIOS/UEFI van je laptop. Meer informatie is te vinden in [dit artikel](https://www.qtithow.com/2020/12/fix-error-this-host-supports-Intel-VT-x.html).
:::

Wanneer we de VM voor de eerste keer opstarten, verschijnt het GRUB-menu. We moeten op enter drukken of een paar seconden wachten:

![Ubuntu Desktop First Grub](./assets/grub1.png)

In de volgende paar stappen zal er een installatieprocedure zijn die we moeten doorlopen.

We kiezen de taal (English):

![Ubuntu Desktop Taalkeuze](./assets/taal.png)

We stellen niets in bij *Accessibility*:

![Ubuntu Desktop Accessibility](./assets/access.png)

We kiezen de juiste keyboard layout. Voor AZERTY selecteren we Belgian. Indien je een QWERTY-keyboard hebt, behoud je best English (US). Indien je een AZERTY toetsenbord hebt en op een Mac werkt, dan kies je voor French (Macintosh).

![Ubuntu Desktop Keyboard Layout](./assets/keyb.png)

We moeten kiezen voor wired connection omdat we deze Ubuntu in een virtuele omgeving draaien:

![Ubuntu Desktop Internetverbinding](./assets/conn.png)

We maken de keuze om Ubuntu te installeren:

![Ubuntu Desktop Installeren of Uitproberen](./assets/inst.png)

We kiezen voor een interactieve installatie:

![Ubuntu Desktop Type Installatie](./assets/typeinst.png)

We kiezen er voor om enkel de standaard selectie van applicaties te installeren:

![Ubuntu Desktop Applicaties](./assets/apps.png)

We kiezen er voor om third-party software te installeren voor drivers en multimedia formats:

![Ubuntu Desktop Third-party software](./assets/third.png)

We kiezen er voor om de disk leeg te maken en Ubuntu Desktop er op te installeren. Denk er aan dat je enkel de Virtuele Disk van je VM gaat ledigen en dit is een lege disk op dit moment. De hard disk van jouw computer/laptop zal dus **niet** leeg gemaakt worden!

![Ubuntu Desktop Disk ledigen](./assets/ledig.png)

We kiezen ervoor om geen versleuteling (encryption) te gebruiken:

![Ubuntu Desktop Versleuteling](./assets/encrypt.png)

We specificeren de gebruikersnaam, wachtwoord en de computernaam. Gebruik als gebruikersnaam **student**, als wachtwoord **ubdesk** en als computernaam een naam naar keuze:

![Ubuntu Desktop Account aanmaken](./assets/name.png)

Als tijdzone klikken we op de kaart Brussel aan of schrijven we Europe/Brussels in het tekstvak:

![Ubuntu Desktop Tijdzone Brussel](./assets/timezone.png)

Controleer de instellingen en klik op Install om de installatie te starten:

![Ubuntu Desktop Klaar om te installeren](./assets/installready.png)

Nu moeten we wachten tot de installatie afgerond is:

![Ubuntu Desktop Installatie bezig](./assets/afronden.png)

Van zodra de installatie afgerond is klikken we op Restart Now om de VM te herstarten:

![Ubuntu Desktop Herstart na installatie](./assets/restart.png)

Wanneer we het scherm zien waar gevraagd wordt om de installatiemedia te verwijderen, gaan we eerst in de settings van de Virtuele Machine de CD/DVD loskoppelen. Ga in VMware naar het menu VM > Settings:

![Ubuntu Verwijder installatiemedia](./assets/remove.png)

![VMware Settings openen](./assets/goset.png)

We vinken uit dat de CD/DVD geconnecteerd moet worden tijdens het booten van de VM (anders wordt telkens bij het opstarten van de VM de installatie opnieuw gestart!)

![VMware CD/DVD uitschakelen](./assets/nocd.png)

Nu kunnen we drukken op de {{Enter}}-toets om de installatie af te ronden door te herstarten. Ubuntu zal opstarten vanaf de harde schijf:

![Ubuntu start op](./assets/udinstall2.png)



## Oefening 4 - Inloggen voor de eerste keer
De allereerste keer dat we inloggen moeten we door de configuratieschermen. Klik op de gebruiker student om in te loggen:

![Ubuntu Desktop Inlogscherm](./assets/inloggen.png)

Vul het wachtwoord in:

![Ubuntu Desktop Wachtwoord invoeren](./assets/wachtwoord.png)

Na het inloggen verschijnt de welkomstwizard en een melding van de Software Updater:

![Ubuntu Desktop Na inloggen](./assets/ingelogd.png)

De welkomst-wizard van Ubuntu 26.04 begeleidt ons door een aantal instellingen. Klik op Next om verder te gaan:

![Ubuntu Desktop Welkomstscherm](./assets/welcome.png)

Kies de gewenste weergave (licht of donker) en een accentkleur:

![Ubuntu Desktop Uiterlijk](./assets/look.png)

Ubuntu Pro kunnen we overslaan voor onze oefeningen:

![Ubuntu Desktop Ubuntu Pro](./assets/pro.png)

Schakel de telemetrieoptie uit om geen gebruiksgegevens te delen:

![Ubuntu Desktop Verbeteren helpen](./assets/impr.png)

Locatieservices kunnen we uitschakelen:

![Ubuntu Desktop Locatieservices](./assets/location.png)

In het laatste scherm van de wizard kun je de App Center openen voor extra applicaties. Klik op Finish om de wizard te sluiten:

![Ubuntu Desktop Klaar om te beginnen](./assets/finish.png)

Nu zijn we klaar om Ubuntu Desktop verder te verkennen:

![Ubuntu Desktop](./assets/desktop.png)



## Oefening 5 - Een snapshot maken (disaster-recovery)
Voordat je iets anders doet, is het een goede gewoonte om een momentopname, oftewel snapshot, te maken. Als op een later tijdstip onze Ubuntu Desktop niet meer opstart of we iets fout hebben ingesteld, kunnen we altijd terugkeren naar deze momentopname. Het is een tijdsbesparing om terug te kunnen keren naar dit punt, omdat we anders het Linux-systeem opnieuw moeten installeren.

Indien er nog updates wachtende zijn, voer je die eerst uit via de Software Updater:

![Ubuntu Desktop Software Updater openen](./assets/update.png)

![Ubuntu Desktop Updates installeren](./assets/instupdates.png)

Maak een momentopname van de Ubuntu Desktop VM, genaamd "Clean install" als volgt:

Sluit eerst de VM af via het energiemenu rechtsboven:

![Ubuntu Desktop Uitschakelen](./assets/poweroff.png)

![Ubuntu Desktop Uitschakelen bevestigen](./assets/poweroff2.png)

Ga in VMware naar VM/Snapshot/Take Snapshot...

![VMware Snapshot maken](./assets/takesnap.png)

Geef de snapshot de naam "Clean install":

![VMware Snapshot naam](./assets/cleaninstall.png)

::: tip
Op een later tijdstip kun je altijd teruggaan naar deze momentopname in de tijd met:

VM/Snapshot/Revert to Snapshot...
:::

![VMware Teruggaan naar snapshot](./assets/revert.png)



## Oefening 6 - Verkennen van de desktopomgeving 

Probeer op de Ubuntu-desktop de volgende oefeningen uit te voeren:

1. Verander de desktopachtergrond
1. Maak een nieuw tekstbestand met de tool "Text Editor" en probeer het op te slaan in je documentenmap
1. Controleer met de bestandsverkenner (Files) of het bestand bestaat
1. Verwijder het bestand en leeg de prullenbak
1. Pin (=Favorite) de Text Editor-applicatie aan het Dock (=launcher of Dash)
1. Surf met Firefox naar de website van de school
1. Installeer de Chromium-webbrowser, start de app, maak deze vast aan het Dock en plaats deze boven het Firefox-pictogram
1. Surf met Chromium naar de school webmail portal (mail.pxl.be)
1. Installeer Libreoffice en verken de apps Writer, Impress en Calc
1. Installeer Codium (Visual Studio Code) en verken de app
1. Installeer Gimp en bekijk de app
