# 递归求和
def get_sum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]

    total = arr[0]
    arr.pop(0)
    total += get_sum(arr)

    return total


# 获取最大数
def get_biggest(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]

    biggest = arr[0]
    for i in range(len(arr)):
        if arr[i] > biggest:
            biggest = arr[i]

    return biggest


def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    small = [i for i in arr[1:] if i <= pivot]
    big = [i for i in arr[1:] if i > pivot]

    print('small: {s}'.format(s=small))
    print('big: {b}'.format(b=big))

    return quick_sort(small) + [pivot] + quick_sort(big)


arr = [1, 2, 4, 6, 3, 5, 8, 9, 7]
# print(get_sum(arr=arr))
# print(get_biggest(arr=arr))

print(quick_sort(arr=arr))
