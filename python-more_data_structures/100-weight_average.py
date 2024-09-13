#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum_1, sum_2 = 0, 0
    for i in my_list:
        sum_1 += i[0] * i[1]
        sum_2 += i[1]
    return sum_1 / sum_2
