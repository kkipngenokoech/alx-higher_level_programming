#!/usr/bin/python3
for count in range(0,100):
    if count < 10:
        count = "0"+str(count)
    elif count == 99:
        print(count)
        continue
    print(count, ",", end="")
