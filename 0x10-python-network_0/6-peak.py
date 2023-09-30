#!/usr/bin/python3
"""find_peak function"""


def find_peak(list_of_integers):
    """list of unsorted integers"""
    var = list_of_integers
    num = len(var)
    if num == 0:
        return
    m = num // 2
    if (m == num - 1 or var[m] >= var[m + 1]) and (m == 0 or var[m] >= var[m - 1]):
        return var[m]
    if m != num - 1 and var[m + 1] > var[m]:
        return find_peak(var[m + 1:])
    return find_peak(var[:m])
