# Määrittelydokumentti

## MÄÄRITTELYDOKUMENTTIIN TULOSSA MUUTOKSIA

Ohjelmointikieli: Python (en hallitse vielä muita) \
Opinto-ohjelma: tietojenkäsittelytieteen kandidaatti (TKT) \
Kieli: suomi

Tarkoituksena on tehdä sovellus, joka löytää lyhimmän reitin labyrintistä ulos. Labyrintin ratkaisemiseen käytetään Dijkstran sekä Jump Point Search (8 suuntaan kulku) algoritmia. Sovelluksessa vertaillaan näitä kahta reitinhakualgoritmia.

Molemmissa Dijkstran ja JPS algoritmeissa käytetään tietorakenteina prioriteettijonoa. Prioriteettijono toteutetaan binäärikekona. Sovelluksessa tulen myös tarvitsemaan hajautustauluja (Pythonin sanakirja) ja listoja.

Tässä sovelluksessa ratkaisen siis ongelmaa "Miten löydetään tehokkaasti lyhin reitti labyrintistä ulos?". Valitsin kyseiset algoritmit, koska JPS algoritmin pitäisi olla tehokkaampi kuin Dijkstran algoritmi, joten toivottavasti tämä ero näkyy myös sovelluksessa, kun verrataan algoritmeja. Toisaalta JPS:n tehokkuus ymmärtääkseni tulee paremmin esiin suuremmassa ruudukossa, jossa ei ole paljoa esteitä mutta on silti mielenkiintoista nähdä miten algoritmit eroavat tehokkuudeltaan tässä kyseisessä ongelmassa. Tietorakenteet valitsin pienen taustatutkimuksen jälkeen. Prioriteettijonon toteutukseen valitsin binäärikeon, koska se on usein käytetty tietorakenne prioriteettijonon toteutuksessa.

Käyttäjä antaa sovellukselle syötteenä haluamansa labyrintin koon, valitsee kumpaa algoritmia haluaa käyttää ja käynnistää reitinhaun. Labyrintistä etsitään siis lyhin reitti lähtösolmusta päätesolmuun ja käyttäjälle näytetään tämän reitin siirtymien määrä ja itse reitti ainakin labyrintin koordinaateilla mutta tarkoituksena olisi myös tehdä toiminto, jolla käyttäjä näkee reitin labyrintissa.

Prioriteettijonoa käyttämällä Dijkstran algoritmin aikavaatimus on O((|E|+|V|)log|V|), jossa E on kaarien määrä ja V on solmujen määrä. Tilavaatimus on O(|V|). En tässä vaiheessa osaa sanoa täysin varmasti JPS:n aika- ja tilavaatimuksista mutta ymmärtääkseni JPS:llä on periaatteessa sama aikavaatimus kuin Dijkstran algoritmilla mutta käytännössä sen pitäisi kuitenkin olla nopeampi. Tilavaatimus JPS:llä on ymmärtääkseni myös O(|V|).

## Lähteet
- [Wikipedia: A* search algorithm, luettu 18.3.2023](https://en.wikipedia.org/wiki/A*_search_algorithm)
- [Jump Search Algorithm in Python, luettu 18.3.2023](https://blog.finxter.com/jump-search-algorithm-in-python-a-helpful-guide-with-video/)
- [Wikipedia: Dijkstra's algorithm, luettu 18.3.2023](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [Polunetsintä ruudukkokartoilla, Tampereen yliopisto, luettu 18.3.2023](https://trepo.tuni.fi/bitstream/handle/10024/121424/PekkaOinas.pdf?sequence=2)
