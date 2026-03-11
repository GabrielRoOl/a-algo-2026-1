import random 
import time

# My implementation of the insertion sot.
def time_to_sort_using_my_insertion_sort(lst):
    
    start = time.perf_counter()
    
    # Insertion sort algorithm.
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    
    end = time.perf_counter()
    return end - start

# Native Python sorted function. 
def native_python_sorted(lst):
    return sorted(lst)

# Time to sort using the native Python sorted function.
def time_to_sort_using_sorted(lst):
    start = time.perf_counter()
    native_python_sorted(lst)
    end = time.perf_counter()
    return end - start


# Generate random number for the tests.
def generate_random_integers(lst, n):
    for i in range(n):
        lst.append(random.randint(0, n))
        

# List of sizes to test the sorting algorithms.
size = [1000, 5000, 10000, 20000, 50000]

# Test the sorting algorithms and print the results.
for n in size:
    lst = []
    generate_random_integers(lst, n)
    
    # Time to sort using my insertion sort and the native Python sorted function.
    time_insertion_sort = time_to_sort_using_my_insertion_sort(lst.copy())
    time_sorted = time_to_sort_using_sorted(lst.copy())
    
    print(f"Time to sort {n} integers using my insertion sort: {time_insertion_sort:.6f} seconds")
    print(f"Time to sort {n} integers using native Python sorted: {time_sorted:.6f} seconds")
    print("-" * 50)
