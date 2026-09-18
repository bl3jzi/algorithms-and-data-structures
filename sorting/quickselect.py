"""
Intuition:

A selection algorithm that finds the k-th smallest element (order statistic)
in an unsorted array without sorting the entire collection. It operates like
QuickSort, but recurses into only the single partition containing index k,
dropping the average runtime from O(n log n) down to linear time O(n).


Mechanics:

1. Select a random pivot index between l and r, and swap it with A[r] to avoid
   pathological O(n^2) worst-case degradation on pre-sorted data.
2. Partition the array such that all elements <= pivot are placed to its left,
   and elements > pivot to its right; the pivot ends at its final sorted rank q.
3. Compare the target rank k with the partition index q:
   - If k == q: the pivot is already at its final sorted position; return A[k].
   - If k < q: the target lies in the left subarray; recurse on [l, q - 1].
   - If k > q: the target lies in the right subarray; recurse on [q + 1, r].


Complexity:
    Time:
        O( n ) - best / average (expected work: n + n/2 + n/4 + ... = 2n)
        O( n^2 ) - worst (consistently choosing the extreme min/max pivot,
                   though random pivot selection makes this statistically negligible)

    Space:
        O( log n ) - average call-stack depth
        O( n ) - worst-case call-stack depth (can be reduced to O(1) iteratively)
        O( 1 ) - auxiliary heap memory (modifies the array in-place)

    Variables:
        n - number of elements in the subarray (r - l + 1)
        k - 0-based target index (0 is minimum, n - 1 is maximum)
        l - start index of current range
        r - end index of current range (inclusive)
"""

import random


def partition(A: list[int], l: int, r: int) -> int:
    # Pick a random pivot and move it to the end
    piv = random.randint(l, r)
    A[piv], A[r] = A[r], A[piv]

    pivot_val = A[r]
    i = l - 1

    for j in range(l, r):
        if A[j] <= pivot_val:
            i += 1
            A[i], A[j] = A[j], A[i]

    # Place pivot into its final sorted position
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quickselect(A: list[int], l: int, r: int, k: int) -> int:
    if l == r:
        return A[l]

    q = partition(A, l, r)

    if k == q:
        return A[k]
    elif k < q:
        return quickselect(A, l, q - 1, k)
    else:
        return quickselect(A, q + 1, r, k)
