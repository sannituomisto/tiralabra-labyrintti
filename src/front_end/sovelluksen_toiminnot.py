def nayta_toiminnot():
    komennot = [("1", "Poistu sovelluksesta"), 
                ("2", "Tutki labyrintteja"),
                ("3", "Ratkaise dead end filling algoritmilla"),
                ("4", "Ratkaise Tremauxin algoritmilla"),
                ("5", "Vertaile algoritmeja"),
                ]
    for komento, selitys in komennot:
        print(f"{komento:5} {selitys}")