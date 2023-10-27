import time
import random
import matplotlib.pyplot as plt

# Merge Sort in-place

def merge_sort_inplace(arr, l, r):

    # Divide l'array in due parti e chiama ricorsivamente per entrambe le metà.
    
    if l < r:
        m = l + (r - l) // 2
        merge_sort_inplace(arr, l, m)
        merge_sort_inplace(arr, m + 1, r)
        merge(arr, l, m, r)

def merge(arr, l, m, r):
    
    # Unisce due sottoliste ordinate in-place in una lista.
    
    n1 = m - l + 1
    n2 = r - m

    left_half = [0] * n1
    right_half = [0] * n2

    # Copia i valori nelle sottoliste
    
    for i in range(0, n1):
        left_half[i] = arr[l + i]

    for j in range(0, n2):
        right_half[j] = arr[m + 1 + j]

    i = j = 0
    k = l

    # Unisce le sottoliste in ordine nella lista originale
    
    while i < n1 and j < n2:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Aggiunge eventuali elementi rimanenti dalle sottoliste alla lista principale se una delle due è più lunga dell'altra
    
    while i < n1:
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_half[j]
        j += 1
        k += 1

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

        # Aggiunge eventuali elementi rimanenti dalle sottoliste alla lista principale se una delle due è più lunga dell'altra

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

sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 12000, 14000, 16000, 18000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 60000, 70000, 80000, 90000, 100000, 120000, 140000, 160000, 180000, 200000, 250000, 300000, 350000, 400000, 450000, 500000, 600000, 700000, 800000, 900000, 1000000]
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
