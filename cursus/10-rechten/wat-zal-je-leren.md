::: info

Dit hoofdstuk komt aan bod in week 10 en 11.

De geschatte tijd voor dit hoofdstuk is ± 6 uur.

:::

## Kernvragen

Dit hoofdstuk gaat over bestandsrechten en toegangscontrole in Linux. Je leert hoe rechten worden weergegeven en berekend, hoe je ze aanpast en hoe speciale bits en ACL's werken.

1. Hoe lees je de rechten van een bestand of map?
2. Hoe pas je rechten aan met `chmod`?
3. Wat is de invloed van de `umask` op nieuwe bestanden?
4. Hoe wijzig je eigenaar en groep met `chown` en `chgrp`?
5. Waarvoor dienen de speciale bits `setgid` en het sticky bit?
6. Hoe gebruik je ACL's voor verfijnder toegangsbeheer?

## Leerdoelstellingen

De student...

1. ... kan de rechten van een bestand of map aflezen uit de uitvoer van `ls -l` (rwx-notatie en octale notatie).
2. ... kan rechten instellen met `chmod` in zowel symbolische als octale notatie.
3. ... begrijpt hoe de `umask` de standaardrechten van nieuwe bestanden en mappen bepaalt en kan de `umask` aanpassen.
4. ... kan de eigenaar en de groepseigenaar van een bestand aanpassen met `chown` en `chgrp`, en begrijpt het verschil tussen `cp` en `cp -a` bij het kopiëren van bestanden inclusief eigenaarschap en rechten.
5. ... kan de speciale bits `setgid` en het sticky bit uitleggen en toepassen op gedeelde mappen; begrijpt ook het bestaan van `setuid` als theoretisch concept.
6. ... begrijpt het verschil tussen schrijfrecht op een map en schrijfrecht op bestanden in die map.
7. ... kan ACL's instellen en opvragen met `setfacl` en `getfacl`, inclusief default ACL's voor overerving.
8. ... kan een back-up van ACL-configuraties maken en terugzetten.
