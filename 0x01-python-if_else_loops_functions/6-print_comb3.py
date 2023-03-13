#!/usr/bin/python3
for n in range(0, 9):
    for r in range(0, 10):
        if n == 8 and r == 9:
            print("{}{}".format(n, r))
        elif n < r:
            print("{}{}".format(n, r), end=", ")
