from random import randint

a = int(input("enter number1: "))
b = int(input("enter number2: "))


random_number = randint(a, b)
# elif b > a:
#     random_number = randint(b, a)
# else:
#     print("the numbers are the same")

for i in range(1, 6):
    guess = int(input(f"guess {i}: "))
    if guess < a or guess > b:
        print(f"please enter a number between {a} and {b}")
    if guess == random_number:
        print(f"you got it in {i} tries")
        break
    elif guess < random_number:
        print("too low")
    elif guess > random_number:
        print("too high")
print("the correct number is: ", random_number)