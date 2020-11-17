# Lösung der Aufgabe "Testen von Fingerabdrücken"

# Vorgegebene Funktionen: suche(), laenge(), loesche()

def auswertung(abdruck, schwelle, finger):
    abdrücke = suche(abdruck)

    # Löschen aller falschen Einträge

    i = laenge(abdrücke)
    while i > 0:
        if abdrücke[i].score < schwelle or (finger != 0 and abdrücke[i].idFinger):
            loesche(abdrücke, i)
        else:
            i = i - 1

    # Sortieren nach score (Bubble sort; absteigend)
    l = laenge(abdrücke)

    for i in range(l - 1):
        for j in range(0, l - i - 1):
            if abdrücke[j] < abdrücke[j + 1]:
                abdrücke[j], abdrücke[j + 1] = abdrücke[j + 1], abdrücke[j]

    return abdrücke
