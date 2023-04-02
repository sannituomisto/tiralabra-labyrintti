from front_end.nayta_labyrintti import labyrintin_nro
from front_end.nayta_labyrintti import labyrintin_koko
from front_end.nayta_labyrintti import labyrintin_haku
from front_end.nayta_labyrintti import labyrintin_visualisointi
from dead_end_filling import etsi_umpikujat

def nayta_dead_end_filling():
    laby_nro=labyrintin_nro()
    laby_koko=labyrintin_koko(laby_nro)
    labyrintti=labyrintin_haku(laby_nro)
    labyrintti2=labyrintin_haku(laby_nro)
    ratkaistu_labyrintti, umpikujat=etsi_umpikujat(labyrintti, laby_koko)
    labyrintti_umpikujilla=umpikujat_labyrinttiin(labyrintti2, umpikujat)
    print('\r')
    print('Labyrintin umpikujat:')
    labyrintin_visualisointi(labyrintti_umpikujilla, laby_koko)
    print('\r')
    print('Ratkaisu:')
    labyrintin_visualisointi(ratkaistu_labyrintti, laby_koko)


def umpikujat_labyrinttiin(labyrintti2, umpikujat):
    for umpikuja in umpikujat:
        labyrintti2[umpikuja[0]][umpikuja[1]] = 'u'
    return labyrintti2