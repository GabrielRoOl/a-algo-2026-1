array1 = [0, 1, 2, 3, 2, 1, 0] 
array2 = ["a", "b", "b", "a"] 
array3 = ["a", "b", "c", "b", "a"] 
array4 = ["a", "b", "c", "f", "b", "a"]

print("*"* 50)

def is_palindrome(array):
    for i in range(len(array)):
        first = array[i]
        last = array[len(array) - 1 - i]
        
        if first != last:
            return False

    return True

print(f"is_palindrome(array1): {is_palindrome(array1)}")
print(f"is_palindrome(array2): {is_palindrome(array2)}")
print(f"is_palindrome(array3): {is_palindrome(array3)}")
print(f"is_palindrome(array4): {is_palindrome(array4)}")

print("*"* 50)