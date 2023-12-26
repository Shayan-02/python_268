import random
import string

n = int(input("How many characters would you like your password to be? "))
random_string = ''.join(random.choice(string.hexdigits) for _ in range(n))
print(random_string)
