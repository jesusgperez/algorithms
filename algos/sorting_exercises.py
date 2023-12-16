from typing import List, Tuple
from algos.sorting import quick_sort, merge_sort
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
    n = len(array)
    starts = [i[0] for i in array]
    ends = [i[1] for i in array]

    merge_sort(starts, low=0, high=n-1)
    merge_sort(ends, low=0, high=n-1)

    total_in, max_in = 0, 0
    highest_start, lowest_end = 0, 0
    i, j = 0, 0

    while i < n and j < n:
        if starts[i] > ends[j]:
            total_in -= 1
            j += 1
            continue

        total_in += 1

        if total_in > max_in:
            max_in = total_in
            highest_start = starts[i]
            lowest_end = ends[j]
        
        i += 1

    return  highest_start, lowest_end


def merge_overlapping_intervals(array: List[Tuple[int, int]]) -> Tuple[int, int]:
    if not array:
        return array

    quick_sort(array=array, low=0, high=len(array)-1)

    response = []
    begin_index = 0
    max_end = 0

    for i in range(1, len(array)):
        if array[max_end][1] < array[i][0]:
            response.append((array[begin_index][0], array[max_end][1]))
            begin_index = i

        if array[max_end][1] < array[i][1]:
            max_end = i

    if not response or response[-1][1] != array[begin_index][1]:
        response.append((array[begin_index][0], array[-1][1]))

    return response


def max_intervals_points(array: List[Tuple[int, int]]) -> Tuple[int, int]:
    return most_people_at_party(array=array)
