"""
M_数组子集:

给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

https://leetcode.cn/problems/subsets/

"""
from typing import List


class Solution:
    """迭代算法"""

    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [[]]
        for num in nums:
            res += [subset + [num] for subset in res]
        return res

    """回溯算法"""

    def subsets2(self, nums: List[int]) -> List[List[int]]:

        res = []
        length = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, length):
                helper(j + 1, tmp + [nums[j]])

        helper(0, [])
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(Solution().subsets(nums))
    print(Solution().subsets2(nums))
