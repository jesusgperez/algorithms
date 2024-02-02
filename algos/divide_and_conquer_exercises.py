from typing import List, Tuple


def max_crossing_sum(
    array: List[int],
    low: int,
    mid: int,
    high: int
):
    sm = 0
    left_sum = float('-inf')

    for i in range(mid, low - 1, -1):
        sm = sm + array[i]
        if sm > left_sum:
            left_sum = sm

    sm = 0
    right_sum = float('-inf')

    for i in range(mid, high + 1):
        sm = sm + array[i]
        if sm > right_sum:
            right_sum = sm

    return max(left_sum + right_sum - array[mid], left_sum, right_sum)


def largest_subrange(
    array: List[int],
    low: int,
    high: int
) -> int:
    if low > high:
        return float('-inf')

    if low == high:
        return array[low]

    mid = (low + high) // 2

    left_subarray = largest_subrange(array=array, low=low, high=mid - 1)
    right_subarray = largest_subrange(array=array, low=mid + 1, high=high)
    mid_subarray = max_crossing_sum(array=array, low=low, mid=mid, high=high)

    return max(left_subarray, right_subarray, mid_subarray)


def kadane_max_subarray_sum(
    array: List[int]
) -> Tuple[int, List[int]]:
    size = len(array)
    max_so_far = float('-inf')
    max_ending_here = 0
    start, end, s = 0, 0, 0

    for i in range(0, size):
        max_ending_here += array[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    return max_so_far, array[start:max_so_far]


def cut_is_valid(wood: List[int], n: int, curr: int, k: int) -> bool:
    count = 0

    for i in range(n):
        count += wood[i] // curr
    
    return count >= k


def maximum_wood_cut(wood: List[int], n: int, k: int) -> int:
    left = 1
    right = max(wood)

    while left <= right:
        mid = left + (right - left) // 2

        if cut_is_valid(wood=wood, n=n, curr=mid, k=k):
            left = mid + 1
        else:
            right = mid - 1

    return right


def find_median_recursive(
    min_arr: List[int],
    max_arr: List[int],
    min_l: int,
    min_h: int,
    max_l: int,
    max_h: int,
    previous: int
) -> int:
    m = (min_l + min_h) // 2
    n = (max_l + max_h) // 2

    if min_l >= min_h:
        return max_arr[min_h]

    if max_l >= max_h:
        return min_arr[max_h]

    if min_arr[n] > max_arr[m]:
        return min_arr[n]

    if not previous % 2:
        return find_median_recursive(
            min_arr=min_arr,
            max_arr=max_arr,
            min_l=m,
            min_h=min_h,
            max_l=max_l,
            max_h=max_h,
            previous=previous+1
        )
    return find_median_recursive(
        min_arr=min_arr,
        max_arr=max_arr,
        min_l=min_l,
        min_h=min_h,
        max_l=max_l,
        max_h=n,
        previous=previous+1
    )


def median_sorted_arrays(nums1: List[int], nums2: List[int]) -> int:
    min_arr = nums1 if nums1[0] < nums2[0] else nums2
    max_arr = nums1 if nums1[0] > nums2[0] else nums2
    return find_median_recursive(
        min_arr=min_arr,
        max_arr=max_arr,
        min_l=0,
        min_h=len(min_arr)-1,
        max_l=0,
        max_h=len(max_arr)-1,
        previous=0
    )
