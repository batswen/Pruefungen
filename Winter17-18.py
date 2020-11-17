# Lösung der Aufgabe "Freie Kinositze auf dem Kreuzfahrtschiff"

# 7 Sitzreihen, 30 Plätze pro Reihe
# Sitzreihe 1: Sitznummern 101 bis 130
# Sitzreihe 2: Sitznummern 201 bis 230

def freie_sitze(anzahl_sitze):
    for reihe in range(7):
        anzahl = 0
        for sitz in range(30):
            if kino[reihe][sitz]:
                anzahl = anzahl + 1
                if anzahl == anzahl_sitze:
                    return (reihe + 1) * 100 + anzahl + 1
            else:
                anzahl = 0
    return 0
