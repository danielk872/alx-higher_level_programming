#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx < 0):
        lst = my_list.copy()
        return lst
    elif (idx >= len(my_list)):
        lst = my_list.copy()
        return lst
    else:
        lst = my_list.copy()
        lst[idx] = element
        return lst


if __name__ == "__main__":
    new_in_list()
