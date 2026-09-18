"""
Intuition:

Transforms the array into a max-heap where the root is always the largest element.
It repeatedly swaps the root with the last unsorted element, shrinks the active heap 
boundary, and restores the heap property to sort the array in-place.


Mechanics:

1. Build a max-heap from the unsorted array in bottom-up fashion.
2. Swap the root (maximum value at index 0) with the last element of the active heap.
3. Shrink the active heap size by 1.
4. Call heapify on the root to sift the new root down to its correct position.
5. Repeat steps 2-4 until all elements are sorted.


Complexity:
    Time:
        O( n log n ) - best / average / worst (guaranteed upper bound across all cases)

    Space:
        O( 1 ) - in-place auxiliary space (or O( log n ) call stack due to recursion)

    Variables:
        n - number of elements in the input list
"""


def parent(i: int) -> int:
    return (i - 1) // 2


def left(i: int) -> int:
    return 2 * i + 1


def right(i: int) -> int:
    return 2 * i + 2


def heapify(A: list[int], n: int, i: int) -> None:  # O( log n )
    max_ind = i
    l = left(i)
    r = right(i)

    if l < n and A[l] > A[max_ind]:
        max_ind = l
    if r < n and A[r] > A[max_ind]:
        max_ind = r

    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, n, max_ind)


def build_heap(A: list[int]) -> None:  # O( n )
    n = len(A)
    for i in range(parent(n - 1), -1, -1):
        heapify(A, n, i)


def heap_sort(A: list[int]) -> list[int]:  # O( n log n )
    n = len(A)
    build_heap(A)

    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)

    return A