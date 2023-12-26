n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
n3 = int(input("Enter number3"))
maximum = n1
minimum = n1

if n2 > n1 and n3 > n2:
    maximum = n3
elif n2 > n1 and n2 > n3:
    maximum = n2
elif n2 > n1 and n2 == n3:
    maximum = n2
else:
    print("Invalid input")
print(maximum)

if n1 < n2 and n1 < n3:
    minimum = n1
elif n1 < n3 and n1 > n2:
    minimum = n2
elif n3 < n2 and n2 <  n1:
    minimum = n3
else:
    print("Invalid input")

print(minimum)