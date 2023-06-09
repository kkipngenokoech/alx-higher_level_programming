#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [None] * list_length
    for index in range(list_length):
        try:
            div = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except TypeError:
            div = 0
            print("wrong type")
        except IndexError:
            div = 0
            print("out of range")
        finally:
            new_list[index]  = div
    return (new_list)
