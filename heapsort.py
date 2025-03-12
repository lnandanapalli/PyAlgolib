def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def heapify(arr, i, heapsize):
    l = left(i)
    r = right(i)
    largest = i
    if l < heapsize and arr[l] > arr[i]:
        largest = l
    if r < heapsize and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp
        heapify(arr, largest, heapsize)


def build_heap(arr, heapsize=None):
    if heapsize is None:
        heapsize = len(arr)
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i, heapsize)


def heapsort(arr):
    heapsize = len(arr)
    build_heap(arr, heapsize)
    for i in range(len(arr) - 1, 0, -1):
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp
        heapsize -= 1
        heapify(arr, 0, heapsize)


if __name__ == "__main__":
    arr = [5, 3, 4, 1, 2]
    heapsort(arr)
    print(arr)
