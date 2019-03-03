# question description:
# Given an array of integers, every element appears three times except for one, which appears exactly once.
# Find that single one.


# class Solution(object):

def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    d = {}
    for n in nums:
        if n in d.keys():
            d[n] += 1
        else:
            d[n] = 1

    for k in d.keys():
        if d[k] == 1:
            print(k)

l = [1]

single_number(l)
