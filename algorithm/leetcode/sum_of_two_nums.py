def func(nums, target):
    length = len(nums)
    for i in range(length):
        j = i + 1
        while j < length:
            if nums[i] + nums[j] == target:
                print("{}, {}".format(nums[i], nums[j]))
            j += 1


def find_insert(nums, target):
    length = len(nums)
    for i in range(length):
        if nums[i] == target or nums[i] > target:
            return i
        if i == length - 1:
            return length
    return -1


def find_insert_2(nums, target):
    length = len(nums)
    lo = 0
    hi = length - 1
    while lo < hi:
        mid = int(lo + (hi - lo) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    mid = int(lo + (hi - lo) / 2)
    if mid == 0 and nums[mid] > target:
        return mid
    else:
        return mid + 1


if __name__ == '__main__':
    lists = [1, 3, 5, 6]
    print(find_insert_2(lists, 6))
