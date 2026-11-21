# 02. Installatie


## Virtualisatie
Om servers te installeren die diensten aanbieden (zoals een minecraft server!) heb je een server nodig met een openbaar IP-adres. Meestal zou je naar een cloudprovider gaan waar je voor een vast bedrag/maand een server kunt huren. Voor deze cursus zullen we dit proces ook simuleren met behulp van een lokale virtuele machine. Dit kan ons dan ook helpen voor wanneer we eens geen Internet-connectie hebben bijvoorbeeld.

Virtualisatie is een concept waarbij je een computersysteem met een besturingssysteem virtueel op een ander systeem kunt laten draaien. Dit maakt het mogelijk om meerdere **gast**-besturingssystemen, elk met hun eigen virtuele hardware, op één **host**-systeem (het fysieke toestel met het echte besturingssysteem) te laten draaien.

![Virtualisatie](./assets/Virtualization.svg)

In deze cursus zullen we dus een lokale Virtuele Machine installeren als backup voor een Cloud instance waarin we normaal gezien zullen werken.



## Ubuntu Server image
Voor deze cursus gebruiken we het besturingssysteem Ubuntu Server en installeren we het in een virtuele omgeving. Ubuntu is een op Debian gebaseerde distro.

::: info Welke versie?
De schermafbeeldingen in dit hoofdstuk zijn van een Ubuntu LTS-versie (*Long Term Support*, 5 jaar updates). Kies steeds de nieuwste **LTS**-versie die je lector aangeeft; de installatiestappen zijn tussen LTS-versies zeer gelijkaardig.
:::

Download het `.iso`-bestand voor Ubuntu Server via [ubuntu.com/download/server](https://ubuntu.com/download/server). Een `.iso`-bestand is een exacte kopie van een CD/DVD. Je gebruikt dit later om het besturingssysteem in de virtuele machine te installeren.

![Download Ubuntu Server](./assets/GetUbuntuServer_Download_Ubuntu.png)



## Virtualisatiesoftware
Om virtualisatie te gebruiken zijn er verschillende opties. De meest voorkomende virtualisatiesoftware is:

* VMware Workstation
* VirtualBox
* Hyper-V

In deze cursus zullen we VMware Workstation gebruiken en ondersteunen, maar de andere softwarepakketten hebben hetzelfde doel.



## Aanmaken nieuwe VM
Om een nieuwe virtuele machine (VM) aan te maken in VMWare ga je naar het menu **File > New Virtual Machine**. De wizard om een nieuwe VM te maken wordt weergegeven.

![VMware bestand nieuwe VM](./assets/VMware_File_New_VM.png)

In het eerste scherm selecteren we de optie Typical:

![VMware Installatie Standaard](./assets/VMware_Typical.png)

Vervolgens kiezen we voor I will install the operating system later:

![VMware installeert besturingssysteem later](./assets/VMware_Operating_System_Later.png)

Vervolgens kiezen we voor het besturingssysteem Linux. In de versie dropdown selecteren we Ubuntu 64 bit. Dit is de Linux-distributie die we tijdens deze cursus zullen gebruiken.

![VMware Ubuntu 64bit](./assets/VMware_Ubuntu_64bit.png)

In het volgende scherm geven we de virtuele machine een naam. Je kunt ook een andere map opgeven om de virtuele machine op je computer op te slaan.

::: warning Sla de VM niet op in de cloud
Sla de bestanden van de VM niet op in een map die gesynchroniseerd wordt met de cloud (OneDrive, Dropbox, Google Drive). Je VM zal crashen en je zal alles in de VM kwijt zijn!
:::

![VMware noemt de VM](./assets/VMware_Name_The_VM.png)

In het volgende scherm configureren we de grootte van de virtuele harde schijf voor de VM. We zullen een schijf maken met 20 GB opslag. We kunnen dit later uitbreiden als dat nodig is:

![VMware schijfgrootte](./assets/VMware_Disk_Size.png)

We moeten op Customize Hardware klikken om de virtuele machine verder te configureren:

![VMware past hardware aan](./assets/VMware_Customize_Hardware.png)

We moeten nog steeds het ISO-bestand van de Ubuntu-server koppelen aan het virtuele cd-rom-station. Dit doen we door New CD/DVD te selecteren en naar het gedownloade iso bestand te bladeren:

![VMware Selecteer ISO](./assets/VMware_Select_ISO.png)

Klik op Finish en de virtuele machine wordt gemaakt.

![VMware afwerking](./assets/VMware_Finish.png)

We kunnen nu de UEFI bios nog instellen. Klik hiervoor op Edit virtual machine settings.

![VMware UEFI stap 1](./assets/VMware_UEFI_1.png)

Ga naar het tabblad Options, klik op Advanced en selecteer de optie UEFI. Hier vind je ook de instelling *Side channel mitigations*. Krijg je later bij het starten van de VM telkens een waarschuwing hierover, dan kan je ze hier uitschakelen.

![VMware UEFI stap 2](./assets/VMware_UEFI_2.png)

Je kunt de VM nu opstarten door op het groene pijltje te klikken. Hiermee wordt de virtuele machine opgestart en wordt het installatieproces uitgevoerd.

![VMware start VM](./assets/VMware_Start_VM.png)


## Installatie Ubuntu Server
Zoals eerder beschreven zullen we de distro Ubuntu gebruiken. Na het maken en opstarten van de virtuele machine is er een installatieproces dat we moeten doorlopen. Je zal merken dat er geen muisaanwijzer beschikbaar is. We gebruiken de pijltjestoetsen en enter om door de stappen te navigeren.

::: warning VT-x uitgeschakeld?
Resulteert het opstarten van de VM in de fout *This host supports Intel VT-x, but Intel VT-x is disabled*, dan moet je de VT-x-optie (virtualisatie) activeren in de BIOS/UEFI van je laptop. Bij AMD-processoren heet die optie *SVM Mode* of *AMD-V*.
:::

::: tip Muis kwijt?
Wil je je muis terug in het besturingssysteem van je laptop (de host, bv. Windows), druk dan op {{Ctrl+Alt}}.
:::

We maken de keuze om Ubuntu te proberen of te installeren:

![Ubuntu Server Try Or Install](./assets/Ubuntu_Server_Try_Or_Install.png)

We starten het installatieproces door een taal te selecteren. We kiezen voor English:

![Ubuntu Server Language](./assets/Ubuntu_Server_Language.png)

We slaan de update van het installatieprogramma over indien je dit schermpje krijgt:

![Ubuntu Server No Installer Update](./assets/Ubuntu_Server_No_Installer_Update.png)

Kies de juiste toetsenbordindeling. Voor een AZERTY-toetsenbord selecteer je Belgian. Studenten met een Mac kiezen voor French (Macintosh).

![Ubuntu Server Keyboard Belgian](./assets/Ubuntu_Server_Keyboard_Belgian.png)

In de volgende 7 stappen brengen we geen wijzigingen aan. We drukken gewoon op **Done** of **Continue**:

![Ubuntu Server Base For The Installation](./assets/Ubuntu_Server_Base_For_The_Installation.png)

![Ubuntu Server Network Connections](./assets/Ubuntu_Server_Network_Connections.png)

![Ubuntu Server Proxy Settings](./assets/Ubuntu_Server_Proxy_Settings.png)

![Ubuntu Server Archive Mirror](./assets/Ubuntu_Server_Archive_Mirror.png)

![Ubuntu Server Storage Config](./assets/Ubuntu_Server_Storage_Config.png)

![Ubuntu Server Storage Config Overview](./assets/Ubuntu_Server_Storage_Config_Overview.png)

![Ubuntu Server Storage Config Overview Confirmation](./assets/Ubuntu_Server_Storage_Config_Overview_Confirmation.png)

Vervolgens maken we een gebruikersaccount aan dat we gebruiken om in te loggen op het besturingssysteem. We gebruiken de volgende inloggegevens:

| Instelling | Waarde |
| --- | --- |
| Gebruikersnaam | `student` |
| Servernaam | `linux-ess` |
| Wachtwoord | `pxl` |

(De servernaam `linux-ess` zie je terug in de prompt `student@linux-ess:~$` in de rest van de cursus.)

![Ubuntu Server Username student Servername](./assets/Ubuntu_Server_Storage_Username_student_Servername_linux-ess.png)

Op de vraag om te upgraden naar Ubuntu Pro behouden we het antwoord **Skip for now**.

![Ubuntu Server Upgrade To Ubuntu Pro](./assets/Ubuntu_Server_Upgrade_To_Ubuntu_Pro.png)

Als extra pakket kiezen we ervoor om enkel de **OpenSSH server** te installeren:

![Ubuntu Server SSH](./assets/Ubuntu_Server_Storage_SSH_WEL.png)

![Ubuntu Server Featured Server Snaps](./assets/Ubuntu_Server_Storage_Featured_Server_Snaps.png)

Het besturingssysteem wordt geïnstalleerd en geconfigureerd. Na een tijdje verschijnt de optie Reboot now. Dit geeft aan dat de installatie is voltooid:

![Ubuntu Server Reboot](./assets/Ubuntu_Server_Reboot.png)

Vervolgens zien we een venster dat vraagt om de {{Enter}}-toets te drukken, maar eerst gaan we naar de settings van de virtuele machine:

![Ubuntu Server VM Settings](./assets/Ubuntu_Server_VM_Settings.png)

Daar vinken we uit dat de CD/DVD moet geconnecteerd worden bij het opstarten (anders blijft de installatie laden telkens we de Virtuele Machine opstarten)

![Ubuntu Server Disable CDROM](./assets/Ubuntu_Server_Disable_CDROM.png)

En dan drukken we op de {{Enter}}-toets:

![Ubuntu Server Press Enter To Reboot](./assets/Ubuntu_Server_Press_Enter_To_Reboot.png)

Zodra de server opnieuw is opgestart, moet je nogmaals op {{Enter}} drukken om de inlogprompt te zien.

![Ubuntu Server Press Enter To See Login](./assets/Ubuntu_Server_Press_Enter_To_See_Login.png)

Je kan nu inloggen en beginnen werken op de server. Achter `login:` type je de gebruikersnaam (`student`) en druk je {{Enter}}. Vervolgens type je je wachtwoord (`pxl`) en druk je op {{Enter}}. Je ziet niet wat je typt: dat is normaal, er verschijnen zelfs geen sterretjes.

![Ubuntu Server Ready To Login](./assets/Ubuntu_Server_Ready_To_Login.png)
