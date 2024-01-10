#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    multiply = [(x * y) for x, y in my_list]
    divide = sum(y for x, y in my_list)
    total_sum = sum(multiply) / divide
    return total_sum
