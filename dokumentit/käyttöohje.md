# Käyttöohje
### Käynnistysohje
1.  Kloonaa repositorio koneellesi ja siirry projektin juurikansioon.
2.  Asenna projektin riippuvuudet komennolla `poetry install`.
3.  Käynnistä sovellus projektin juurikansiossa komennolla `python3 src/main.py`.

### Toiminnallisuudet
Kun sovellus on käynnistetty aiempien ohjeiden mukaan, käyttäjälle avautuu valikkonäkymä. Valikkonäkymässä on labyrintteja, joista käyttäjä voi valita haluamansa labyrintin, jossa algoritmit esitetään. Labyrintteja voi selata valikkonäkymässä `nuoli ylös- ja alaspäin`-näppäimillä. Labyrintin voi valita painamalla `enter`. Kun käyttäjä on valinut labyrintin, avautuu uusi näkymä, jossa on kaksi labyrinttia, joissa algoritmit esitetään. Ensin aloittaa Dead-end filling algoritmi ja kun tämä on päässyt loppuun, Tremauxin algoritmi aloittaa automaattisesti toisessa labyrintissa.
