#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    if count == 1:
        print("{} argument:".format(count))
    elif count > 1:
        print("{} arguments:".format(count))
    else:
        print('.')
    for index, argument in enumerate(sys.argv):
        if index == 0:
            continue
        print("{}: {}".format(index, argument))
