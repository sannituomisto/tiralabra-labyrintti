def labyrintin_haku(labyrintin_nro):
        labyrintti=[]
        if labyrintin_nro <= 5:
                with open("20x20labyrintit/labyrintti"+str(labyrintin_nro)+".txt") as tiedosto:
                        for rivi in tiedosto:
                                rivi = rivi.replace("\n", "")
                                labyrintti.append(list(rivi))
        else:
                with open("100x100labyrintit/labyrintti"+str(labyrintin_nro)+".txt") as tiedosto:
                        for rivi in tiedosto:
                                rivi = rivi.replace("\n", "")
                                labyrintti.append(list(rivi))
        return labyrintti
        
        # Ei näy terminaalissa järkevästi, joten 150x150 labyrintit ei välttämättä tule sovellukseen. Toisaalta aikavertailussa olisi hyviä.
        # else:
        #         with open("150x150labyrintit/labyrintti"+str(labyrintin_nro)+".txt") as tiedosto:
        #                 for rivi in tiedosto:
        #                         rivi = rivi.replace("\n", "")
        #                         labyrintti.append(list(rivi))
        # return labyrintti

