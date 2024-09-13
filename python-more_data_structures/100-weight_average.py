#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    av_weight = 0
    for i in my_list:
        av_weight = (i[0] + i[1]) / i[1]
        
    return av_weight
