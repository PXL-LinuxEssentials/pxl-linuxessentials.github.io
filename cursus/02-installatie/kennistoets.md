---
outline: deep
---

# Kennistoets: Installatie

Klik op een antwoordoptie of denk eerst zelf na voordat je het antwoord bekijkt.

<Quiz vraag="Wat is een snapshot in de context van virtuele machines?" opties="Een kopie van de VM op een USB-stick.|Een systeemscan van de VM.|Een momentopname van de huidige status van de VM.|Een update van het besturingssysteem." :correct="2">

**Een momentopname van de huidige status van de VM.**

Een snapshot bewaart de volledige toestand van een VM op dat moment. Zo kun je altijd terugkeren naar dat punt als er later iets misgaat.

</Quiz>

<Match
  vraag="Koppel de termen aan hun toepassing:"
  prompts="VMware Workstation|SSH|License Agreement"
  antwoorden="Populaire software voor virtualisatie.|Verbinding maken met een server op een veilige manier.|Een overeenkomst die goedgekeurd moet worden."
  afleidingen="Interface om Cisco switches en Routers te configureren."
/>

<Quiz vraag="Welke software wordt in de cursus gebruikt voor virtualisatie?" opties="VMware Workstation|Docker|Hyper-V|VirtualBox" :correct="0">

**VMware Workstation.**

Hoewel er meerdere virtualisatiepakketten bestaan (VirtualBox, Hyper-V, ...), wordt in deze cursus VMware Workstation gebruikt en ondersteund.

</Quiz>

<Match
  vraag="Koppel de termen aan hun beschrijvingen:"
  prompts="Virtual Machine (VM)|ISO-bestand|Ubuntu Server"
  antwoorden="Simuleert een computersysteem binnen een ander computersysteem.|Kopie van een CD/DVD die gebruikt wordt voor installatie.|Op Debian gebaseerde Linux-distributie."
  afleidingen="Op Redhat gebaseerde Linux-distributie."
/>

<Quiz vraag="Wat is een belangrijk voordeel van het gebruik van virtualisatie?" opties="Het is altijd sneller dan fysieke servers.|Je hebt geen internet nodig voor gebruik.|Het bespaart elektriciteit.|Het kan meerdere besturingssystemen draaien op één host." :correct="3">

**Het kan meerdere besturingssystemen draaien op één host.**

Virtualisatie maakt het mogelijk om meerdere gast-besturingssystemen met hun eigen virtuele hardware op één fysiek systeem te laten draaien.

</Quiz>

<Quiz vraag="Waarom mag je geen VM-bestanden opslaan in een gesyncte map zoals OneDrive of Google Drive?" opties="Omdat het tegen de regels is van VMware.|Omdat het de snelheid vermindert.|Omdat het ongeoorloofd is.|Omdat je VM kan crashen en je alles kwijt kunt raken." :correct="3">

**Omdat je VM kan crashen en je alles kwijt kunt raken.**

Cloud-synchronisatiediensten schrijven voortdurend naar bestanden terwijl de VM actief is. Dit conflicteert met hoe VMware schijfbestanden beheert en kan leiden tot corruptie en dataverlies.

</Quiz>

<Quiz vraag="Wat moet je doen als je de foutmelding 'This host supports Intel VT-x, but Intel VT-x is disabled' krijgt?" opties="Een andere VM-software gebruiken.|Je moet de VT-X-optie activeren in de BIOS van je laptop.|Het ISO-bestand opnieuw downloaden.|De installatie opnieuw starten." :correct="1">

**Je moet de VT-X-optie activeren in de BIOS van je laptop.**

Intel VT-x is hardwarevirtualisatie die VMware nodig heeft. Als dit uitgeschakeld is in de BIOS, kan de VM niet opstarten. Je activeert dit via de BIOS-instellingen van je laptop.

</Quiz>
