from typing import List
from math import floor as math__floor


def merge_sort(array: List[int], low: int, high: int) -> None:
    if low < high:
        mid = math__floor((low + high)/2)
        merge_sort(array=array, low=low, high=mid)
        merge_sort(array=array, low=mid + 1, high=high)

        merge(array=array, low=low, mid=mid, high=high)


def merge(array: List[int], low: int, mid: int, high: int) -> None:
    left_buffer = [array[i] for i in range(low, mid + 1)]
    right_buffer = [array[i] for i in range(mid + 1, high + 1)]

    i = low

    while left_buffer and right_buffer:
        if left_buffer[0] <= right_buffer[0]:
            array[i] = left_buffer.pop(0)
        else:
            array[i] = right_buffer.pop(0)

        i += 1

    while left_buffer:
        array[i] = left_buffer.pop(0)
        i += 1

    while right_buffer:
        array[i] = right_buffer.pop(0)
        i += 1


def quick_sort(array: List[int], low: int, high: int) -> List[int]:
    if low < high:
        partition = get_partition(array=array, low=low, high=high)
        quick_sort(array=array, low=low, high=partition - 1)
        quick_sort(array=array, low=partition + 1, high=high)


def get_partition(array: List[int], low: int, high: int) -> int:
    p = high
    first_high = low

    for i in range(low, high):
        if array[i] < array[p]:
            array_swap(
                array=array,
                left_position=i,
                right_position=first_high
            )

            first_high += 1

    array_swap(
        array=array,
        left_position=p,
        right_position=first_high
    )

    return first_high


def array_swap(
    array: List[int],
    left_position: int,
    right_position: int
) -> None:
    buffer = array[left_position]
    array[left_position] = array[right_position]
    array[right_position] = buffer
