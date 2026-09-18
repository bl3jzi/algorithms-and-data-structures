"""
Intuition:

A classic top-down divide-and-conquer algorithm that recursively splits an array
into two halves until base-case segments of length 1 remain, then merges
the sorted halves back together in linear time using a pre-allocated auxiliary buffer.


Mechanics:

1. Check if the sub-array contains more than one element (r - p > 1).
2. Divide the interval [p, r) at the midpoint q = (p + r) // 2.
3. Recursively sort the left half [p, q) and the right half [q, r).
4. Merge the two adjacent sorted halves into auxiliary buffer B.
5. Copy the merged elements from buffer B back into original array A[p:r].


Complexity:
    Time:
        O( n log n ) - best / average / worst (guaranteed across all inputs;
                       recursion tree has depth ceil(log2(n)), each level takes O(n) work)

    Space:
        O( n ) - O(n) auxiliary buffer B + O(log n) call stack frames

    Variables:
        n - total number of elements in the array
        p - start index of current subarray (inclusive)
        q - midpoint index dividing left and right halves
        r - end index of current subarray (exclusive)
"""


def merge( A: list[int], B: list[int], p: int, q: int, r: int) -> None:  # O(r - p)
    i = p
    j = q
    k = p

    # Merge sorted halves [p, q) and [q, r) into buffer B
    while i < q and j < r:
        if A[i] <= A[j]:  # '<=' preserves stability
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1

    # Copy remaining elements from left half
    while i < q:
        B[k] = A[i]
        i += 1
        k += 1

    # Copy remaining elements from right half
    while j < r:
        B[k] = A[j]
        j += 1
        k += 1

    # Copy merged range back to original array A
    for t in range(p, r):
        A[t] = B[t]


def mergesort( A: list[int], B: list[int], p: int, r: int) -> None:  # O(n log n)
    if r - p > 1:
        q = (p + r) // 2
        mergesort(A, B, p, q)
        mergesort(A, B, q, r)
        merge(A, B, p, q, r)


def msort(A: list[int]) -> list[int]:
    n = len(A)
    if n <= 1:
        return A

    # Allocate auxiliary buffer once upfront to avoid O(n log n) allocations
    B = [0] * n
    mergesort(A, B, 0, n)

    return A