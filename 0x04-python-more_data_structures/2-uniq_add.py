#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set()
    new_set.update(my_list)
    total_sum = sum(new_set)
    return total_sum
