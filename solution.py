def find_smallest_int(arr):
    a = len(arr)
    count = 0
    s = arr[0]
    while count < (a):
        if s > arr[count]: s = arr[count]
        count += 1
    return s
