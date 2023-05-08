# Käyttöohje
### Käynnistysohje
1.  Kloonaa repositorio koneellesi ja siirry projektin juurikansioon.
2.  Asenna projektin riippuvuudet komennolla `poetry install`.
3.  Käynnistä sovellus projektin juurikansiossa komennolla `python3 src/main.py`.

### Toiminnallisuudet
Kun sovellus on käynnistetty aiempien ohjeiden mukaan, käyttäjälle avautuu valikkonäkymä. Valikkonäkymässä on labyrintteja, joista käyttäjä voi valita haluamansa labyrintin, jossa algoritmit esitetään. Labyrintteja voi selata valikkonäkymässä `nuoli ylös- ja alaspäin`-näppäimillä. Labyrintin voi valita painamalla `enter`. Kun käyttäjä on valinut labyrintin, avautuu uusi näkymä, jossa on kaksi labyrinttia, joissa algoritmit esitetään. Ensin aloittaa Dead-end filling algoritmi ja kun se on päässyt loppuun, Tremauxin algoritmi aloittaa automaattisesti viereisessä labyrintissa. Algoritmien etenemisen voi lopettaa 1. painamalla `m`-näppäintä, jolloin sovellus palaa valikkonäkymään tai 2. painamalla `rastia` ikkunan oikeassa ylänurkassa tai vaihtoehtoisesti `esc`-näppäintä, jolloin pygame ikkuna sulkeutuu ja samalla sovellus sulkeutuu. Valikkonäkymästä sovelluksen sulkeminen tapahtuu niinikään painamalla `rastia` tai `esc`-näppäintä. Jos molemmat algoritmit pääsevät loppuun ilman keskeytyksiä, ratkaistut labyrintit jäävät näkyviin kunnes käyttäjä sulkee sovelluksen tai palaa takaisin valikkonäkymään edelleen samalla `m`-näppäimellä. Sovellus ei ota vastaan muita kuin edellä mainittuja syötteitä.

### Testausohje
Yksikkötestit voi suorittaa komennolla `poetry run coverage run --branch -m pytest src`, jonka jälkeen testikattavuusraportin saa suorittamalla komento `poetry run coverage html`. Lisää testauksesta [testausdokumentissa]((https://github.com/sannituomisto/tiralabra-labyrintti/blob/main/dokumentit/testausdokumentti.md))
