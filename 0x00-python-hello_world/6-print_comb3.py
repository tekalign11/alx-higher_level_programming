#!/usr/bin/python3
for i in range(0, 10):
    for n in range(digit1 + 1, 10):
        if i == 8 and digit2 == 9:
            print("{}{}".format(i, n))
        else:
            print("{}{}".format(i, n), end=", ")
