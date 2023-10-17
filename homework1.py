import time
import random
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

# Il primo blocco while confronta gli elementi delle due metà (sinistra e destra) e li unisce in ordine nella lista originale. Il ciclo continua finché entrambe le sottoliste hanno elementi da confrontare.

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

# Il secondo e il terzo blocco while sono usati per aggiungere eventuali elementi rimanenti dalle due sottoliste (sinistra e destra) alla lista principale se una delle due sottoliste è più lunga dell'altra. Questo assicura che tutti gli elementi siano inseriti correttamente nell'array finale.

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

sizes = [500, 1000, 2000, 3000, 40000]
times = []

for size in sizes:
    arr = [random.randint(0, 1000) for _ in range(size)]

    start_time = time.time()
    merge_sort(arr)
    end_time = time.time()

    times.append(end_time - start_time)


plt.plot(sizes, times, marker='o')
plt.title('Merge Sort Performance')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.show()
