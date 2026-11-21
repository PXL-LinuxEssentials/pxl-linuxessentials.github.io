# Linux Essentials – cursus

Cursus Linux voor Toegepaste Informatica (PXL). De website wordt automatisch gebouwd uit de markdown in `cursus/` en gepubliceerd met GitHub Pages.

## Eenmalig instellen
1. Maak een repository op GitHub en push deze map naar de branch `main`.
2. Ga naar **Settings → Pages** en kies bij *Source* **GitHub Actions**.
3. Na de eerste run staat de cursus op `https://<gebruiker>.github.io/<repo>/`.

## Cursus aanpassen
- Pas de markdown aan in `cursus/<hoofdstuk>/` (`theorie.md`, `oefeningen*.md`, `kennistoets.md`, `overzicht.md`, `wat-zal-je-leren.md`) en push. De site wordt vanzelf opnieuw gepubliceerd.
- Afbeeldingen staan in `cursus/<hoofdstuk>/assets/`.

## Lokaal bouwen
```bash
pip install -r bouw/requirements.txt
python bouw/build_all.py site/index.html
```
Het resultaat is één zelfstandig bestand (`site/index.html`) dat ook offline werkt.

## Functies
- Linkermenu met inklapbare hoofdstukken
- Oplossingen bij oefeningen openen pas als alle oefeningen op *Klaar* of *Overgeslagen* staan
- Kennistoetsen, overzichtspagina per hoofdstuk, zoeken (Ctrl+K), donker thema
- Docentenmodus: voeg `?docent` toe aan de URL om alle oplossingen te ontgrendelen

## Niet indexeren
De pagina bevat `noindex, nofollow, noarchive` en er wordt een `robots.txt` (Disallow: /) meegepubliceerd. Zoekmachines die zich daaraan houden, nemen de site niet op. Dit is geen toegangsbeveiliging: wie de link heeft, kan de site openen.
