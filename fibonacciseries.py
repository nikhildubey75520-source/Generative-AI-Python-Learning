def print_fibonacci(n):
    """Prints the first n numbers of the Fibonacci sequence."""
    a, b = 0, 1
    
    # Handle negative inputs or zero
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print("Fibonacci sequence:", a)
    else:
        print("Fibonacci sequence:")
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b  # Update a to the next number, and b to the sum

# Example: Print the first 10 Fibonacci numbers
print_fibonacci(10)
 