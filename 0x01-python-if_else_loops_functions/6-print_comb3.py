#!/usr/bin/python3
for i in range(100):
    if int(i / 10) != i % 10 and int(i / 10) < i % 10:
        print("{}{}".format(int(i / 10), i % 10), end="")
