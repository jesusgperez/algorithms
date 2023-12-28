from typing import List, Tuple, Optional
from data_structures.domain import (
    Node
)
from algos.sorting import (
    quick_sort,
    merge_sort,
    get_partition,
)
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

    return highest_start, lowest_end


def merge_overlapping_intervals(
    array: List[Tuple[int, int]]
) -> Tuple[int, int]:
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


def find_median(array: List[int]) -> int:
    median = math__floor(len(array)/2)
    return find_media_by_partition(
        array=array,
        low=0,
        high=len(array) - 1,
        median=median
    )


# Use partition logic to find median in linear time
def find_media_by_partition(
    array: List[int],
    low: int,
    high: int,
    median: int
) -> int:
    if low > high:
        return -1

    partition = get_partition(array, low, high)

    if partition > median:
        return find_media_by_partition(
            array=array,
            low=low,
            high=partition - 1,
            median=median
        )
    elif partition < median:
        return find_media_by_partition(
            array=array,
            low=partition + 1,
            high=high,
            median=median
        )

    return array[partition]


def divide_negatives_and_positives(array: List[int]) -> List[int]:
    return divide_negatives_and_positives_recursive(
        array=array,
        low=0,
        high=len(array) - 1
    )


def divide_negatives_and_positives_recursive(
    array: List[int],
    low: int,
    high: int
) -> List[int]:
    partition = get_partition(array=array, low=low, high=high)

    if partition < 0:
        return divide_negatives_and_positives_recursive(
            array=array, low=partition + 1, high=high
        )
    elif partition > 0:
        return divide_negatives_and_positives_recursive(
            array=array, low=low, high=partition - 1
        )

    return array


def reconstruct_queue_by_height(
    array: List[List[int]]
) -> List[List[int]]:
    n = len(array)
    new_array = sorted(array, key=lambda x: (-x[0], x[1]))

    response = []

    for i in range(n):
        response.insert(new_array[i][1], new_array[i])

    return response


def merge_sorted_lists(
    lists: List[Optional[Node]],
    low: int,
    high: int
):
    if low > high:
        return

    if low == high:
        return lists[low]

    mid = math__floor((low + high)/2)

    left = merge_sorted_lists(lists=lists, low=low, high=mid)
    right = merge_sorted_lists(lists=lists, low=mid + 1, high=high)

    return merge_lists(left=left, right=right)


def merge_lists(left: Optional[Node], right: Optional[Node]):
    if not left:
        return right
    if not right:
        return left

    response = None

    if left.data <= right.data:
        response = Node(data=left.data)
        response.next = merge_lists(left=left.next, right=right)
    else:
        response = Node(data=right.data)
        response.next = merge_lists(left=left, right=right.next)

    return response


def k_smallest_pairs(
    nums1: List[int],
    nums2: List[int],
    k: int
) -> List[Tuple[int, int]]:
    i = 0
    j = 0
    count = 0

    response = []

    while count < 2*k:
        max_array = nums1 if nums1[i] > nums2[j] else nums2

        if nums1[i] <= nums2[j]:
            min_index, min_array = i, nums1
            i += 1
        else:
            min_index, min_array = j, nums2
            j += 1

        inner_count = 0

        while count + inner_count < 2*k and inner_count < len(max_array):
            response.append((min_array[min_index], max_array[inner_count]))
            inner_count += 1

        count += inner_count

    return sorted(response)[:k]
