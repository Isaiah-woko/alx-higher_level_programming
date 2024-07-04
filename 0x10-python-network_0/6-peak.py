#!/usr/bin/python3
"""a function that finds a peak in a lst of unsorted integers."""
def find_peak(list_of_integers):
    """finds a peak in a lst of unsorted integers"""
    def binary_search(lst, low, high):
        """using binary search"""
        mid = low + (high - low) // 2
        # check if fthe middle element is a peak
        if (mid == 0 or lst[mid] >= lst[mid - 1]) and (
            mid == len(lst) - 1 or lst[mid] >= lst[mid + 1]):
            return lst[mid]
        elif mid > 0 and lst[mid - 1] > lst[mid]:
            return binary_search(lst, low, mid - 1)
        else:
            return binary_search(lst, mid + 1, high)
        
    if not list_of_integers:
            return None

    return binary_search(list_of_integers, 0, len(list_of_integers) - 1)