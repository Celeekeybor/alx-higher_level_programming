#!/usr/bin/python3
"""function find_peak"""


def find_peak(list_of_integers):
    """list of unsorted integers"""
    li = list_of_integers
    ln = len(li)
    if ln == 0:
        return
    m = ln // 2
    if (m == ln - 1 or li[m] >= li[m + 1]) and (m == 0 or li[m] >= li[m - 1]):
        return li[m]
    if m != ln - 1 and li[m + 1] > li[m]:
        return find_peak(li[m + 1:])
    return find_peak(li[:m])
