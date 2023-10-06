'''Scrivere il codice Python per le due funzioni presenti alla fine della lezione 1 (find_max e test).'''

import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

def find_max(list):
    max_value = list[0]
    for item in list:
        if max_value < list[item]:
            max_value = list[item]
    return max_value

def test(n):
    costo_unif_values = []  # Lista per registrare i valori di costo_unif
    costo_log_values = []   # Lista per registrare i valori di costo_log
    z = 2
    for i in range(n-1):
        z = z*z
        costo_unif_values.append(3 + costo_unif_values[-1] if costo_unif_values else 3)
        costo_log_values.append(2 + math.log(z) + costo_log_values[-1] if costo_log_values else 2 + math.log(z))
    
    # Stampa l'ultimo valore di z e il massimo valore tra i due costi
    print("Ultimo valore di z:", z)
    print("costo_unif e costo_log:", sum(costo_unif_values), "\n", sum(costo_log_values))
    
    
    # Crea il grafico
    plt.plot(range(1, n), costo_unif_values, label='costo_unif')
    plt.plot(range(1, n), costo_log_values, label='costo_log')
    plt.plot( 2**np.arange(1, n + 1), c="black", linestyle="--", alpha=0.5)
    plt.plot(np.arange(1, n + 1), c="black", linestyle="--", alpha=0.5)


    # Aggiungi etichette agli assi e una legenda
    plt.xlabel('Iterazioni')
    plt.ylabel('Valore del costo')
    plt.legend()
    
    # Mostra il grafico
    plt.show()

n = int(input("Dammi n per la funzione test: "))
test(n)
