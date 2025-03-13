def partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break

        while True:
            j -= 1
            if arr[j] <= pivot:
                break

        if i >= j:
            return j
        else:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp


def quicksort(arr, low, high):
    if low >= high:
        return
    q = partition(arr, low, high)
    quicksort(arr, low, q)
    quicksort(arr, q + 1, high)


if __name__ == "__main__":
    arr = [5, 3, 4, 2, 1]
    quicksort(arr, 0, len(arr) - 1)
    print(arr)
