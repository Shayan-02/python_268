def sumNums(a, b):
    global c
    c = a + b
    return c


def sayHello():
    return "hi"


sumNums(5, 6)

c *= 2

print(c)

a = sayHello()
print(type(sayHello()))


def f2():
    global y
    x = 5
    y = 6
    print([x, y])
print(y)
f2()