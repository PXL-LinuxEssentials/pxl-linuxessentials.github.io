::: info

Dit hoofdstuk wordt doorlopen in week 8 en 9.

De doorlooptijd van dit hoofdstuk is ± 6 uur.

:::

## Kernvragen

Dit hoofdstuk gaat over gebruikers- en groepsbeheer in Linux. Je leert hoe gebruikers en groepen in configuratiebestanden worden vastgelegd, hoe je accounts aanmaakt en wijzigt, en welke invloed groepslidmaatschap heeft op het eigenaarschap van bestanden.

1. Waar bewaart Linux de informatie over gebruikers en groepen?
2. Hoe maak je gebruikers aan, hoe wijzig je ze en hoe verwijder je ze?
3. Hoe stel je wachtwoorden in en hoe wijzig je ze?
4. Hoe maak je groepen aan en hoe beheer je ze?
5. Hoe werkt het lidmaatschap van een primaire en een aanvullende groep?

## Leerdoelstellingen

1. De student(e)...
   1. ... kan de opbouw van `/etc/passwd`, `/etc/shadow` en `/etc/group` beschrijven.
   2. ... kan met `useradd` een nieuwe gebruiker aanmaken, inclusief homefolder, shell en commentaar.
   3. ... kan met `usermod` een gebruikersaccount wijzigen (commentaar, shell, groepslidmaatschap).
   4. ... kan met `userdel -r` een gebruiker samen met zijn homefolder verwijderen.
   5. ... kan met `passwd` wachtwoorden instellen en wijzigen.
   6. ... kan met `su` van gebruiker wisselen en kan het verschil tussen `su` en `su -` uitleggen.
   7. ... kan met `groupadd` en `groupmod` groepen aanmaken en hernoemen.
   8. ... kan met `usermod -aG` een gebruiker toevoegen aan een aanvullende groep en hem eruit verwijderen met `deluser` of `usermod -r`.