import sys as s
import random as r
import time as t

# Increases the recursion limit to 2000.
s.setrecursionlimit(2000)

# Function recursive to calculete the n factorial number
def factorial(n):
    # If n is 0, the factorial is 1, otherwise, the factorial is n times the factorial of n - 1
    if n == 0:
        return 1
    # Else the factorial multiply n by the factorial of n - 1
    else:
        return n * factorial(n - 1)

# Generate random number for the tests.
def generate_random_integers(lst, n):
    for i in range(n):
        lst.append(r.randint(0, n))
        

# Codigo para ordenar a lista com complexidade O(n) 
def counting_sort(arr):
    # Find the maximum element in the array
    max_element = max(arr)
    
    # Create a count array to store the count of each unique object
    count = [0] * (max_element + 1)
    
    # Count each element in the input array
    for num in arr:
        count[num] += 1
    
    # Build the output array
    output = []
    for i in range(len(count)):
        output.extend([i] * count[i])
    
    return output

# List of sizes to test the factorial function.
size = [10, 100, 500, 1000]


print("Calculating factorials for the following numbers: ", size)
for n in size:
    start = t.perf_counter()
    factorial(n)
    end = t.perf_counter()
    print(f"Time to calculate the factorial of {n}: {end - start:.6f} seconds")
    

print("\nGenerating random integers and sorting them using counting sort...")
for n in size:
    lst = []
    generate_random_integers(lst, n)
    
    start = t.perf_counter()
    sorted_lst = counting_sort(lst)
    end = t.perf_counter()
    
    print(f"Time to sort {n} integers using counting sort: {end - start:.6f} seconds")

# ---------------------------------------------------------
# This code tests the time of two things: factorial and counting sort.
# First it calculete the factorial of some numbers (10, 100, 500, 1000)
# using a recursive function and measure how long it takes.
#
# After that, the program generate random numbers in a list and
# sort them using counting sort. It also measure the time for that.
#
# The ideia is just to see how the time change when the size of
# the input gets bigger.
# ---------------------------------------------------------
