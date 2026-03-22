array1 = [0, 1, 2, 3, 2, 1, 0] 
array2 = ["a", "b", "b", "a"] 
array3 = ["a", "b", "c", "b", "a"] 
array4 = ["a", "b", "c", "f", "b", "a"]

print("*"* 50)

# Function recursive to check if an array is a palindrome
def is_palindrome(array):
    # Loop to check if the first and last elements are the same
    for i in range(len(array)):
        first = array[i]
        last = array[len(array) - 1 - i]
        
        # If the first and last elements are not the same, return False
        if first != last:
            return False

    # If the loop finishes without finding any differences, return True
    return True


# Check arrays and print the results
print(f"is_palindrome(array1): {is_palindrome(array1)}")
print(f"is_palindrome(array2): {is_palindrome(array2)}")
print(f"is_palindrome(array3): {is_palindrome(array3)}")
print(f"is_palindrome(array4): {is_palindrome(array4)}")

print("*"* 50)