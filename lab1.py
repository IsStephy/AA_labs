import time
import matplotlib.pyplot as plt
import sys
import tracemalloc
sys.setrecursionlimit(300000)

# Backtracking algorithm
def fibonacci_backtracking(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci_backtracking(n-1) + fibonacci_backtracking(n-2)
        return memo[n]


# Iterative algorithm
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

# Dynamic Programming algorithm
def fibonacci_dynamic(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Matrix Power algorithm
def fibonacci_matrix_power(n):
    def matrix_mult(A, B):
        return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

    def matrix_power(F, n):
        if n == 1:
            return F
        if n % 2 == 0:
            half_power = matrix_power(F, n // 2)
            return matrix_mult(half_power, half_power)
        else:
            return matrix_mult(F, matrix_power(F, n - 1))

    if n <= 1:
        return n
    F = [[1, 1], [1, 0]]
    result = matrix_power(F, n - 1)
    return result[0][0]


def measure_time_and_memory(func, n):
    tracemalloc.start()
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    execution_time = end_time - start_time
    return execution_time, peak, result
limit = 16000
input_sizes = list(range(0, limit, 2000))
backtracking_times = []
backtracking_memories = []
iterative_times = []
iterative_memories = []
dynamic_times = []
dynamic_memories = []
matrix_times = []
matrix_memories = []
print(f"{'Input Size':>10}  {'Iterative Time (s)':>25} {'Iterative Memory (KB)':>25}")
print("-" * 115)
count = 0;
for n in input_sizes:
    if n <= 16000: 
        time_taken, memory_used, _ = measure_time_and_memory(fibonacci_backtracking, n)
        backtracking_times.append(time_taken)
        backtracking_memories.append(memory_used / 1024)
    else:
        backtracking_times.append(None)
        backtracking_memories.append(None)

    time_taken, memory_used, _ = measure_time_and_memory(fibonacci_iterative, n)
    iterative_times.append(time_taken)
    iterative_memories.append(memory_used / 1024)


    time_taken, memory_used, _ = measure_time_and_memory(fibonacci_dynamic, n)
    dynamic_times.append(time_taken)
    dynamic_memories.append(memory_used / 1024)

    time_taken, memory_used, _ = measure_time_and_memory(fibonacci_matrix_power, n)
    matrix_times.append(time_taken)
    matrix_memories.append(memory_used / 1024)
    
    print(f"{n:>10} {iterative_times[count]:>25.6f} {iterative_memories[count] / 1024:>30.6f}")
    count+=1




# Plotting the results
plt.figure(figsize=(14, 10))

# Time complexity comparison
plt.subplot(2, 1, 1)
plt.plot(input_sizes, backtracking_times, label="Backtracking")
plt.plot(input_sizes, iterative_times, label="Iterative")
plt.plot(input_sizes, dynamic_times, label="Dynamic Programming")
plt.plot(input_sizes, matrix_times, label="Matrix Power")


plt.xlabel("Fibonacci Term")
plt.ylabel("Time (seconds)")
plt.title("Time Complexity")
plt.legend()
plt.grid()

# Memory complexity comparison
plt.subplot(2, 1, 2)
plt.plot(input_sizes, backtracking_memories, label="Backtracking")
plt.plot(input_sizes, iterative_memories, label="Iterative")
plt.plot(input_sizes, dynamic_memories, label="Dynamic Programming")
plt.plot(input_sizes, matrix_memories, label="Matrix Power")
plt.xlabel("Fibonacci Term")
plt.ylabel("Memory (KB)")
plt.title("Memory Complexity")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
