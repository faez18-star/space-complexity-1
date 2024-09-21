# Function to print "Codingal" recursively and calculate time complexity
def prints(n):
    # Base case: If n is less than or equal to 0, stop the recursion
    if n <= 0:
        return

    # Print the message
    print("Codingal")

    # Recursive case: Call the function with integer division by 2
    prints(n // 2)  # First recursive call, dividing n by 2
    prints(n // 2)  # Second recursive call, dividing n by 2 again

# Test the function with an example
prints(8)  # Call the function with an integer n, e.g., 8