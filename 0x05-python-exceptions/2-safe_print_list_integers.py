#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            counter += 1
        except ValueError:
            continue
        except IndexError:
            print("IndexError: list index out of range")
        except:
            pass
    return counter
