import time
import random

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def compare_binary_search():
    sizes = [10, 100, 1000, 10000]
    print(f"{'Array Size':>10} | {'Recursive Time (ms)':>20} | {'Iterative Time (ms)':>20}")
    print("-" * 60)

    for size in sizes:
        arr = sorted(random.sample(range(size * 2), size))
        target = random.choice(arr)

        start = time.perf_counter()
        binary_search_recursive(arr, target, 0, len(arr) - 1)
        recursive_time = (time.perf_counter() - start) * 1000  

        start = time.perf_counter()
        binary_search_iterative(arr, target)
        iterative_time = (time.perf_counter() - start) * 1000  

        print(f"{size:>10} | {recursive_time:>20.6f} | {iterative_time:>20.6f}")

if __name__ == "__main__":
    compare_binary_search()
