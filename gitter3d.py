#wie gitter1d.py, nur dass hier ein 2D Gitter verwendet wird (2 körper mit je 2 x 4 Atomen)

import random as rnd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import Counter

# random seed setzen (nicht reproduzierbar)
rnd.seed()

show_histo = True
show_koerper = False
show_pdf = True


anzahl_koerper = 2
# Anzahl Atome in x und y Richtung (pro Körper)
x = 4
y = 4
z = 4
anzahl_simulationen = 10000

energie = 100

#resultat liste initalisieren
resultat = []

#wähle eine zufällige Position aus und erhöhe den Wert um 1
for s in range(anzahl_simulationen):
    #gitter definieren: 2D array mit 2 x 8 Atomen (int)
    gitter = np.zeros((y , x * anzahl_koerper, z), dtype=int)
    for i in range(energie):
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
    


import numpy as np
import matplotlib.pyplot as plt

# Assuming the rest of your code is already defined

if show_koerper:
    # Körper 1 - anzahl_koerper als matrix definieren
    gitterliste = []
    for i in range(anzahl_koerper):
        gitter2 = gitter[:, i*(x):(i+1)*(x), :]
        gitterliste.append(gitter2)
    visualisiere_gitter(gitterliste)

# durchschnitt berechnen
durchschnitt = sum(resultat) / len(resultat)
print("Durchschnitt:", durchschnitt)

if show_histo:
    # Create a figure with two subplots: one for the histogram and one for the Durchschnitt
    if show_pdf:
        fig, (ax_hist, ax_text, ax_prob) = plt.subplots(3, 1, gridspec_kw={'height_ratios': [4, 1, 4]}, figsize=(8, 6))
    
    else:
        fig, (ax_hist, ax_text) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [4, 1]}, figsize=(8, 6))
    
    # Histogramm erstellen
    ax_hist.hist(resultat, bins=energie)
    ax_hist.set_title(f"Histogramm von {anzahl_simulationen} Simulationen")
    ax_hist.set_xlabel("Anzahl Energie 1. Körper")
    ax_hist.set_ylabel("Häufigkeit/Anzahl Simulationen")
    
    
    ax_hist.xaxis.set_major_locator(MaxNLocator(integer=True, prune='both', nbins=10))
    ax_hist.yaxis.set_major_locator(MaxNLocator(integer=True, prune='both', nbins=10))
    
    
    ax_text.axis('off')
    
    
    ax_text.text(0.5, 0.5, f"Durchschnitt: {durchschnitt:.2f}", ha='center', va='center')
    
    plt.tight_layout()
    
    if show_pdf:
        
        # wahrscheinlichkeit berechnen
        zaehler = Counter(resultat)
        category_probabilities = {category: count / anzahl_simulationen for category, count in zaehler.items()}

        categories = list(category_probabilities.keys())
        probabilities = list(category_probabilities.values())


        plt.bar(categories, probabilities, color='g')
        ax_prob.xaxis.set_major_locator(MaxNLocator(integer=True, prune='both', nbins=10))
        ax_prob.yaxis.set_major_locator(MaxNLocator(integer=True, prune='both', nbins=10))
        ax_prob.set_xlabel("Anzahl Energie 1. Körper")
        ax_prob.set_ylabel("Wahrscheinlichkeit")
        ax_prob.set_title("Wahrscheinlichkeit")
    
    plt.tight_layout()
    plt.show()
