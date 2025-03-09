def merge(arr, start, mid, end):
    start1 = start
    end1 = mid
    start2 = mid + 1
    end2 = end
    temp = []
    while start1 <= end1 and start2 <= end2:
        # add the smallest element into temporary storage
        if arr[start1] <= arr[start2]:
            temp.append(arr[start1])
            start1 += 1
        else:
            temp.append(arr[start2])
            start2 += 1
    while start1 <= end1:
        temp.append(arr[start1])
        start1 += 1
    while start2 <= end2:
        temp.append(arr[start2])
        start2 += 1
    for i in range(end - start + 1):
        arr[start + i] = temp[i]


def mergesort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    # If less than or equal to one element
    if end <= start:
        return
    mid = (start + end) // 2
    mergesort(arr, start, mid)
    mergesort(arr, mid + 1, end)
    merge(arr, start, mid, end)


if __name__ == "__main__":
    arr = [5, 3, 2, 4, 1]
    mergesort(arr)
    print(arr)
