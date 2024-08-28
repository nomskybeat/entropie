#wie gitter1d.py, nur dass hier ein 2D Gitter verwendet wird (2 körper mit je 2 x 4 Atomen)

import random as rnd
import numpy as np

# random seed setzen (nicht reproduzierbar)
rnd.seed()



anzahl_koerper = 3
# Anzahl Atome in x und y Richtung (pro Körper)
x = 5
y = 4
anzahl_simulationen = 1000

entropie = 20

#resultat liste initalisieren
resultat = []

#wähle eine zufällige Position aus und erhöhe den Wert um 1
for s in range(anzahl_simulationen):
    #gitter definieren: 2D array mit 2 x 8 Atomen (int)
    gitter = np.zeros((y , x * anzahl_koerper), dtype=int)
    for i in range(entropie):
        atom = (rnd.randint(0, y-1), rnd.randint(0, anzahl_koerper * x-1))
        gitter[atom] += 1

    #print(gitter)

    # atome im 1. Körper zählen (Hälfte x, alle y)
    anzahl1 = 0
    for i in range(y):
        for j in range(x):
            anzahl1 += gitter[i, j]
    #anzahl einer liste zufügen 
    resultat.append(int(anzahl1))

# resultate ausgeben
#print(resultat)

# letztes Gitter ausgeben
print(gitter)

# durchschnitt berechnen
durchschnitt = sum(resultat) / len(resultat)
print("Durchschnitt:", durchschnitt)


#histogramm erstellen
import matplotlib.pyplot as plt
plt.hist(resultat, bins=range(0, entropie + 1))
plt.title("Histogramm")
plt.xlabel("Anzahl Atome 1. Körper")
plt.ylabel("Häufigkeit")
plt.show()



