#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in new_list:
        if (i == search):
            num = new_list.index(search)
            new_list.pop(num)
            new_list.insert(num, replace)
    return new_list
