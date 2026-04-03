# f(n) = 2f(n-1)+n²

def function_f(x):
    if x == 1:
        return 2
    return 2 * function_f(x -1) + x**2

n = int(input("Digite o valor de n: "))
print(function_f(n))