import time
import random
import matplotlib.pyplot as plt

# Merge Sort in-place

def merge_sort_inplace(arr, l, r):
    # Implementazione dell'algoritmo di merge sort in-place
    if l < r:
        m = l + (r - l) // 2  # Trova il punto medio
        merge_sort_inplace(arr, l, m)  # Ordina la prima metà
        merge_sort_inplace(arr, m + 1, r)  # Ordina la seconda metà
        merge_inplace(arr, l, m, r)  # Unisce le due metà ordinate

def merge_inplace(arr, l, m, r):
    # Unisce due sottoliste ordinate in-place in una lista
    n1 = m - l + 1  # Lunghezza della prima metà
    n2 = r - m  # Lunghezza della seconda metà

    # Inizializzazione degli indici per le due metà
    p1, p2 = l, m + 1

    # Unisce le sottoliste direttamente nell'array originale senza l'uso di nuove liste
    while p1 <= m and p2 <= r:
        if arr[p1] <= arr[p2]:
            p1 += 1
        else:
            # Copia l'elemento corrente della seconda metà nell'array originale
            arr[m] = arr[p2]
            p2 += 1

    # Sposta gli elementi rimanenti della prima metà a destra
    for i in range(m + 1, r + 1):
        arr[i] = arr[i - 1]

    # Aggiorna il limite destro della prima metà
    m += n2

# Merge Sort out-of-place

def merge_sort_outplace(arr):

    # Divide l'array in due parti e chiama ricorsivamente per entrambe le metà.

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort_outplace(left_half)
        merge_sort_outplace(right_half)

        i = j = k = 0

        # Confronta gli elementi delle due metà e li unisce in ordine nella lista originale

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Aggiunge eventuali elementi rimanenti dalle sottoliste alla lista principale 
        # se una delle due è più lunga dell'altra

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Confronto delle prestazioni

sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 
         9000, 10000, 12000, 14000, 16000, 18000, 20000, 
         25000, 30000, 35000, 40000, 45000, 50000, 60000, 
         70000, 80000, 90000, 100000, 120000, 140000, 160000, 
         180000, 200000, 250000, 300000, 350000, 400000, 450000, 
         500000, 600000, 700000, 800000, 900000, 1000000]
times_inplace = []
times_outplace = []

for size in sizes:
    arr = [random.randint(0, 1000) for _ in range(size)]
    arr_copy = arr.copy()

    start_time = time.time()
    merge_sort_inplace(arr, 0, size - 1)
    end_time = time.time()
    times_inplace.append(end_time - start_time)

    start_time = time.time()
    merge_sort_outplace(arr_copy)
    end_time = time.time()
    times_outplace.append(end_time - start_time)

# Plotting dei grafici

plt.plot(sizes, times_inplace, marker='o', label='Merge Sort in-place')
plt.plot(sizes, times_outplace, marker='o', label='Merge Sort out-of-place')
plt.title('Confronto delle prestazioni di Merge Sort')
plt.xlabel('Dimensione dell\'input')
plt.ylabel('Tempo (secondi)')
plt.legend()
plt.show()
