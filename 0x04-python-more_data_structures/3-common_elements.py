#!/usr/bin/python3
def common_elements(set_1, set_2):
    list1 = list(set_1)
    list2 = list(set_2)
    indices_present = [value for index, value in enumerate(list1) if value in list2]
    set1 = set(indices_present)
    return indices_present
