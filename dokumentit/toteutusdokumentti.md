# Toteutusdokumentti
### Ohjelman yleisrakenne 
Sovelluksen päätoiminta on sijoitettu `src` kansioon. Sovellus käynnistyy tiedostosta `main.py`, joka avaa sovelluksen valikkonäkymän Pygame-ikkunaan. `main.py` tiedosto hallitsee sovelluksen toimintaa. Valikkonäkymän toiminnoista vastaa `Menu` luokka. Kun käyttäjä on valinnut haluamansa labyrintin valikkonäkymässä, avautuu uusi näkymä, jossa molemmat algoritmit visualisoidaan vierekkäin mutta eri aikaa käyttäjän valitsemassa labyrintissa. `Labyrinth` luokassa piirretään käyttäjän valitsema labyrintti kahteen eri kohtaan näyttöä ja päivitetään labyrintteja algoritmien edetessä askel askeleelta. `Labyrinth` luokassa myös haetaan labyrtintit tiedostosta. `Labyrinth` luokkassa on siis kaikki labyrintteihin liittyvä toiminta. `DeadEndFilling` luokkassa suoritetaan Dead-end filling algoritmi ja `Tremaux` luokassa Tremauxin algoritmi. Lisäksi on `handle_event_algorithm_view.py` tiedosto, joka liittyy ainoastaan  pygame ikkunan tapahtumien käsittelyyn. Labyrintit on sijoitettu kansioon `20x20labyrinths`, josta ne haetaan aina tarvittaessa. `tests` kansiossa on algoritmien oikeellisuustestit ja `dokumentit` kansiossa on sovelluksen dokumentaatio.

### Saavutetut aika- ja tilavaativuudet
#### Dead-end filling
Saavutettu aikavaatimus: O(n), jossa n on solmujen määrä eli solmujen määrään nähden.
Saavutettu tilavaatimus: O(|V|), jossa V on solmujen määrä.


#### Tremaux
Saavutettu aikavaatimus: O(n), jossa n on solmujen määrä eli solmujen määrään nähden.
Saavutettu tilavaatimus: O(|V|), jossa V on solmujen määrä.


### Työn mahdolliset puutteet ja parannusehdotukset
Sovellus näyttää kuormittavan tietokonetta jonkin verran, mikä oman näkemyksen mukaan liittyy luultavimmin Pygamen toimintaan/toteutukseen joten tähän voisi löytyä parempia ratkaisuja. Sovellusta voisi laajentaa myös helposti esimerkiksi lisäämällä erikokoisia labyrintteja, sillä tällä hetkellä sovelluksessa on vain yhden kokoisia labyrintteja.

### Lähteet
- [Wikipedia: Maze-solving algorithm, viim. luettu 9.5.2023](https://en.wikipedia.org/wiki/Maze-solving_algorithm)
- [Astrolog.org, viim. luettu 9.5.2023](https://www.astrolog.org/labyrnth/algrithm.htm)
- [Youtube: Trémaux's algorithm, viim. katsottu 9.5.2023](https://www.youtube.com/watch?v=MxUkDpVLOmc)
- [Wikipedia: Depth-first search, viim luettu 9.5.2023](https://en.wikipedia.org/wiki/Depth-first_search)