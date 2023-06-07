#!/usr/bin/python3
for count in range(0, 10):
    for counter in range(count, 10):
        if count == 9 and counter == 9:
            print("{}{}".format(count, counter))
            continue
        print("{}{}, ".format(count, counter), end="")

