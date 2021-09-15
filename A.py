import random




def my_sort(arr: list):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[i] < arr[j - 1]:
            j = j - 1
        temp = arr[i]
        del arr[i]
        arr.insert(j, temp)


def my_sort(arr: list):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[i] = arr[i], arr[j]
            # temp = arr[j]
            # arr[j] = arr[j - 1]
            # arr[j - 1] = temp
            j = j - 1


def my_merge(a, b):
    i = 0
    j = 0
    n = len(a)
    m = len(b)
    c = []
    while i + j < m + n:
        if j == m or (i < n and a[i] < b[j]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    return c


def my_merge_sort(arr: list):
    n = len(arr)
    if n == 1:
        return arr
    m = int(n/2)
    arr_l = my_merge_sort(arr[0: m])
    arr_r = my_merge_sort(arr[m:])
    arr = my_merge(arr_l, arr_r)
    return arr


def my_partition(l, r, arr, x):
    m1 = l
    m2 = l + 1
    for i in range(l, r):
        if arr[i] < x:
            arr[m1], arr[i] = arr[i], arr[m1]
            arr[m2], arr[i] = arr[i], arr[m2]
            m1 += 1
            m2 += 1
        elif arr[i] == x:
            arr[m2], arr[i] = arr[i], arr[m2]
            m2 += 1
    return m1, m2


def my_quick_sort(l, r, arr):
    if r - l <= 1:
        return arr
    x = arr[random.randint(l, r - 1)]
    m1, m2 = my_partition(l, r, arr, x)
    my_quick_sort(l, m1, arr)
    my_quick_sort(m2, r, arr)


def solution(inp: str):
    arr = list(map(int, inp.split()))
    # arr = my_merge_sort(arr)
    my_sort(arr)
    my_quick_sort(0, len(arr), arr)
    return ' '.join(map(str, arr))

