#wie gitter1d.py, nur dass hier ein 2D Gitter verwendet wird (2 körper mit je 2 x 4 Atomen)

import random as rnd
import numpy as np
import matplotlib.pyplot as plt

# random seed setzen (nicht reproduzierbar)
rnd.seed()



anzahl_koerper = 3
# Anzahl Atome in x und y Richtung (pro Körper)
x = 5
y = 4
z = 3
anzahl_simulationen = 10000

entropie = 100

#resultat liste initalisieren
resultat = []

#wähle eine zufällige Position aus und erhöhe den Wert um 1
for s in range(anzahl_simulationen):
    #gitter definieren: 2D array mit 2 x 8 Atomen (int)
    gitter = np.zeros((y , x * anzahl_koerper, z), dtype=int)
    for i in range(entropie):
        atom = (rnd.randint(0, y-1), rnd.randint(0, anzahl_koerper * x-1), rnd.randint(0, z-1))
        gitter[atom] += 1

    #print(gitter)

    # atome im 1. Körper zählen (Hälfte x, alle y)
    anzahl1 = 0
    for i in range(y):
        for j in range(x):
            for k in range(z):
                anzahl1 += gitter[i, j, k]
    #anzahl einer liste zufügen 
    resultat.append(int(anzahl1))

import numpy as np
import matplotlib.pyplot as plt

# definiere Funktion, um gitter in 3D zu visualisieren
def visualisiere_gitter(gitterliste):
    fig = plt.figure(figsize=(15, 5))
    
    for idx, gitter in enumerate(gitterliste):
        y, x, z = gitter.shape  # Get the dimensions of the matrix
        ax = fig.add_subplot(1, anzahl_koerper, idx + 1, projection='3d')
        
        # Plot all points in the grid
        for i in range(y):
            for j in range(x):
                for k in range(z):
                    # Set a small marker size for points with value 0
                    if gitter[i, j, k] == 0:
                        marker_size = 10
                        ax.scatter(j, i, k, c='g', s=marker_size)
                    else:
                        marker_size = gitter[i, j, k] * 100
                        ax.scatter(j, i, k, c='b', s=marker_size)
        
        # Plot grid lines within the body
        for i in range(y):
            for j in range(x):
                ax.plot([j, j], [i, i], [0, z-1], color='gray', linestyle='--', linewidth=0.5)
        for i in range(y):
            for k in range(z):
                ax.plot([0, x-1], [i, i], [k, k], color='gray', linestyle='--', linewidth=0.5)
        for j in range(x):
            for k in range(z):
                ax.plot([j, j], [0, y-1], [k, k], color='gray', linestyle='--', linewidth=0.5)
        
        ax.set_xlabel('X Position')
        ax.set_ylabel('Y Position')
        ax.set_zlabel('Z Position')
        ax.set_title(f'Entropie Visualisierung Körper {idx + 1}')

        # Set grid lines at every integer position
        ax.set_xticks(np.arange(0, x, 1))
        ax.set_yticks(np.arange(0, y, 1))
        ax.set_zticks(np.arange(0, z, 1))
        ax.grid(False)
    
    plt.tight_layout()
    plt.show()
    



# Körper 1 - anzahl_koerper als matrix definieren
gitterliste = []
for i in range(anzahl_koerper):
    gitter2 = gitter[:, i*(x):(i+1)*(x), :]
    gitterliste.append(gitter2)
visualisiere_gitter(gitterliste)

# durchschnitt berechnen
durchschnitt = sum(resultat) / len(resultat)
print("Durchschnitt:", durchschnitt)


#histogramm erstellen

plt.hist(resultat, bins=range(0, entropie + 1))
plt.title("Histogramm")
plt.xlabel("Anzahl Atome 1. Körper")
plt.ylabel("Häufigkeit")
plt.show()







