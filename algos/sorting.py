from typing import List
from math import floor as math__floor


def merge_sort(array: List[int], low: int, high: int):
    if low < high:
        mid = math__floor((low + high)/2)
        merge_sort(array=array, low=low, high=mid)
        merge_sort(array=array, low=mid + 1, high=high)

        merge(array=array, low=low, mid=mid, high=high)

def merge(array: List[int], low: int, mid: int, high: int):
    left_buffer = [array[i] for i in range(low, mid)]
    right_buffer = [array[i] for i in range(mid + 1, high)]

    i = low

    while left_buffer and right_buffer:
        if left_buffer[0] < right_buffer[0]:
            array[i] = left_buffer.pop(0)
        else:
            array[i] = right_buffer.pop(0)
        
        i += 1

    if left_buffer:
        array.extend(left_buffer)
    elif right_buffer:
        array.extend(right_buffer)
