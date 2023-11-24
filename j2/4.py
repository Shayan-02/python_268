f1 = 1
f2 = 1
n = int(input("Enter a number: "))
if n == 1:
    print(f1)
elif n == 2:
    print(f1, f2,  sep="\n")
else:
    print(f1, f2, sep="\n")
    i = 3
    while i <= n:
        f3 = f1 + f2
        print(f3, sep="\n")
        f1 = f2
        f2 = f3
        i += 1