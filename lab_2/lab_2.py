import random
import time
import matplotlib.pyplot as plt
import numpy as np
import tracemalloc

def measure_time_memory(sort_func, arr):
    arr_copy = arr[:]
    tracemalloc.start()
    start_time = time.time()
    sort_func(arr_copy)
    end_time = time.time()
    memory_used = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return end_time - start_time, memory_used

#==============================================================
#               Quick Sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

#==============================================================
#                   Merge Sort

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

#==============================================================
#                   Heap Sort

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

#==============================================================
#                   Bogo Sort enproved

def bogo(arr):
    while arr != sorted(arr):
        random.shuffle(arr)
    print("sorted")
    return arr

def bogo_sort(arr):
    sorted_part = []
    fig, ax = plt.subplots()
    
    while arr:
        random.shuffle(arr)
        
        if arr == sorted(arr):
            sorted_part += arr
            arr = []
        elif min(arr) == arr[0]:
            sorted_part.append(arr.pop(0))
        
        #print_arr = sorted_part + arr
        #visualize_array(print_arr, ax)
        #time.sleep(0.1)
    print("sorted")
    
    return sorted_part

def visualize_array(arr, ax):
    ax.clear()
    ax.bar(range(len(arr)), arr, color='blue')
    ax.set_ylim(0, max(arr) + 1)
    plt.pause(0.04)

def visualize_sorting(arr, sort_func, title):
    fig, ax = plt.subplots()
    arr_copy = arr[:]
    for _ in range(100):
        random.shuffle(arr_copy)
        ax.clear()
        ax.bar(range(len(arr_copy)), arr_copy, color='blue')
        ax.set_title(title)
        ax.set_ylim(0, max(arr) + 1)
        plt.pause(0.05)
        if arr_copy == sorted(arr):
            break
    plt.show()

data_sizes = []
for _ in range(0,12):
    if _%2 == 0:
        data_sizes.append(_)
time_results = {}
memory_results = {}

sorting_algorithms = {
    #'Quick Sort': quick_sort
    #'Merge Sort': merge_sort,
    #'Heap Sort': heap_sort
    #'Bogo Sort modified':bogo_sort
    'Bogo Sort ': bogo
}

for name, func in sorting_algorithms.items():
    times = []
    memories = []
    for size in data_sizes:
        arr = [random.randint(0, 999) for _ in range(size)]  
        t, m = measure_time_memory(func, arr)
        times.append(t)
        memories.append(m)
    time_results[name] = times
    memory_results[name] = memories

plt.figure(figsize=(12, 6))
for name in sorting_algorithms.keys():
    plt.plot(data_sizes, time_results[name], label=f'{name} Time')
plt.xlabel('Input Size')
plt.ylabel('Time (s)')
plt.title('Sorting Algorithm Time Complexity')
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
for name in sorting_algorithms.keys():
    plt.plot(data_sizes, memory_results[name], label=f'{name} Memory')
plt.xlabel('Input Size')
plt.ylabel('Memory (bytes)')
plt.title('Sorting Algorithm Memory Complexity')
plt.legend()
plt.show()
