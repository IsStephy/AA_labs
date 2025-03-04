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

def quick_sort(arr):
    def quick_sort_helper(arr, left, right, ax):
        if left < right:
            pivot_index = partition(arr, left, right)
            visualize_array(arr, ax)
            quick_sort_helper(arr, left, pivot_index - 1, ax)
            quick_sort_helper(arr, pivot_index + 1, right, ax)
    
    def partition(arr, left, right):
        pivot = arr[right]
        i = left - 1
        for j in range(left, right):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        return i + 1
    
    fig, ax = plt.subplots()
    quick_sort_helper(arr, 0, len(arr) - 1, ax)
    plt.show()

def merge_sort(arr):
    def merge_sort_helper(arr, l, r, ax):
        if l < r:
            m = (l + r) // 2
            merge_sort_helper(arr, l, m, ax)
            merge_sort_helper(arr, m + 1, r, ax)
            merge(arr, l, m, r)
            visualize_array(arr, ax)
    
    def merge(arr, l, m, r):
        left = arr[l:m+1]
        right = arr[m+1:r+1]
        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    
    fig, ax = plt.subplots()
    merge_sort_helper(arr, 0, len(arr) - 1, ax)
    plt.show()

def heap_sort(arr):
    def heapify(arr, n, i, ax):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest, ax)
            visualize_array(arr, ax)
    
    fig, ax = plt.subplots()
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, ax)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, ax)
    plt.show()

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
        
        print_arr = sorted_part + arr
        visualize_array(print_arr, ax)
        time.sleep(0.05)
    
    return sorted_part

def visualize_array(arr, ax):
    ax.clear()
    ax.bar(range(len(arr)), arr, color='blue')
    ax.set_ylim(0, max(arr) + 1)
    plt.pause(0.04)

data_sizes = [40]
time_results = {}
memory_results = {}

sorting_algorithms = {
    'Quick Sort': quick_sort,
    #'Merge Sort': merge_sort,
    #'Heap Sort': heap_sort,
    "Bogo Sort": bogo_sort
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
