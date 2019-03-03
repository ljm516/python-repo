def sub_array_sum(nums, k):
    count = 0
    sum = 0
    d = {}
    for i in nums:
        sum += i
        if sum == k:
            count += 1

        if sum not in d:
            d.pop(sum, 1)
        d.pop(sum, d.get(sum) + 1)
    return count


print(sub_array_sum([1, 1, 1, 1, 1], 2))
