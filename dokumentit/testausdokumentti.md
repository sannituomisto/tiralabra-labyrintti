# Testausdokumentti

[![codecov](https://codecov.io/gh/sannituomisto/tiralabra-labyrintti/branch/main/graph/badge.svg?token=7V5900RYNR)](https://codecov.io/gh/sannituomisto/tiralabra-labyrintti)

Projektissa testataan algoritmien toimintaa eli käytännössä `DeadEndFilling` ja `Tremaux` luokkia. Käyttöliittymä ja algoritmien visualisointi on jätetty testien ulkopuolelle. Testaus toteutetaan unittesteillä.

### Dead-end Filling algoritmin testaus
Testauksessa käytetään käsin tehtyjä labyrintteja, joista on etsitty käsin umpikujat, umpikujista lähtevät polut sekä tehty käsin ratkaistu labyrintti.
1. testi testaa löytääkö algoritmi umpikujien koordinaatit labyrintissa, jossa on silmukoita ja vertaa tuloksia käsin laadittuihin tuloksiin.
2. testi testaa löytääkö algoritmi umpikujista lähtevien polkujen koodinaatit aina seuraavaan risteykseen asti labyrintissa, jossa on silmukoita ja vertaa tuloksia käsin laadittuihin
   tuloksiin.
3. testi testaa lopullista labyrinttia eli löytääkö algoritmi oikein polut ulos labyrintista, jossa on silmukoita ja vertaa tuloksia käsin laadittuihin tuloksiin. 
4. testi testaa algoritmia labyrintissa, jossa ei ole umpikujia eli tällöin algoritmin ei tulisi löytää umpikujia labyrintista.
5. testi testaa algoritmia labyrintissa, jossa ei ole umpikujia, jolloin algoritmin ei tulisi tehdä labyrintiin mitään.
6. testi testaa lopullista labyrinttia tilanteessa, jossa labyrintissa ei ole polkua ulos eli ei ole ratkaisua eli tällöin kaikki polut tulee olla täytetty.

### Tremauxin algoritmin testaus
Testauksessa käytetään käsin tehtyjä labyrintteja, joista on etsitty käsin polut ulos labyrintista eli ratkaisut.
1. testi testaa löytääkö algoritmi yhden mahdollisista poluista ulos labyrintista, jossa on silmukoita ja vertaa tuloksia käsin laadittuihin tuloksiin.
2. testi testaa, että algoritmi löytää aloitus ja lopetusruudun oikein.
3. testi testaa algoritmia tilanteessa, jossa labyrintissa ei ole polkua ulos eli ratkaisua.

### Yksikkötestauksen ja kattavuusraportin tekeminen
Yksikkötestit voi suorittaa komennolla `poetry run coverage run --branch -m pytest src`, jonka jälkeen testikattavuusraportin saa suorittamalla komento `poetry run coverage html`. Testikattavuusraporttia voi lukea selaimessa avaamalla hakemiston htmlcov/index.html. \
Vaihtoehtoisesti kattavuusraportin voi tulostaa suoraan komentoriville komennolla `poetry run coverage report -m`. \
Projektin koodikattavuutta voi myös tarkastella Codecovin avulla painamalla dokumentin alussa olevaa Codecov-badgea.

### Yksikkötestauksen kattavuusraportti

![Screenshot from 2023-05-05 16-32-57](https://user-images.githubusercontent.com/101722915/236471872-27a4bd29-5a63-4aa5-bfad-795199339258.png)

***Huom!*** Dead-end filling ja Tremauxin algoritmin koodissa on pygame ikkunan tapahtumien käsittelyyn tarvittavaa koodia, joka ei liity algoritmin toimintaan. Tätä osaa koodista ei testata ja tämä alentaa haaraumakattavuutta.

### Pylint ja koodin laatu
Koodin laadun tarkistus voidaan tehdä suorittamalla komento `poetry run pylint src`.
