::: info

Dit hoofdstuk komt aan bod in week 12.

De geschatte tijd voor dit hoofdstuk is ± 2 uur.

:::

## Kernvragen

Dit hoofdstuk gaat over het automatiseren van taken in Linux met behulp van bash-scripts, de PATH-variabele, geplande taken (`at`) en cronjobs.

1. Hoe maak en voer je een bash-script uit?
2. Hoe gebruik je variabelen en parameters in een script?
3. Hoe plan je een eenmalige taak in met `at`?
4. Hoe maak je een herhalende taak aan met `cron`?
5. Wat is de rol van de variabele `PATH` bij het uitvoeren van scripts?

## Leerdoelstellingen

De student...

1. ... kan een bash-script aanmaken met een correcte shebang en het uitvoerbaar maken met `chmod +x`.
2. ... kan een script uitvoeren met `./scriptnaam`, via `bash scriptnaam` (zonder uitvoerrechten) en via de `PATH`-variabele.
3. ... kan systeemvariabelen (`$USER`, `$HOME`) en eigen variabelen gebruiken in een script.
4. ... kan invoer van de gebruiker opvangen met `read` en meegegeven parameters verwerken via `$1`, `$2`, `$3`.
5. ... kan de uitvoer van een commando inbedden in een script via command substitution (`$(commando)`).
6. ... kan de `PATH`-variabele uitbreiden zodat scripts in een zelfgekozen map overal uitvoerbaar zijn, en deze wijziging permanent maken via `~/.profile`.
7. ... kan een eenmalige geplande taak aanmaken met `at` en de status ervan controleren.
8. ... kan een persoonlijke cronjob aanmaken met `crontab -e` en de crontab-syntaxis correct toepassen (inclusief `@reboot`).
9. ... kan een systeembrede cronjob toevoegen via `/etc/crontab` en een bijhorend script aanmaken.
