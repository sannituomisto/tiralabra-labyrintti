# Määrittelydokumentti

### Sovelluksen tarkoitus
Tässä sovelluksessa ratkaisen ongelmaa "Miten löydetään reitti ulos labyrintista?". Tarkoituksena on tehdä sovellus, joka vertailee Dead-end filling- ja Tremauxin algoritmia labyrintin ratkaisemisessa. Vertailun kohteena on siis algoritmien erilaiset toimintaperiaatteet labyrintin ratkaisemisessa. Molemmissa algoritmeissaa käytetään tietorakenteena pinoa, joka toteutetaan listarakenteen avulla.

### Miksi kyseiset algoritmit?
Valitsin kyseiset algoritmit, koska kumpikaan algoritmi ei ole aikaisemmin tullut vastaan ja ne vaikuttivat mielenkiintoisilta ja keskenään tarpeeksi erilaisilta, jotta vertailu on mielekästä. Käytettäessä Tremauxin algoritmia labyrintin rakenteesta ei ole aiempaa tietoa mutta Dead End Filling algoritmia taas käytetään, kun oletetaan, että nähdään koko labyrintti joten tässäkin asiassa algoritmeilla on jo eroa.

Kumpikaan algoritmi ei lupaa löytää lyhintä reittiä ulos. Dead-end filling algoritmi löytää ja näyttää kaikki mahdolliset reitit ulos, kun taas Tremauxin algoritmi näyttää vain yhden mahdollisista reiteistä ulos. Tremauxin algoritmi myös kyllä löytää kaikki reitit ulos mutta on satunnaista, minkä reitin se milloinkin valitsee. Kummatkin algoritmit toimivat siis labyrinteissa, joissa on silmukoita.

### Sovelluksen perustoiminta ja syötteet
Sovelluksessa on valmiina tekstigrafiikalla itse tehtyjä 20x20 kokoisia labyrintteja. Sovelluksen käyttöliittymä on tehty pygamella, jotta algoritmien toiminnan etenemistä voi seurata askel askeleelta. Käyttäjä valitsee labyrintin, jonka jälkeen algoritmien eteneminen näytetään vierekkäin, ensin Dead-end filling ja sen jälkeen Tremauxin algoritmi. Labyrintteja on erilaisia: labyrintteja, joissa on silmukoita; labyrintti, jossa on vain yksi reitti ulos ja labyrintti, jossa ei ole ratkaisua. Käyttäjän antamat syötteet liittyvät ainoastaan sovelluksen ohjaukseen.

### Tavoitellut aika- ja tilavaatimukset
Tremauxin algoritmin aikavaatimus on O(|V| + |E|), jossa E on kaarien määrä ja V on solmujen määrä. Dead end filling aikavaatimuksesta ei tässä vaiheessa
ole tietoa. Tilavaatimus molemissa on O(|V|).

### Lähteet
- [Wikipedia: Maze-solving algorithm, luettu 27.3.2023](https://en.wikipedia.org/wiki/Maze-solving_algorithm)
