

def binary_exponentiation(a, b):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2
    return result

# Example usage:
print(binary_exponentiation(2, 10))  # Output: 1024
