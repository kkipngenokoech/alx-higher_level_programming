#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    integers = sys.argv[1:]
    sum = 0
    for item in integers:
        sum += int(item) 
    print("{}".format(sum))
