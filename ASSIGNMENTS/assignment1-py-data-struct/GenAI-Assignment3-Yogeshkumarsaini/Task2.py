# Task 2: Recursive Factorial

def factorial(n):

    if n < 0:
        return "Error: Negative number"

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print("factorial(5):", factorial(5))
print("factorial(0):", factorial(0))
print("factorial(-3):", factorial(-3))