
def factorial(n):
    if n == 0:
        return 1
    else:
        print("recursion")
        return n * factorial(n - 1)

# Example usage:
print(factorial(5))  # Output: 120
