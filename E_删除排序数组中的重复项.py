"""
E_删除排序数组中的重复项:

给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
元素的 相对顺序 应该保持一致 。

https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
"""

# 双指针- 快慢指针
def removeDuplicates(nums):
    if not nums:
        return 0
    length = len(nums)
    fast = slow = 1
    while fast < length:
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    return slow


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(nums)
    print(removeDuplicates(nums))
    print(nums)
    
