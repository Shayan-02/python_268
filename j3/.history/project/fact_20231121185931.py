n = int(input("Enter a positive integer: "))

factorial = 1

for i in range(n + 1):
    factorial *= i

print(f"The factorial of {n} is {factorial}")