# Viikkoraportti 3

Tein tällä viikolla sovelluksen käyttöliittymän toimivampaan muotoon. Lisäsin sovellukseen valmiiksi erikokoisia labyrintteja ja toteutin niiden
lukemiseen tarvittavat toiminnot. Tein myös dead end filling-algoritmin ainakin siihen asti, että käyttäjälle tulostuu labyrintti, jossa on umpikujat ja labyrintti, jossa on lopullinen ratkaisu.
Aloitin testauksen mutta dead end filling- algoritmin testaus jäi vielä puuttumaan, sillä en keksinyt hyvää tapaa lähteä testaamaan sitä. Testikattavuus on nyt myös käytössä
ja lisäsin GitHub Actions ja Codecov (en ymmärrä miksi Codecov ei ota dead end filling tiedostoa mukaan kattavuusraporttiin koska ei se 100% ole). Lisäsin koodiin myös kommentteja ja tehtävät (tasks)

Ohjelma edistyi käyttöliittymän osalta sekä dead end filling- algoritmin osalta ja myös testauksen osalta.

Opin tällä viikolla, että testaukseen täytyy varata lisää aikaa. 

Vaikeuksia oli dead end filling algoritmin testauksen kanssa. Jätin liian vähän aikaa sen miettimiseen ja se ei ollutkaan niin yksinkertaista. Epäselväksi jäi
vähän se, että mistä tedän että tekemäni algoritmi toimii oikein tai, että olen tehnyt sen tehokkaalla tavalla. Tein dead end filling algoritmin ohjeen
mukaan eli että ensin etsitään umpikujat ja sitte täytetään umpikujat kunnes tulee risteys. Kaikissa labyrinteissa algoritmi löytää umpikujat ja tuottaa oikean polun mutta
siitä en ole varma teinkö sen liian monimutkaisesti ja epätehokkaasti. Epäselväksi jäi myös, että miksi Codecov näyttää 100% eikä ota dead_end_algoritmi tiedostoa mukaan.

Seuraavaksi lisään dead end filling- algoritmiin ajanottamisen ja ryhdyn tekemään Tremauxin algoritmia. Jätän seuravalla viikolla enemmän aikaa testaukseen ja teen testit
niille osille, jotka tällä viikolla jäi puuttumaan.

Kysymyksiä:
- Minkälaisen tuloksen käyttäjän pitäisi saada algoritmin tehokkuudesta ja toimivuudesta (esim. aika, reitti, ratkaisu polun pituus)? Varmaan paras olisi se, että
käyttäjä näkisi miten reitti muodostuu livenä mutta uskon että minulla menisi siihen liian kauan aikaa. 
- Pitääkö käyttöliittymää testata?
