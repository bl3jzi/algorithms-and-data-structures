"""
Intuition:

A divide-and-conquer algorithm that selects a "pivot" element and partitions 
the array around it—rearranging elements so that values smaller than the pivot
shift to its left and values greater shift to its right. It then recursively 
sorts the resulting sub-arrays in-place.


Mechanics:

1. Base Case: If the subarray range contains 0 or 1 elements (p >= r), return.
2. Partition:
   - Lomuto: Select the last element as pivot. Scan left-to-right, maintaining a 
     boundary of elements <= pivot. Swap pivot into its exact final rank q.
   - Hoare: Select the first element as pivot. Use two inward-moving pointers (i, j) 
     until inversions are found, swapping them until pointers cross at split index q.
3. Divide & Conquer:
   - Lomuto: Recurse on [p, q - 1] and [q + 1, r] (pivot is already finalized).
   - Hoare: Recurse on [p, q] and [q + 1, r] (pivot is not guaranteed to be at q).
4. Tail-Call Optimization: Recurse only on one partition while looping on the other 
   to reduce call-stack consumption.


Complexity:
    Time:
        O( n log n ) - best / average (balanced splits dividing data roughly in half)
        O( n^2 )     - worst (severely skewed splits, e.g., already sorted array with 
                       first/last element chosen as pivot)

    Space:
        O( log n )   - average call-stack depth
        O( n )       - worst-case call-stack depth (mitigated to O(log n) if always 
                       recursing on the smaller partition first)
        O( 1 )       - auxiliary heap memory (strictly in-place)

    Variables:
        n - number of elements in the array
        p - starting index of current subarray
        r - ending index of current subarray (inclusive)
        q - split/partition boundary index
"""


# =====================================================================
# 1. Lomuto Partition Scheme (Simpler, Pivot Placed at Final Position)
# =====================================================================


def partition_lomuto(A: list[int], p: int, r: int) -> int:
    pivot = A[r]  # Choose last element as pivot
    i = p - 1  # Boundary for elements <= pivot

    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    # Place pivot in its exact sorted location
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort_lomuto(A: list[int], p: int, r: int) -> None:
    if p < r:
        q = partition_lomuto(A, p, r)
        quick_sort_lomuto(A, p, q - 1)  # Exclude pivot (already sorted)
        quick_sort_lomuto(A, q + 1, r)


# =====================================================================
# 2. Hoare Partition Scheme (Faster in practice, fewer swaps)
# =====================================================================


def partition_hoare(A: list[int], p: int, r: int) -> int:
    pivot = A[p]  # Choose first element as pivot
    i = p - 1
    j = r + 1

    while True:
        i += 1
        while A[i] < pivot:
            i += 1

        j -= 1
        while A[j] > pivot:
            j -= 1

        if i >= j:
            return j

        A[i], A[j] = A[j], A[i]


def quick_sort_hoare(A: list[int], p: int, r: int) -> None:
    if p < r:
        q = partition_hoare(A, p, r)
        quick_sort_hoare(A, p, q)  # Note: Includes q (pivot not finalized)
        quick_sort_hoare(A, q + 1, r)


# =====================================================================
# 3. Tail-Call Optimization (Prevents RecursionStack Overflow)
# =====================================================================


def quick_sort_tail_call(A: list[int], p: int, r: int) -> None:
    while p < r:
        q = partition_lomuto(A, p, r)

        # Recurse on the smaller half first to guarantee O(log n) stack depth
        if (q - 1) - p < r - (q + 1):
            quick_sort_tail_call(A, p, q - 1)
            p = q + 1  # Eliminate tail recursion for right half
        else:
            quick_sort_tail_call(A, q + 1, r)
            r = q - 1  # Eliminate tail recursion for left half