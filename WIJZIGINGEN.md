# Wijzigingen t.o.v. de oorspronkelijke cursus

Hoofdstuk 06 is volledig herwerkt (zie onderaan). Voor de andere hoofdstukken zijn fouten, kapotte opmaak en verouderde voorbeelden gecorrigeerd. Hoofdstukken 07 t/m 10 zijn minder diep nagelopen dan 01 t/m 06 en 11: daar vooral opmaak- en structuurfouten.

## Overzichten
- De PDF-spiekbriefjes zijn opnieuw opgebouwd als "Overzicht hoofdstuk"-pagina in de cursus (tab "Overzicht" bij hoofdstuk 01 t/m 09, bron: `overzicht.md` in elke hoofdstukmap). Ze zijn doorzoekbaar, hebben een afdrukknop en een "Test jezelf" met uitklapbare antwoorden.
- Aangepast bij het overnemen: servernaam `linux-ess` (stond `ubserv`), `dnf` naast `yum`, `sudo` bij `tail` op `auth.log`, `head -n 2` i.p.v. `head -2`.
- "Linux Snelle hulp (tldr)" staat in het overzicht van hoofdstuk 03 en als sectie "Snelle hulp met tldr" onder de manpages in de theorie van hoofdstuk 03.

## Alle hoofdstukken
- Promptnamen eenvormig: `student@linux-ess` (op een paar plaatsen stond `ubserv`, `ubuntu-server`, `ulinux-ess` of `@linux-ess` zonder gebruiker).
- Codeblokken met ontbrekende of foute afsluiting hersteld; losse commando's en scriptinhoud in codeblokken gezet.
- HTML-afbeeldingen vervangen door gewone markdown-afbeeldingen.
- Geneste `::: tip` binnen `::: details` verwijderd.

## 01 Introductie, 02 Installatie
- Servernaam overal `linux-ess`. Pagina `ms-visual-studio-pro.md` is een extra tab in hoofdstuk 01.
- Niet te verifiëren: PXL-specifieke stappen (Academic Software, SharePoint-link).

## 03 Command Line Interface
- Uitvoer van `echo Einde` gecorrigeerd. Nieuw: sectie "Snelle hulp met tldr".

## 04 Bestanden en mappen
- `rm -f` correct beschreven; `cp`-voorbeeld met juiste bestandsnaam; `cp -i` melding. Oefening 23: ondubbelzinnige tab-completion.
- Let op: sommige oefeningen verwijzen naar mappen `chapter5` / `chapter6`.

## 05 Software en pakketten
- Opsommingen hersteld, `dependency hell`-zin afgewerkt, tar-opties als lijst. Oefening 5 zonder "OF" in het codeblok, oefening 22 `grep "\.bashrc$"`.
- Kennistoets: tarball-vraag had twee juiste antwoorden; `sources.list` aangevuld met `ubuntu.sources` (Ubuntu 24.04).

## 07 t/m 10
- 08: promptnamen. 10: codeblokken rond `ls -l`-voorbeelden, geneste tip in oefening 7 verwijderd.

## 11 Automatisatie
- Kapotte codeblokken hersteld; uitvoer van `helloworld.sh` kwam niet overeen met het script; scriptinhoud en commando's gescheiden.
- Locale-voorbeeld: `sed` op `/etc/locale.conf` (bestaat niet op Ubuntu) vervangen door `sudo update-locale LC_TIME=nl_BE.UTF-8`.
- `at` installeren vermeld, tijdzone-uitleg in eigen kopje, dubbele prompt verwijderd.

## 12 Extra's (Ubuntu Pro)
- Lijsten en kopjes hersteld.

## Oefeningen en oplossingen (offline bestand)
- Per oefening **Klaar** of **Overslaan**. Oplossingen openen pas als alle oefeningen van die set klaar of overgeslagen zijn. Hoofdstuk 01 en 02 hebben geen oplossingen. Docent: voeg `?docent` toe aan de URL om alles te ontgrendelen.

## Aandachtspunten
- Screenshots in hoofdstukken 01 t/m 03 tonen deels Ubuntu 22.04 en 24.04 terwijl de desktopinstallatie 26.04 toont. Niet aangepast.
- Hoofdstuk 08 haalt bestanden op via `wget` van `vwgert.github.io`. Controleer of die nog bereikbaar zijn.

## Hoofdstuk 06

## Inhoudelijke fouten verbeterd
- **Oefening 15 (i):** de opgave zei "regel 10", de oplossing "regel 9". Na stap e (één regel verwijderd) is het regel 9. Opgave aangepast en uitleg toegevoegd.
- **Oefening 15 (j):** "voer de knip opnieuw uit" is *redo* (`Alt+E`), niet opnieuw `Ctrl+K`.
- **Oefening 15 (k):** in de oplossing ontbrak het knippen van de laatste regel (`Ctrl+K`).
- **Oefening 15 (m):** "twee keer een sneltoets" is `Ctrl+S` + `Ctrl+X` (niet `Ctrl+O`, `Enter`, `Ctrl+X`).
- **Oefening 17:** `-v` is overbodig bij meerdere bestanden (head/tail tonen dan automatisch de bestandsnaam). Oplossing en uitleg aangepast; `-v` is enkel nodig bij één bestand.
- **less afsluiten:** `Ctrl+C` sluit `less` niet af (enkel `q`). Gecorrigeerd.
- **`-i` in less:** nuance toegevoegd (smartcase) en `-I` vermeld.
- **Oefening 10:** kapotte opsomming (ontbrekende spaties na `*`) hersteld.
- **Oefening 2:** vermelding dat `MemTotal` in kB staat.
- **Oefening 9:** `sudo` toegevoegd (auth.log is niet leesbaar voor gewone gebruikers).
- **Typfouten:** `æctrl + d`, `crtl + d`, `ctl+w`, `commado`, `less´`, "Maar" met hoofdletter midden in een zin, ontbrekende spaties, enz.
- **`more`:** uitleg genuanceerd (het is een beperktere pager, niet "enkel naar beneden").
- **`cat overspoelt de terminal`:** formulering gecorrigeerd ("kun je niet scrollen" was te absoluut).
- **Plakken in nano:** uitleg toegevoegd (plakken van buiten nano gebeurt door de terminal).

## Verouderd -> actueel
- nano 4.8-screenshot vervangen door een nano 7.2-weergave (Ubuntu 24.04). Sneltoetsenlijst gecontroleerd op nano 7.2.
- Voorbeelden bijgewerkt: Ubuntu 24.04.3, recente datums in logvoorbeelden.
- `head -2` -> `head -n 2` (duidelijkere, aanbevolen schrijfwijze); `Ctrl+O` -> `Ctrl+S` als snelste opslaanmethode.
- `Ctrl+_` -> `Ctrl+/` (zichtbaar in de nano-balk); `Alt+D` voor telling en `Alt+Q` voor vorige treffer toegevoegd.

## Nieuw
- Overzichtstabel "Welk commando gebruik ik wanneer?" en een spiekbrief.
- `cat -n`, `head -c`, `tail -n +N`, `tail -F`, `journalctl -f`, `less`-sneltoetsentabel (`g`, `G`, `?`, `F`, `-N`, `h`).
- Waarschuwing voor `>` (overschrijft) en voor `cat bestand > bestand`.
- Tip: `Ctrl+D` werkt het best aan het begin van een lege regel.
- Hoe kom je uit `vim` (`Esc`, `:q!`).
- Oefening 18 (extra): regels 5 t/m 8 met `head | tail`.
- Kennistoets: 9 nieuwe vragen die bij dit hoofdstuk horen.

## Kennistoets herschikt
De oorspronkelijke vragen over nginx, `scp`, `tar`, `wget`, `Ctrl+F5` hoorden niet bij dit hoofdstuk. Ze staan nu onder "Deel 2: herhaling uit andere hoofdstukken" (de nano-vraag is bijgewerkt naar `Ctrl+S`, `Ctrl+X`).

## Update: layout en afbeeldingen
- Rechter paneel "Op deze pagina" verwijderd; pagina's zijn nu enkelvoudig.
- Fout in `10-rechten/theorie.md` hersteld (ontbrekende sluit-fence), waardoor commentaarregels als titels verschenen.
- Decoratieve afbeeldingen verwijderd (tux, distro-grap, tar-joke, chmod_joke, hoofdstukheaders in wat-zal-je-leren.md). Functionele screenshots en diagrammen blijven.
- Nieuw: eigen SVG-illustratie per hoofdstuk in de hero (`_bouw/art.py`).
