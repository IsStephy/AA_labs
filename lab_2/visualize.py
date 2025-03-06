import random
import time
import matplotlib.pyplot as plt
import numpy as np
import tracemalloc

i = 0

def quick_sort(arr):
    steps = [0]
    def quick_sort_helper(arr, left, right, ax):
        if left < right:
            pivot_index = partition(arr, left, right)
            steps[0] += 1
            visualize_array(arr, ax, 'Quick Sort', steps[0])
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
    steps = [0]
    def merge_sort_helper(arr, l, r, ax):
        if l < r:
            m = (l + r) // 2
            merge_sort_helper(arr, l, m, ax)
            merge_sort_helper(arr, m + 1, r, ax)
            merge(arr, l, m, r)
            steps[0] += 1
            visualize_array(arr, ax, 'Merge Sort', steps[0])
    
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
    steps = [0]
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
            steps[0] += 1
            visualize_array(arr, ax, 'Heap Sort', steps[0])
    
    fig, ax = plt.subplots()
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, ax)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, ax)
    visualize_array(arr, ax, 'Heap Sort', steps[0])
    plt.show()

def bogo_sort(arr):
    sorted_part = []
    steps = 0
    fig, ax = plt.subplots()
    
    while arr:
        random.shuffle(arr)
        steps += 1
        
        if arr == sorted(arr):
            sorted_part += arr
            arr = []
        elif min(arr) == arr[0]:
            sorted_part.append(arr.pop(0))
        
        print_arr = sorted_part + arr
        visualize_array(print_arr, ax,'Bogo Sort', steps)
    plt.show()

    return sorted_part

def visualize_array(arr, ax, name, steps=0):
    ax.clear()
    ax.bar(range(len(arr)), arr, color='blue')
    ax.set_ylim(0, max(arr) + 1)
    ax.set_title(f"{name} - Steps: {steps}")
    plt.pause(0.04)

data_sizes = [31]
time_results = {}
memory_results = {}

sorting_algorithms = {
    'Quick Sort': quick_sort,
    'Merge Sort': merge_sort,
    'Heap Sort': heap_sort,
    "Bogo Sort": bogo_sort
}

for name, func in sorting_algorithms.items():
    times = []
    memories = []
    for size in data_sizes:
        arr = [random.randint(0, 999) for _ in range(size)]  
        arr_copy = arr[:]
        func(arr_copy)
