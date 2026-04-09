import math
import sympy as sp

# Solves recurrences of the type T(n) = aT(n/b) + f(n) using the Master Theorem.
def solve_recurrence(a, b, f_n_string):
    
    n = sp.Symbol('n', positive=True, real=True)
    f_n = sp.sympify(f_n_string)
    
    # Calculation of the critical value: n^(log_b(a))    
    log_b_a = math.log(a, b)
    n_critical = n**log_b_a
    
    print(f"Equation: T(n) = {a}T(n/{b}) + {f_n_string}")
    print(f"Critical term n^log_{b}({a}) = n^{log_b_a:.2f}")
    
    # Simplified comparison for the Master Theorem
    if sp.simplify(f_n / n_critical).is_constant():
        result = f"O(n^{log_b_a:.2f} * log n)"
    elif sp.limit(f_n / n_critical, n, sp.oo) == 0:
        result = f"O(n^{log_b_a:.2f})"
    else:
        result = f"O({f_n_string})"
        
    print(f"Estimated Complexity: {result}\n" + "-"*30)

# Executes the recurrences from the image
questions = [
    (2, 4, "sqrt(n)"),
    (2, 4, "n"),
    (16, 4, "n**2")
]

print("=======  RECURRENCE RESOLUTION =======\n")
for a, b, f in questions:
    solve_recurrence(a, b, f)

# Practical Merge Sort example
def merge_sort_count(arr):
    """A version that only demonstrates recursive division."""
    if len(arr) <= 1:
        return 0
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # The merge cost is proportional to n
    merge_cost = len(arr)
    return merge_cost + merge_sort_count(left) + merge_sort_count(right)

n_test = 64
total_operations = merge_sort_count(list(range(n_test)))
print(f"Merge Sort for n={n_test}:")
print(f"Estimated operations (n log2 n): {n_test * math.log2(n_test)}")
print(f"Calculated operations in recursion: {total_operations}")