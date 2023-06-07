#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newList = my_list.copy()
    for index in range(0, len(my_list)-1):
        if my_list[index] % 2 == 0:
            newList[index] = True
        else:
            newList[index] = False
    return newList
