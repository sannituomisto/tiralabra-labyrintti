# Generoidaan labyrintti käyttäen satunnaistettua (randomized) Primin Algoritmia.
# Koodi perustuu Orestis Zekain "Fun With Python #1: Maze Generator" artikkelissa esitellyyn labyrintin generointi esimerkkiin. 
# Itse olen muuttanut rakennetta ja suomentanut koodia sekä muuttaanut visuaalisia yksityiskohtia.

import random

"""Ymmpäröivien solujen määrä"""
def ymparoivat_solut(labyrintti, random_seina):
    v_solut = 0
    if (labyrintti[random_seina[0]-1][random_seina[1]] == '*'):
        v_solut += 1
    if (labyrintti[random_seina[0]+1][random_seina[1]] == '*'):
        v_solut += 1
    if (labyrintti[random_seina[0]][random_seina[1]-1] == '*'):
        v_solut +=1
    if (labyrintti[random_seina[0]][random_seina[1]+1] == '*'):
        v_solut += 1

    return v_solut


"""Labyrintin generointi"""
def generoidaan_labyrintti(leveys, korkeus):
    seina = '@'
    solu = '*'
    ei_kayty = 'u'
    labyrintti = []

    """Tehdään tyhjä labyrintti ja merkitään kaikki solut käymättömiksi"""
    for i in range(0, korkeus):
        line = []
        for j in range(0, leveys):
            line.append(ei_kayty)
        labyrintti.append(line)

    """Valitaan satunnainen aloituspiste labyrintin generointiin ja varmistetaan että se ei ole labyrintin reunalla"""
    alku_korkeus = int(random.random()*korkeus)
    alku_leveys = int(random.random()*leveys)
    if (alku_korkeus == 0):
        alku_korkeus += 1
    if (alku_korkeus == korkeus-1):
        alku_korkeus -= 1
    if (alku_leveys == 0):
        alku_leveys += 1
    if (alku_leveys == leveys-1):
        alku_leveys -= 1

    """Merkitään aloitussolu poluksi ja sitä ympäröivät seinät seinälistalle"""
    labyrintti[alku_korkeus][alku_leveys] = solu
    seinat = []
    seinat.append([alku_korkeus - 1, alku_leveys])
    seinat.append([alku_korkeus, alku_leveys - 1])
    seinat.append([alku_korkeus, alku_leveys + 1])
    seinat.append([alku_korkeus + 1, alku_leveys])

    """Tässä vaiheessa merkitään aloitussolun ympäröivät lohkot seiniksi"""
    labyrintti[alku_korkeus-1][alku_leveys] = '@'
    labyrintti[alku_korkeus][alku_leveys - 1] = '@'
    labyrintti[alku_korkeus][alku_leveys + 1] = '@'
    labyrintti[alku_korkeus + 1][alku_leveys] = '@'

    """Generoidaan labyrintti aloitussolusta lähtien"""
    while seinat:
        random_seina = seinat[int(random.random()*len(seinat))-1]

        if (random_seina[1] != 0):
            if (labyrintti[random_seina[0]][random_seina[1]-1] == 'u' and labyrintti[random_seina[0]][random_seina[1]+1] == '*'):
                v_solut = ymparoivat_solut(labyrintti, random_seina)

                if (v_solut < 2):
                    labyrintti[random_seina[0]][random_seina[1]] = '*'

                    if (random_seina[0] != 0):
                        if (labyrintti[random_seina[0]-1][random_seina[1]] != '*'):
                            labyrintti[random_seina[0]-1][random_seina[1]] = '@'
                        if ([random_seina[0]-1, random_seina[1]] not in seinat):
                            seinat.append([random_seina[0]-1, random_seina[1]])

                    if (random_seina[0] != korkeus-1):
                        if (labyrintti[random_seina[0]+1][random_seina[1]] != '*'):
                            labyrintti[random_seina[0]+1][random_seina[1]] = '@'
                        if ([random_seina[0]+1, random_seina[1]] not in seinat):
                            seinat.append([random_seina[0]+1, random_seina[1]])

                    if (random_seina[1] != 0):	
                        if (labyrintti[random_seina[0]][random_seina[1]-1] != '*'):
                            labyrintti[random_seina[0]][random_seina[1]-1] = '@'
                        if ([random_seina[0], random_seina[1]-1] not in seinat):
                            seinat.append([random_seina[0], random_seina[1]-1])
                    

                for seina in seinat:
                    if (seina[0] == random_seina[0] and seina[1] == random_seina[1]):
                        seinat.remove(seina)

                continue

        if (random_seina[0] != 0):
            if (labyrintti[random_seina[0]-1][random_seina[1]] == 'u' and labyrintti[random_seina[0]+1][random_seina[1]] == '*'):

                v_solut = ymparoivat_solut(labyrintti, random_seina)
                if (v_solut < 2):
                    labyrintti[random_seina[0]][random_seina[1]] = '*'

                    if (random_seina[0] != 0):
                        if (labyrintti[random_seina[0]-1][random_seina[1]] != '*'):
                            labyrintti[random_seina[0]-1][random_seina[1]] = '@'
                        if ([random_seina[0]-1, random_seina[1]] not in seinat):
                            seinat.append([random_seina[0]-1, random_seina[1]])

                    if (random_seina[1] != 0):
                        if (labyrintti[random_seina[0]][random_seina[1]-1] != '*'):
                            labyrintti[random_seina[0]][random_seina[1]-1] = '@'
                        if ([random_seina[0], random_seina[1]-1] not in seinat):
                            seinat.append([random_seina[0], random_seina[1]-1])

                    if (random_seina[1] != leveys-1):
                        if (labyrintti[random_seina[0]][random_seina[1]+1] != '*'):
                            labyrintti[random_seina[0]][random_seina[1]+1] = '@'
                        if ([random_seina[0], random_seina[1]+1] not in seinat):
                            seinat.append([random_seina[0], random_seina[1]+1])

                for seina in seinat:
                    if (seina[0] == random_seina[0] and seina[1] == random_seina[1]):
                        seinat.remove(seina)

                continue

        if (random_seina[0] != korkeus-1):
            if (labyrintti[random_seina[0]+1][random_seina[1]] == 'u' and labyrintti[random_seina[0]-1][random_seina[1]] == '*'):

                v_solut = ymparoivat_solut(labyrintti, random_seina)
                if (v_solut < 2):
                    labyrintti[random_seina[0]][random_seina[1]] = '*'

                    if (random_seina[0] != korkeus-1):
                        if (labyrintti[random_seina[0]+1][random_seina[1]] != '*'):
                            labyrintti[random_seina[0]+1][random_seina[1]] = '@'
                        if ([random_seina[0]+1, random_seina[1]] not in seinat):
                            seinat.append([random_seina[0]+1, random_seina[1]])
                    if (random_seina[1] != 0):
                        if (labyrintti[random_seina[0]][random_seina[1]-1] != '*'):
                            labyrintti[random_seina[0]][random_seina[1]-1] = '@'
                        if ([random_seina[0], random_seina[1]-1] not in seinat):
                            seinat.append([random_seina[0], random_seina[1]-1])
                    if (random_seina[1] != leveys-1):
                        if (labyrintti[random_seina[0]][random_seina[1]+1] != '*'):
                            labyrintti[random_seina[0]][random_seina[1]+1] = '@'
                        if ([random_seina[0], random_seina[1]+1] not in seinat):
                            seinat.append([random_seina[0], random_seina[1]+1])

                for seina in seinat:
                    if (seina[0] == random_seina[0] and seina[1] == random_seina[1]):
                        seinat.remove(seina)


                continue

        if (random_seina[1] != leveys-1):
            if (labyrintti[random_seina[0]][random_seina[1]+1] == 'u' and labyrintti[random_seina[0]][random_seina[1]-1] == '*'):

                v_solut = ymparoivat_solut(labyrintti, random_seina)
                if (v_solut < 2):
                    labyrintti[random_seina[0]][random_seina[1]] = '*'

                    if (random_seina[1] != leveys-1):
                        if (labyrintti[random_seina[0]][random_seina[1]+1] != '*'):
                            labyrintti[random_seina[0]][random_seina[1]+1] = '@'
                        if ([random_seina[0], random_seina[1]+1] not in seinat):
                            seinat.append([random_seina[0], random_seina[1]+1])
                    if (random_seina[0] != korkeus-1):
                        if (labyrintti[random_seina[0]+1][random_seina[1]] != '*'):
                            labyrintti[random_seina[0]+1][random_seina[1]] = '@'
                        if ([random_seina[0]+1, random_seina[1]] not in seinat):
                            seinat.append([random_seina[0]+1, random_seina[1]])
                    if (random_seina[0] != 0):	
                        if (labyrintti[random_seina[0]-1][random_seina[1]] != '*'):
                            labyrintti[random_seina[0]-1][random_seina[1]] = '@'
                        if ([random_seina[0]-1, random_seina[1]] not in seinat):
                            seinat.append([random_seina[0]-1, random_seina[1]])

                for seina in seinat:
                    if (seina[0] == random_seina[0] and seina[1] == random_seina[1]):
                        seinat.remove(seina)

                continue

        for seina in seinat:
            if (seina[0] == random_seina[0] and seina[1] == random_seina[1]):
                seinat.remove(seina)
            

    for i in range(0, korkeus):
        for j in range(0, leveys):
            if (labyrintti[i][j] == 'u'):
                labyrintti[i][j] = '@'

    for i in range(0, leveys):
        if (labyrintti[1][i] == '*'):
            labyrintti[0][i] = '*'
            break

    for i in range(leveys-1, 0, -1):
        if (labyrintti[korkeus-2][i] == '*'):
            labyrintti[korkeus-1][i] = '*'
            break
        
    return labyrintti
