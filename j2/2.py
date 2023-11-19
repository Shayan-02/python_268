fnum = int(input("enter first number: "))
op = input("enter operator: ")
snum = int(input("enter second number: "))

if op == "+":
    print(f"{fnum} {op} {snum} ali {fnum + snum}")
elif op == "-" :
    print(f"{fnum} {op} {snum} ali {fnum - snum}")
elif op == "*":
    print(f"{fnum} {op} {snum} ali {fnum * snum}")
elif op == "/" :
    print(f"{fnum} {op} {snum} ali {fnum / snum}")
else:
    print("invalid operator")