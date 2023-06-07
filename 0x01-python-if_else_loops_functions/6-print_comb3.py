#!/usr/bin/python3
for count in range(0, 10):
    for counter in range(count, 10):
        if count == counter:
            continue
        if count == 8 and counter == 9:
            print("{}{}".format(count, counter))
            continue
        print("{}{}, ".format(count, counter), end="")

