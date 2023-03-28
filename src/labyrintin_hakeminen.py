def labyrintin_haku(labyrintin_nro):
        with open("labyrintti"+str(labyrintin_nro)+".txt") as tiedosto:
                labyrintti=[]
                for rivi in tiedosto:
                        rivi = rivi.replace("\n", "")
                        labyrintti.append(rivi)
        return labyrintti

