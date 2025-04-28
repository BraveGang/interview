"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素
请注意: 你需要找的是数组排序后的第k个最大的元素，而不是第k个不同的元素
你必须设计并实现时间复杂度为 O(n) 的算法解决此问题

输入: [3,2,1,5,6,4], k = 2
输出: 5

输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4

https://leetcode.cn/problems/xx4gT2/


"""
import heapq


'''基于排序的选择方法'''

def findKthLargest(self, nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]


'''基于堆排序的选择方法'''

def findKthLargest2(nums, k):
    if k < 1 or k > len(nums):
        return -1
    hp = [x for x in nums[:k]]
    heapq.heapify(hp)
    for i in range(k, len(nums)):
        if hp[0] < nums[i]:
            heapq.heappop(hp)
            heapq.heappush(hp, nums[i])
    return heapq.heappop(hp)


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 3
    print(nums)
    print(findKthLargest2(nums, k))
