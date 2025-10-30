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
    start, s = 0, 0

    for i in range(0, size):
        max_ending_here += array[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s

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


def median_sorted_arrays(nums1: List[int], nums2: List[int]) -> int:
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(B) < len(A):
        A, B = B, A

    l, r = 0, len(A) - 1

    while True:
        i = (l + r) // 2
        j = half - i - 2

        A_left = A[i] if i >= 0 else float('-inf')
        A_right = A[i + 1] if (i + 1) < len(A) else float('inf')
        B_left = B[j] if j >= 0 else float('-inf')
        B_right = B[j + 1] if (j + 1) < len(B) else float('inf')

        if A_left <= B_right and B_left <= A_right:
            if total % 2:
                return min(A_right, B_right)
            
            return (max(A_left, B_left) + min(A_right, B_right)) / 2
        elif A_left > B_right:
            r = i - 1
        else:
            l = i + 1


def count_range_sum(array: List[int], lower: int, upper: int) -> int:
    n = len(array)
    sums = [0]

    for i in range(n):
        sums.append(sums[i] + array[i])

    return merge_sort_count(
        array=sums,
        low=0,
        high=n,
        lower=lower,
        upper=upper
    )


def merge_sort_count(
    array: List[int],
    low: int,
    high: int,
    lower: int,
    upper: int
) -> int:
    if low >= high:
        return 0

    mid = (high + low + 1) // 2

    left_count = merge_sort_count(
        array=array, low=low, high=mid - 1, lower=lower, upper=upper
    )

    right_count = merge_sort_count(
        array=array, low=mid, high=high, lower=lower, upper=upper
    )

    count = left_count + right_count

    start_ix, end_ix = mid, mid

    for i in range(low, mid):
        while start_ix <= high and array[start_ix] - array[i] < lower:
            start_ix += 1

        while end_ix <= high and array[end_ix] - array[i] <= upper:
            end_ix += 1

        count += (end_ix - start_ix)

    merge_count(array=array, low=low, mid=mid, high=high)

    return count


def merge_count(
    array: List[int],
    low: int,
    mid: int,
    high: int
) -> None:
    left_arr = [array[i] for i in range(low, mid)]
    right_arr = [array[i] for i in range(mid, high)]

    i = low

    while left_arr and right_arr:
        if left_arr[0] <= right_arr[0]:
            array[i] = left_arr.pop(0)
        else:
            array[i] = right_arr.pop(0)

        i += 1

    while left_arr:
        array[i] = left_arr.pop(0)
        i += 1

    while right_arr:
        array[i] = right_arr.pop(0)
        i += 1
