"""Dead end filling-algoritmin toiminnasta vastaava moduuli."""
from collections import deque


def dead_end_filling(labyrintti, koko):
    """Kokoaa algoritmin vaiheet yhteen.

    Args:
        labyrintti (lista): labyrintti
        koko (int): labyrintin leveys ja korkeus

    Returns:
        Ratkaistu labyrintti ja labyrintin umpikujien koordinaatit listassa.
    """
    umpikujat = etsi_umpikujat(labyrintti, koko)
    ratkaistu_labyrintti = taytetaan_umpikujat(umpikujat, labyrintti, koko)
    return ratkaistu_labyrintti, umpikujat


def etsi_umpikujat(labyrintti, koko):
    """Etsii lapyrintin umpikujat.

    Args:
        labyrintti (lista): labyrintti
        koko (int): labyrintin leveys ja korkeus

    Returns:
        Labyrintin umpikujien koordinaatit listassa.
    """
    umpikujat = []
    for i in range(1, koko-1):
        for j in range(1, koko-1):
            v_ruudut = ymparoivat_ruudut(labyrintti, i, j)
            if labyrintti[i][j] != "@" and v_ruudut.count("@") >= 3:
                umpikujat.append((i, j))
                labyrintti[i][j] = 'u'
    return umpikujat


def ymparoivat_ruudut(labyrintti, i, j):
    """Etsii ruudun ympäröivät ruudut (pohjoinen, itä, etelä ja länsi)

    Args:
        labyrintti (lista): labyrintti
        i (int): labyrintin ruudun korkeus koordinaatti
        j (int): labyrintin ruudun leveys koordinaatti

    Returns:
        Ruudun ympäröivät ruudut.
    """
    v_ruudut = []
    v_ruudut.append(labyrintti[i-1][j])
    v_ruudut.append(labyrintti[i+1][j])
    v_ruudut.append(labyrintti[i][j-1])
    v_ruudut.append(labyrintti[i][j+1])
    return v_ruudut


def taytetaan_umpikujat(umpikujat, labyrintti, koko):
    """Täyttää labyrintin polkuja umpikujista lähtien kunnes vain ratkaisu on jäljellä.

    Args:
        umpikujat (lista): labyrintin umpikujat
        labyrintti (lista): labyrintti
        koko (int): labyrintin korkeus ja leveys

    Returns:
        Labyrintin, jossa umpikujat ovat täytetty seinillä ja vain ratkaisu polku on jäljellä.
    """
    jono = deque()
    for umpikuja in umpikujat:
        jono.append(umpikuja)
        while len(jono) > 0:
            ruutu = jono.popleft()
            labyrintti[ruutu[0]][ruutu[1]] = '#'
            for siirto in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                uusi_ruutu = (ruutu[0]+siirto[0], ruutu[1]+siirto[1])
                if uusi_ruutu[0] == koko-1 or uusi_ruutu[1] == koko-1:
                    continue
                v_ruudut = ymparoivat_ruudut(
                    labyrintti, uusi_ruutu[0], uusi_ruutu[1])
                if v_ruudut.count(".") > 1:
                    continue
                if labyrintti[uusi_ruutu[0]][uusi_ruutu[1]] == "@":
                    continue
                if labyrintti[uusi_ruutu[0]][uusi_ruutu[1]] == ".":
                    jono.append(uusi_ruutu)
    return labyrintti


# if __name__ == "__main__":
#     labyrintti=labyrintti_tahan
#     koko=20
#     print(etsi_umpikujat(labyrintti,koko))
