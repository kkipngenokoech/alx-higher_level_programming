#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
print (digit)
if number >= 0:
    if digit == 0:
        print(f'Last digit of {number} is {number % 10} and is 0')
    elif digit >= 6:
        print(f'Last digit of {number} is {number % 10} and is greater than 5')
    else:
        print(f'Last digit of {number} is {number % 10} and is less than 6 and not 0')
else:
    number = abs(number)
    print(f'Last digit of {number} is {number % 10} and is less than 6 and not 0')
