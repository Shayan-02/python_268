import random
lst = []
a = int(input("enter first number: "))
b = int(input("enter second number: "))
for i in range (1, 101):
    i = random.randint(a, b)
    lst.append(i)
print(lst)