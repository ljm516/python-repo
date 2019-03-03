# 找出数据中最小元素的下标
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selector_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest_index = find_smallest(arr=arr)
        new_arr.append(arr.pop(smallest_index))

    return new_arr


sort_arr = [4, 2, 5, 3, 1, 6, 8, 7, 9]
print(selector_sort(arr=sort_arr))
