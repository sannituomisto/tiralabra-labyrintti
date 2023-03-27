# Määrittelydokumentti

Ohjelmointikieli: Python (en hallitse vielä muita) \
Opinto-ohjelma: tietojenkäsittelytieteen kandidaatti (TKT) \
Kieli: suomi

Tarkoituksena on tehdä sovellus, joka vertailee kahta algoritmia labyrintin ratkaisemisessa. Labyrintin ratkaisemiseen käytetään DFS algoritmia sekä Dead end filling algoritmia. Sovelluksen tarkoituksena on vertailla kumpi näistä algoritmeista on tehokkaampi labyrintin ratkaisemiseen.

Molemmissa algoritmeissaa käytetään tietorakenteena pinoa.

Tässä sovelluksessa ratkaisen siis ongelmaa "Miten löydetään tehokkaasti nopein reitti ulos labyrintista?". Valitsin kyseiset algoritmit, koska Dead End Filling algoritmi ei ole aikaisemmin tullut vastaan ja on mielenkiintoista nähdä miten DFS toimii labyrinteissa. Toisaalta myös käytettäessä DFS labyrintin rakenteesta ei ole aiempaa tietoa mutta Dead End Filling käytetään, kun nähdään koko labyrintti. Uskon siis, että näiden algoritmien tehokkuuden vertailu voisi olla mielekästä.

Käyttäjä antaa sovellukselle syötteenä haluamansa labyrintin koon, jolloin sovellus luo labyrintin tekstigrafiikalla. Sen jälkeen käyttäjä voi aloittaa labyrintin ratkaisemisen kahdella eri algoritmilla ja tulokseksi käyttäjälle näytetään löydetty reitti labyrintissa, siirtymien määrä ja aika reitin löytämiseen.

DFS algoritmin aikavaatimus on O(|V| + |E|), jossa E on kaarien määrä ja V on solmujen määrä. Dead end filling aikavaatimuksesta ei tässä vaiheessa
ole tietoa. Tilavaatimus molemissa on O(|V|).

## Lähteet
- [Wikipedia: Maze-solving algorithm, luettu 27.3.2023](https://en.wikipedia.org/wiki/Maze-solving_algorithm)
- [Solving mazes with Depth-First Search, luettu 18.3.2023](https://medium.com/swlh/solving-mazes-with-depth-first-search-e315771317ae)
- [Wikipedia: Depth-first search, luettu 27.3.2023](https://en.wikipedia.org/wiki/Depth-first_search)
