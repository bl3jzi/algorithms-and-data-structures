"""
Intuition:

Sorts multi-digit integers position by position, moving from the least significant
digit (LSD) to the most significant digit (MSD). By using a stable intermediate
sorter (Counting Sort), the relative order established by lower-order digits is
preserved as higher-order digits are processed.


Mechanics:

1. Find the maximum element to determine the total number of digit places d.
2. Initialize the place-value exponent (exp = 1, representing the 1s, 10s, 100s, ...).
3. Extract the current digit key `(val // exp) % 10` for each element.
4. Perform a stable Counting Sort pass on the array using the extracted digits:
   - Compute frequency counts for digits 0 through 9.
   - Calculate prefix sums to determine the destination offsets.
   - Traverse the input array backward to preserve stability while writing to a temporary array.
5. Copy the sorted pass back to the source array.
6. Multiply exp by 10 and repeat until the largest value has been fully processed.


Complexity:
    Time:
        O( d * (n + b) ) - best / average / worst (strictly deterministic runtime)
                           where d is digits count, n is element count, b is radix base (10)

    Space:
        O( n + b ) - auxiliary buffer of size n plus count array of size b (10)

    Variables:
        n - number of elements in the array
        d - maximum number of digits in the largest key (floor(log_b(max_val)) + 1)
        b - base / radix of the number system (b = 10 for decimal)
        exp - current digit place-value multiplier (1, 10, 100, ...)
"""


def count_sort_radix(T: list[int], exp: int) -> None:  # O(n + b)
    n = len(T)
    RADIX_BASE = 10

    count = [0] * RADIX_BASE
    sorted_list = [0] * n

    # Step 1: Count digit occurrences
    for i in range(n):
        digit = (T[i] // exp) % RADIX_BASE
        count[digit] += 1

    # Step 2: Prefix sums for starting target indices
    for i in range(1, RADIX_BASE):
        count[i] += count[i - 1]

    # Step 3: Stable placement (traverse backward)
    for i in range(n - 1, -1, -1):
        digit = (T[i] // exp) % RADIX_BASE
        count[digit] -= 1
        sorted_list[count[digit]] = T[i]

    # Step 4: Copy back to original array
    for i in range(n):
        T[i] = sorted_list[i]


def radix_sort(T: list[int]) -> list[int]:  # O(d * (n + b))
    if len(T) <= 1:
        return T

    max_num = max(T)
    exp = 1

    while max_num // exp > 0:
        count_sort_radix(T, exp)
        exp *= 10

    return T