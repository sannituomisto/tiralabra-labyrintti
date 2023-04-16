"""Sovelluksen käyttöliittymän toiminnasta vastaava moduuli."""
import os
from front_end.sovelluksen_toiminnot import nayta_toiminnot
from front_end.nayta_labyrintti import labyrintin_teko
from front_end.dead_end_filling_alg import nayta_dead_end_filling
from front_end.tremaux_alg import nayta_tremaux
from front_end.vertaile import vertaile_algoritmeja


class Sovellus:
    """Luokka, joka vastaa sovelluksen toiminnasta
    """

    def suorita(self):
        """Käynnistää sovelluksen käyttöliittymän
        """
        os.system("clear")
        while True:
            print('\r')
            print("LABYRINTTISOVELLUS")
            print('\r')
            print("Käyttöliittymä keskeneräinen ja tällä hetkellä vain sellainen, että näen algoritmien toimivan oikein.")
            print("Pygame ikkunaa ei saa tai voi sulkea ennen kuin algoritmi on päättynyt eikä terminaaliin saa kirjoittaa")
            print("samalla kuin pygame ikkuna on auki.")
            print('\r')
            nayta_toiminnot()
            print('\r')
            kayttajan_syote = input("")
            if kayttajan_syote == '1':
                os.system("clear")
                break
            if kayttajan_syote == '2':
                os.system("clear")
                try:
                    labyrintin_teko()
                except:
                    print('\r')
                    print(
                        'Labyrinttia ei voitu näyttää. Syötithän labyrintin numeron 1-5?')
            elif kayttajan_syote == "3":
                os.system("clear")
                try:
                    print(
                        'Valitse labyrintti, jonka haluat ratkaista dead end filling- algoritmilla.')
                    nayta_dead_end_filling()
                except:
                    print('\r')
                    print(
                        'Algoritmia ei voitu suorittaa. Syötithän labyrintin numeron 1-5?')
            elif kayttajan_syote == "4":
                os.system("clear")
                try:
                    print(
                        'Valitse labyrintti, jonka haluat ratkaista Tremauxin algoritmilla.')
                    nayta_tremaux()
                except:
                    print('\r')
                    print(
                        'Algoritmia ei voitu suorittaa. Syötithän labyrintin numeron 1-5?')
            elif kayttajan_syote == "5":
                os.system("clear")
                vertaile_algoritmeja()
            else:
                os.system("clear")
                print('Toimintoa ei löytynyt.')
