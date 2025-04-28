"""
输入一个 递增排序 的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
如果有多对数字的和等于s，则输出任意一对即可。

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]

https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof/
"""
from typing import List

'''双指针法 两边计算求和 -- 前提是递增排序'''


def twoSum(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target:
            return [nums[left], nums[right]]
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            left += 1
    return []


'''暴力枚举法 -- 对数据是否有序均适用,缺点是时间复杂度变高'''


def twoSum2(nums: List[int], target: int) -> List[int]:
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[j] == target - nums[i]:
                return [nums[i], nums[j]]
    return []


if __name__ == '__main__':
    nums = [10, 26, 30, 31, 47, 60]
    print(twoSum(nums, 40))
    print(twoSum2(nums, 40))
