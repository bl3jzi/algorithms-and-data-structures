"""
Intuition:

Partitions an array into smaller intervals (buckets),
sorts each bucket independently, and stitches them back together.


Mechanics:

1. Divide a given range of numbers into k buckets of equal range.
2. Assign the numbers to the corresponding buckets.
3. Sort numbers in non-empty buckets using insertion sort.
4. Concatenate all sorted buckets into the original array.


Complexity:
    Time:
        O( n + k ) - average / occurs when input is uniformly distributed across buckets.
        O( n^2 )  - worst / occurs when all elements cluster into a single bucket

    Space:
        O( n + k ) - additional space for buckets

Variables:
        n - number of elements in the input list
        k - number of buckets
"""


def bucket_sort(T: list[int]) -> list[int]:
    n = len(T)
    buckets = [[] for _ in range(n)]

    min_val = min(T)
    max_val = max(T)
    if max_val == min_val:
        return T

    for num in T:
        bi = int((num - min_val) / (max_val - min_val) * (n - 1))
        bi = min(bi, n - 1)
        buckets[bi].append(num)

    for bucket in buckets:
        insertion_sort(bucket)

    index = 0

    for bucket in buckets:
        for num in bucket:
            T[index] = num
            index += 1

    return T


def insertion_sort(bucket: list[int]) -> list[int]:
    n = len(bucket)

    for i in range(1, n):
        pom = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > pom:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = pom
    return bucket
