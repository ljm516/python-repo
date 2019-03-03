# 实现二分查找
def binary_search(nums, n):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = int((low + high) / 2)

        if nums[mid] == n:
            return mid

        if nums[mid] > n:  # mid too big, change high
            high = mid - 1
        else:  # mid too small, change low
            low = mid + 1

    return -1


num_list = [1, 2, 5, 9, 12, 14, 18, 20, 23, 24, 30]
find = 18

result = binary_search(nums=num_list, n=find)

print("find result: {result}".format(result=result))
