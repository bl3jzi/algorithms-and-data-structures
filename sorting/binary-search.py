"""
Intuition:

An efficient search algorithm for sorted datasets that repeatedly divides
the search space in half. By comparing the target with the middle element,
it eliminates half of the remaining elements in each step until the value
is found or the range becomes empty.


Mechanics:

1. Initialize boundary pointers: low = 0 and high = len(T) - 1.
2. Calculate the middle index: mid = low + (high - low) // 2.
3. Compare target x with middle element T[mid]:
   - If T[mid] == x, return mid (target found).
   - If T[mid] < x, discard the left half by setting low = mid + 1.
   - If T[mid] > x, discard the right half by setting high = mid - 1.
4. Repeat steps 2-3 while low <= high.
5. If pointers cross (low > high), return -1 (target not present).


Complexity:
    Time:
        O( 1 )      - best (target happens to be at the exact first midpoint)
        O( log n )  - average / worst (search space is halved on every iteration)

    Space:
        O( 1 ) - iterative auxiliary memory (constant space)

    Variables:
        n - number of elements in the sorted list
        x - target element being searched
"""


def bin_search(T: list[int], x: int) -> int:
    low = 0
    high = len(T) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if T[mid] == x:
            return mid
        elif T[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found
