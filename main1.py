# Iterative approach: Sum of elements in an array
def arraysum(a):
    sum = 0
    for i in a:
        sum = sum + i
    return sum

# Recursive approach: Sum of first n natural numbers
def summ(n):
    # Base case: when n is 0 or less, return 0
    if n <= 0:
        return 0
    # Recursive case: add n to the result of summ(n - 1)
    return n + summ(n - 1)

# Example usage of both functions

# 1. Using arraysum (iterative approach)
a = [12, 3, 4, 15]  # Example array
print("Sum of array elements (iterative):", arraysum(a))  # Output: 34

# 2. Using summ (recursive approach)
n = 5  # Example n
print("Sum of first", n, "natural numbers (recursive):", summ(n))  # Output: 15