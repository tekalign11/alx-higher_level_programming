#!/usr/bin/python3
def fizzbuzz():
    for n in range(0, 101):
        if n == 100:
            print("Buzz")
        elif n % 3 == 0:
            print("Fizz", end=", ")
        elif n % 5 == 0:
            print("Buzz", end=", ")
        elif n % 3 and n % 5 == 0:
            print("FizzBuzz", end=", ")
        else:
            print(f"{n}", end=", ")
