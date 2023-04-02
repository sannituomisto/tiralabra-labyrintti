import os
from front_end.sovelluksen_toiminnot import nayta_toiminnot
from front_end.nayta_labyrintti import labyrintin_teko
from front_end.dead_end_filling_alg import nayta_dead_end_filling
from front_end.tremaux_alg import nayta_tremaux
from front_end.vertaile import vertaile_algoritmeja


class Sovellus:
    def suorita(self):
        os.system("clear")
        print("LABYRINTTISOVELLUS")
        while True:
            print('\r')
            nayta_toiminnot()
            print('\r')
            kayttajan_syote = input("")
            if kayttajan_syote == '1':
                os.system("clear")
                break
            elif kayttajan_syote == '2':
                os.system("clear")
                try:
                    labyrintin_teko()
                except:
                    print('\r')
                    print('Labyrinttia ei voitu näyttää. Annoithan labyrintin numeron 1-10?')
            elif kayttajan_syote == "3":
                os.system("clear")
                try:
                    nayta_dead_end_filling()
                except:
                    print('\r')
                    print('Algoritmia ei voitu suorittaa. Annoithan labyrintin numeron 1-10?')
            elif kayttajan_syote == "4":
                os.system("clear")
                nayta_tremaux()
            elif kayttajan_syote == "5":
                os.system("clear")
                vertaile_algoritmeja()
            else:
                os.system("clear")
                print('Toimintoa ei löytynyt.')
