import random as rnd

#resultat liste initalisieren
resultat = []




# Positionen 0-7: 1. Körper
# Positionen 8-15: 2. Körper

for s in range(1000):
    # Gitter definieren: Liste mit 16 Atomen
    gitter = [0 for i in range(16)]
    print(gitter)
    #10 mal zufällig ein Atom auswählen und den Wert um 1 erhöhen
    for i in range(10):
        atom = rnd.randint(0, 15)
        gitter[atom] += 1

    # atome im 1. Körper zählen
    anzahl1 = 0
    for i in range(8):
        anzahl1 += gitter[i]
    print(gitter)
    print("Anzahl Atome 1. Körper:", anzahl1)

    #anzahl einer liste zufügen 
    resultat.append(anzahl1)
    
    
# resultate ausgeben
print(resultat)

#durchschnitt berechnen
durchschnitt = sum(resultat) / len(resultat)
print("Durchschnitt:", durchschnitt)

#histogramm erstellen
import matplotlib.pyplot as plt
plt.hist(resultat, bins=range(0, 11))
#normalverteilung einzeichnen

plt.title("Histogramm")
plt.xlabel("Anzahl Atome 1. Körper")
plt.ylabel("Häufigkeit")

plt.show()



