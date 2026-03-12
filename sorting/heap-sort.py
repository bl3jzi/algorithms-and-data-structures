# Kopiec jest drzewem binarnym, w którym zawartość każdego z węzłów jest większa,
# lub równa zawartości węzłów w jego pod drzewie.

def parent(i):
    return (i-1) // 2

def left(i):
    return i * 2 + 1

def right(i):
    return i * 2 + 2

def heapify(A,n,i): # O( log n )
    max_ind = i
    if left(i) < n and A[left(i)] > A[max_ind]:
        max_ind = left(i)
    if right(i) < n and A[right(i)] > A[max_ind]:
        max_ind = right(i)
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A,n,max_ind)

def build_heap(A): # O( n )
    n = len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A,n,i)

def heap_sort(A): # O( n log n )
    n = len(A)
    build_heap(A)
    for i in range(n-1):
        A[0], A[n-i-1] = A[n-i-1], A[0]
        heapify(A,n-i-1,0)