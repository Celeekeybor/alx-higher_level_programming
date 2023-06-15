#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    sm_wt = sum(x * y for x, y in my_list)
    tt_wt = sum(y for _, y in my_list)

    return sm_wt / tt_wt
