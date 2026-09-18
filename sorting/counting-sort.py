"""
Intuition:

Counts the occurrences of each unique value and uses prefix sums
to place every element directly into its exact sorted position without comparisons.


Mechanics:

1. Find the maximum value k and initialize a count array of size k + 1.
2. Count the frequency of each element in the input array.
3. Compute cumulative sums (prefix sums) to determine the starting positions for each key.
4. Iterate backward through the input array and place each element into the sorted list.


Complexity:
    Time:
        O( n + k ) - best / average / worst (runs in deterministic linear time)

    Space:
        O( n + k ) - auxiliary space for the count array of size (k + 1) and output array of size n

    Variables:
        n - number of elements in the input list
        k - maximum value in the input list (max_val)
"""


def counting_sort(T: list[int]) -> list[int]:
    n = len(T)
    if n <= 1:
        return T

    max_val = max(T)
    values = [0] * (max_val + 1)
    sorted_list = [0] * n

    # Step 2: Frequency count
    for i in range(n):
        values[T[i]] += 1

    # Step 3: Prefix sums (positions)
    for i in range(1, len(values)):
        values[i] = values[i] + values[i - 1]

    # Step 4: Build sorted array (backward traversal ensures stability)
    for i in range(n - 1, -1, -1):
        values[T[i]] -= 1
        sorted_list[values[T[i]]] = T[i]

    return sorted_list
