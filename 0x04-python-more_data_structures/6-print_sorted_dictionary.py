#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    s = sorted(a_dictionary.keys())
    for i in s:
        print("{}: {}".format(i, a_dictionary[i]))


if __name__ == "__main__":
    print_sorted_dictionary()
