"""
M_三数之和

给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组

注意：答案中不可以包含重复的三元组

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0

不同的三元组是 [-1,0,1] 和 [-1,-1,2]
注意，输出的顺序和三元组的顺序并不重要

https://leetcode.cn/problems/3sum

"""

from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []
        
        n = len(nums)
        
        if n < 3:
            return result

        for i in range(n - 2):
            # 跳过重复的第一个元素
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = n - 1
            
            while left < right:
                
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    
                    result.append([nums[i], nums[left], nums[right]])
                    # 跳过重复的left和right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
                    
        return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))
