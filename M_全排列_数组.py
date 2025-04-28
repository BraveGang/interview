"""
全排列_数组:
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

https://leetcode.cn/problems/permutations/description/
"""

from typing import List


'''

方法思路->回溯

回溯算法：通过递归遍历所有可能的排列组合。
标记数组：使用布尔数组记录元素是否已被使用，避免重复选择。
路径管理：维护当前路径，当路径长度等于数组长度时保存结果。
剪枝优化：每次递归时跳过已使用的元素，减少无效搜索。

'''


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    used[i] = False

        backtrack([])
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(Solution().permute(nums))
