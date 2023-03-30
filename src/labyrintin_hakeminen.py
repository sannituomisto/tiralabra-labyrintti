def labyrintin_haku(labyrintin_nro):
        if labyrintin_nro <= 5:
                with open("20x20labyrintit/labyrintti"+str(labyrintin_nro)+".txt") as tiedosto:
                        labyrintti=[]
                        for rivi in tiedosto:
                                rivi = rivi.replace("\n", "")
                                labyrintti.append(rivi)
        else:
                with open("100x100labyrintit/labyrintti"+str(labyrintin_nro)+".txt") as tiedosto:
                        labyrintti=[]
                        for rivi in tiedosto:
                                rivi = rivi.replace("\n", "")
                                labyrintti.append(rivi)
        return labyrintti
        
        # Ei näy terminaalissa järkevästi, joten 150x150 labyrintit ei välttämättä tule sovellukseen. Toisaalta aikavertailussa olisi hyviä.
        # else:
        #         with open("150x150labyrintit/labyrintti"+str(labyrintin_nro)+".txt") as tiedosto:
        #                 labyrintti=[]
        #                 for rivi in tiedosto:
        #                         rivi = rivi.replace("\n", "")
        #                         labyrintti.append(rivi)
        # return labyrintti