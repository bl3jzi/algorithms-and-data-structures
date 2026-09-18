"""
Intuition:

Sorts an array iteratively from the bottom up by treating individual elements
as sorted runs of length 1, then progressively merging adjacent runs of doubling
lengths (1, 2, 4, 8, ...) until the entire collection forms a single sorted array,
completely eliminating recursive call-stack overhead.


Mechanics:

1. Initialize run size curr_size = 1 and allocate an auxiliary buffer B of size n.
2. Traverse the array in pairs of subarrays of length curr_size.
3. Merge each pair of adjacent subarrays into the auxiliary buffer using two pointers.
4. Copy the merged sub-segment from the buffer back into the original array.
5. Double the subarray size (curr_size = 2 * curr_size) and repeat until curr_size >= n.


Complexity:
    Time:
        O( n log n ) - best / average / worst (guaranteed across all distributions;
                       requires ceiling(log2(n)) passes, each taking O(n) merge work)

    Space:
        O( n ) - auxiliary buffer B of size n (O(1) call stack space,
                 unlike recursive merge sort which uses O(log n) stack)

    Variables:
        n - number of elements in the input list
"""


def merge(T: list[int], B: list[int], left: int, mid: int, right: int) -> None:
    i = left
    j = mid
    k = left

    # Merge elements in sorted order into buffer B
    while i < mid and j < right:
        if T[i] <= T[j]:  # '<=' preserves stability
            B[k] = T[i]
            i += 1
        else:
            B[k] = T[j]
            j += 1
        k += 1

    # Copy any remaining elements from the left subarray
    while i < mid:
        B[k] = T[i]
        i += 1
        k += 1

    # Copy any remaining elements from the right subarray
    while j < right:
        B[k] = T[j]
        j += 1
        k += 1

    # Copy the merged slice back to original array T
    for idx in range(left, right):
        T[idx] = B[idx]


def merge_sort(T: list[int]) -> list[int]:
    n = len(T)
    if n <= 1:
        return T

    B = [0] * n
    curr_size = 1

    # Outer loop runs ceil(log2(n)) times
    while curr_size < n:
        left_start = 0

        # Inner loop sweeps through the array in chunks of 2 * curr_size
        while left_start < n:
            mid = min(left_start + curr_size, n)
            right_end = min(left_start + 2 * curr_size, n)

            merge(T, B, left_start, mid, right_end)
            left_start += 2 * curr_size

        curr_size *= 2

    return T
