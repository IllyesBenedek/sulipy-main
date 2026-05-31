# Enclosing (nonlocal) scope

def kulso_fgv():
    szam = 17

    def belso_fgv():
        print(f"A belső fügvényből {szam}")
    belso_fgv()


kulso_fgv()
