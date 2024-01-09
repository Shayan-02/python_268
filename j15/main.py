# import time
# def num(m):
#     t1 = time.time()
#     for i in range(0, m):
#         print(i, end=' ')
#     t2 = time.time()
#     print(str(t2 - t1))
# num(30000)
#
# def f1(a, b=[]):
#     b.append(a)
#     return b
# print(f1(2, [3, 4]))


# def test(*a, b=[]):
#     b = []
#     a = list(a)
#     c = []
#     for i in a:
#         c.append(i)
#         b.append(c)
#
#     print(b)
#
# test([12, 13, 14])

# class Geeks:
#     def __init__(self):
#         self._age = 0
#
#     # using property decorator
#     # a getter function
#     @property
#     def age(self):
#         print("getter method called")
#         return self._age
#
#         # a setter function
#
#     @age.setter
#     def age(self, a):
#         if (a < 18):
#             raise ValueError("Sorry you age is below eligibility criteria")
#         print("setter method called")
#         self._age = a
#
#
# mark = Geeks()
#
# mark.age = 17
#
# print(mark.age)

def get_numbers(*a):
    numbers = []
    while True:
        a = input("enter num: ")
        if a == "":
            break
        number = int(a)
        numbers.append(number)

    return numbers

numbers = get_numbers()
print("list:", numbers)