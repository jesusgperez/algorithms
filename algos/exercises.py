from typing import List, Tuple
from math import floor as math__floor


"""
    Checks if k elements sum t in a array
    Time complexity O(n^klog(n))
"""
def k_element_sum(array: List[int], k: int, t: int) -> bool:
    array = sorted(array)

    _, found = k_sum_recursive(array=array, k=k, t=t)

    return found

def k_sum_recursive(array: List[int], k: int, t: int) -> Tuple[int, bool]:
    if k == 0:
        return t, True

    new_t, found = k_sum_recursive(array=array, k=k-1, t=t)

    if not found:
        return -1, found

    for n in array:
        if binary_search(array=array, element=new_t - n):
            return new_t - n, True
    return new_t, False


def binary_search(array: List[int], element: int) -> bool:
    if not array:
        return False
    
    if len(array) < 2:
        return element in array

    low = 0
    high = len(array) - 1
    found = False

    while not found and low <= high:
        mid = math__floor((low + high)/2)
        if element < array[mid]:
            high = mid - 1
            continue
        elif element > array[mid]:
            low = mid + 1
            continue

        found = True

    return found




