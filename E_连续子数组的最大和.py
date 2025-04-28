"""

小红书一面:

输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6

https://leetcode.cn/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/

"""


"""
动态规划
f(i) = max{f(i-1)+nums[i],nums[i]}
"""


def max_subarray_sum(nums):

    if not nums:
        return 0

    max_current = nums[0]
    max_global = nums[0]

    for num in nums[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)

    return max_global


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(nums)
    print(max_subarray_sum(nums))
