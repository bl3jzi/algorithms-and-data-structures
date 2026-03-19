# Merge sort without recursion / no stack used
# Bottom up approach

def merge(T,B,l,mid,r):
    i = k = l
    j = mid

    while i < mid and j < r:
        if T[i] <= T[j]:
            B[k] = T[i]
            i += 1
        else:
            B[k] = T[j]
            j+= 1
        k += 1

    while i < mid:
        B[k] = T[i]
        i += 1
        k += 1

    while j < r:
        B[k] = T[j]
        j += 1
        k += 1

    for i in range(l,r):
        T[i] = B[i]

def merge_sort(T):
    n = len(T)
    B = [0] * n

    curr_size = 1
    while curr_size <= n:
        left_start = 0

        while left_start < n:

            mid = min(left_start + curr_size, n)
            right_end = min(left_start + 2 * curr_size,n)

            merge(T, B, left_start, mid, right_end)
            left_start += 2*curr_size

        curr_size = 2 * curr_size
    return T
