::: info

Dit hoofdstuk wordt doorlopen in week 6.

De doorlooptijd van dit hoofdstuk is ± 4 uur.

:::

<p align="center">
</p>

## Kernvragen

Dit hoofdstuk focust op geavanceerde commandostructuren in de Linux shell. Je leert hoe je wildcards gebruikt om bestanden te selecteren, aliassen aanmaakt voor veelgebruikte commando's, en in- en uitvoer omleidt tussen commando's en bestanden.

1. Hoe gebruik je wildcards (file globbing) om meerdere bestanden tegelijk te selecteren?
2. Wat zijn aliassen en hoe maak je ze permanent?
3. Hoe leid je standaarduitvoer en foutuitvoer om naar bestanden of `/dev/null`?
4. Hoe koppel je commando's aan elkaar met control operators (`&&`, `||`, `;`)?
5. Hoe gebruik je accolades (`{}`) en vierkante haken (`[]`) in globpatronen?

## Doelstellingen

De student(e)...

1. ... kan wildcards (`*`, `?`, `[]`, `{}`) gebruiken om bestanden te selecteren op basis van naam en extensie.
2. ... begrijpt het verschil tussen `*` (nul of meer tekens) en `?` (exact één teken).
3. ... kan aliassen aanmaken, verwijderen en permanent opslaan in `~/.bash_aliases`.
4. ... kan standaarduitvoer omleiden met `>` (overschrijven) en `>>` (toevoegen).
5. ... kan foutuitvoer (stderr) afzonderlijk omleiden met `2>` of onderdrukken met `2>/dev/null`.
6. ... kan stdout en stderr samen omleiden met `&>`.
7. ... kan commando's koppelen met `&&` (voer uit bij succes) en `||` (voer uit bij fout).
8. ... begrijpt het verschil tussen commentaar (`#`) en de `#`-teken binnen een string.
