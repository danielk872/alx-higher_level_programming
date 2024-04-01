#!/usr/bin/python3

def uniq_add(my_list=[]):
    summed = 0
    new_list = set(my_list)
    for i in new_list:
        summed = summed + i
    return summed
