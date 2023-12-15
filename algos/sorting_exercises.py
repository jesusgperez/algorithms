from typing import List, Tuple
from algos.sorting import quick_sort
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


def unique_elements_array(array1: List[int], array2: List[int]) -> List[int]:
    len1, len2 = len(array1), len(array2)
    array = array1 if len1 >= len2 else array2
    other = array1 if len1 < len2 else array2

    i, j = 0, 0

    response = []

    while i < len(array) and j < len(other):
        if array[i] < other[j]:
            response.append(array[i])
            i += 1
        elif array[i] > other[j]:
            response.append(other[j])
            j += 1
        else:
            response.append(array[i])
            i += 1
            j += 1

    while i < len(array):
        response.append(array[i])
        i += 1

    while j < len(other):
            response.append(other[j])
            j += 1

    return response


def most_people_at_party(array: List[Tuple[int, int]]) -> Tuple[int, int]:
    starts = [entrance[0] for entrance in array]
    ends = [entrance[1] for entrance in array]

    quick_sort(starts, low=0, high=len(array)-1)
    quick_sort(ends, low=0, high=len(array)-1)

    j = 0
    start_errased = 0

    while starts[-1] > ends[j] and j < len(array):
        j += 1
        start_errased += 1
    
    i = len(array) - 1
    end_errased = 0

    while starts[i] > ends[0] and i >= 0:
        i -= 1
        end_errased += 1

    return ((starts[-1], ends[j])
            if start_errased < end_errased 
            else (starts[i], ends[0]))


def merge_overlapping_intervals(array: List[Tuple[int, int]]) -> Tuple[int, int]:
    if not array:
        return array

    quick_sort(array=array, low=0, high=len(array)-1)

    response = []

    least_end, least_index = array[0][1], 0
    highest_start, highest_index = array[0][0], 0

    for i in range(len(array)):
        if array[i][0] > highest_start:
            highest_start = array[i][0]
            highest_index = i

        if least_end < highest_start:
            response.append((array[least_index][0], array[highest_index - 1][1]))
            highest_start = array[i][0]
            least_end = array[i][1]
            least_index, highest_index = i, i

    if not response or response[-1][1] != array[highest_index][1]:
        response.append((array[least_index][0], array[-1][1]))

    return response
