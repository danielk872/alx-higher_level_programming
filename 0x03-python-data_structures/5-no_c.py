#!/usr/bin/python3
def no_c(my_string):
    lst = ""
    for i in my_string:
        if (i != 'c' and i != 'C'):
            lst = lst + i
    return lst


if __name__ == "__main__":
    no_c()
