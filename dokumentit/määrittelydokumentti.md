# Määrittelydokumentti

Ohjelmointikieli: Python (en hallitse vielä muita) \
Opinto-ohjelma: tietojenkäsittelytieteen kandidaatti (TKT) \
Kieli: suomi

Tarkoituksena on tehdä sovellus, joka vertailee kahta algoritmia labyrintin ratkaisemisessa. Labyrintin ratkaisemiseen käytetään Dead end filling algoritmia ja Tremauxin algoritmia. Sovelluksen tarkoituksena on vertailla kumpi näistä algoritmeista on tehokkaampi labyrintin ratkaisemiseen.

Molemmissa algoritmeissaa käytetään tietorakenteena pinoa.

Tässä sovelluksessa ratkaisen siis ongelmaa "Miten löydetään tehokkaasti nopein reitti ulos labyrintista?". Valitsin kyseiset algoritmit, koska kumpikaan algoritmi ei ole aikaisemmin tullut vastaan ja ne vaikuttivat mielenkiintoisilta ja keskenään tarpeeksi erilaisilta. Käytettäessä Tremauxin algoritmia labyrintin rakenteesta ei ole aiempaa tietoa mutta Dead End Filling algoritmia taas käytetään, kun oletetaan, että nähdään koko labyrintti joten tässäkin asiassa algoritmeilla on jo eroa. Uskon siis, että näiden algoritmien tehokkuuden vertailu on mielekästä.

Sovelluksessa on valmiina tekstigrafiikalla itse tehtyjä labyrintteja. Käyttäjä antaa sovellukselle syötteenä haluamansa labyrintin numeron, jonka haluaa sovelluksen ratkaisevan. Käyttäjä voi myös nähdä eri labyrintit ennen ratkaisemista. Sen jälkeen käyttäjä voi aloittaa labyrintin ratkaisemisen kahdella eri algoritmilla ja tulokseksi käyttäjälle näytetään löydetyt reitit labyrintissa, siirtymien määrä ja aika reittien löytämiseen.

Tremauxin algoritmin aikavaatimus on O(|V| + |E|), jossa E on kaarien määrä ja V on solmujen määrä. Dead end filling aikavaatimuksesta ei tässä vaiheessa
ole tietoa. Tilavaatimus molemissa on O(|V|).

## Lähteet
- [Wikipedia: Maze-solving algorithm, luettu 27.3.2023](https://en.wikipedia.org/wiki/Maze-solving_algorithm)
