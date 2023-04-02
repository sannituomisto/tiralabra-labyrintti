from collections import deque

def etsi_umpikujat(labyrintti, koko):
    umpikujat=[]
    for i in range(1, koko-1):
        for j in range(1, koko-1):
            v_ruudut=ymparoivat_ruudut(labyrintti, i, j)
            if labyrintti[i][j] != "@" and v_ruudut.count("@") >= 3:
                umpikujat.append((i,j))
                labyrintti[i][j] = 'u'
    return taytetaan_umpikujat(umpikujat,labyrintti,koko)


def ymparoivat_ruudut(labyrintti, i, j):
        v_ruudut = []
        v_ruudut.append(labyrintti[i-1][j])
        v_ruudut.append(labyrintti[i+1][j])
        v_ruudut.append(labyrintti[i][j-1])
        v_ruudut.append(labyrintti[i][j+1])
        return v_ruudut

def taytetaan_umpikujat(umpikujat, labyrintti, koko):
    jono=deque()
    for umpikuja in umpikujat:
        jono.append(umpikuja)
        while len(jono) > 0:
            ruutu = jono.popleft()
            labyrintti[ruutu[0]][ruutu[1]] = '#'
            for siirto in [(0,1),(0,-1),(1,0),(-1,0)]:
                uusi_ruutu = (ruutu[0]+siirto[0],ruutu[1]+siirto[1])
                if uusi_ruutu[0] == koko-1 or uusi_ruutu[1] == koko-1:
                    continue
                v_ruudut=ymparoivat_ruudut(labyrintti, uusi_ruutu[0], uusi_ruutu[1])
                if v_ruudut.count(".") > 1:
                    continue
                if labyrintti[uusi_ruutu[0]][uusi_ruutu[1]] == "@":
                    continue
                if labyrintti[uusi_ruutu[0]][uusi_ruutu[1]] == ".":
                    jono.append(uusi_ruutu)
    return labyrintti, umpikujat
         
          
def umpikujat_labyrinttiin(labyrintti, umpikujat):
    for umpikuja in umpikujat:
        labyrintti[umpikuja[0]][umpikuja[1]] = 'u'
    return labyrintti


# if __name__ == "__main__":
#     labyrintti=[['@', '.', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'], ['@', '.', '@', '.', '.', '.', '.', '.', '.', '.', '.', '@', '.', '.', '.', '.', '.', '.', '.', '@'], ['@', '.', '@', '.', '@', '@', '@', '@', '@', '@', '@', '@', '.', '@', '@', '@', '@', '@', '@', '@'], ['@', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '@'], ['@', '@', '.', '@', '@', '@', '@', '@', '.', '@', '@', '@', '@', '@', '@', '@', '@', '@', '.', '@'], ['@', '.', '.', '@', '.', '.', '.', '.', '.', '@', '@', '.', '.', '.', '.', '@', '@', '@', '.', '@'], ['@', '@', '.', '@', '@', '@', '@', '@', '.', '@', '@', '@', '@', '@', '.', '.', '.', '.', '.', '@'], ['@', '.', '.', '.', '.', '.', '@', '@', '.', '@', '@', '@', '.', '@', '.', '@', '@', '@', '.', '@'], ['@', '@', '.', '@', '@', '@', '@', '@', '.', '.', '.', '@', '.', '@', '.', '@', '.', '@', '.', '@'], ['@', '.', '.', '@', '.', '.', '.', '@', '@', '@', '.', '@', '.', '@', '.', '@', '.', '@', '@', '@'], ['@', '@', '.', '@', '@', '.', '@', '@', '.', '@', '.', '@', '.', '@', '.', '.', '.', '.', '.', '@'], ['@', '.', '.', '.', '.', '.', '@', '@', '.', '@', '.', '@', '.', '@', '@', '.', '@', '@', '.', '@'], ['@', '@', '.', '@', '@', '.', '@', '@', '.', '@', '.', '@', '.', '@', '@', '@', '@', '@', '.', '@'], ['@', '@', '@', '@', '@', '@', '@', '@', '.', '.', '.', '@', '.', '@', '@', '.', '.', '.', '.', '@'], ['@', '.', '.', '.', '.', '.', '@', '@', '.', '@', '@', '@', '.', '@', '@', '.', '@', '@', '@', '@'], ['@', '.', '@', '@', '@', '.', '@', '@', '.', '@', '.', '.', '.', '.', '.', '.', '.', '.', '.', '@'], ['@', '.', '@', '.', '@', '.', '@', '@', '.', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'], ['@', '.', '@', '.', '@', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '@'], ['@', '.', '.', '.', '@', '.', '@', '@', '.', '@', '@', '@', '.', '@', '@', '.', '@', '@', '.', '@'], ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '.', '@']]
#     koko=20
#     print(etsi_umpikujat(labyrintti,koko))