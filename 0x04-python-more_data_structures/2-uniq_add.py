#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = list(set(my_list))

    findsum = 0
    for index in range(0, len(my_list)):
            findsum += my_list[index]
    return findsum
