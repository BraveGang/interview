"""
美团一面: 考察二分查找,或遍历

给你一个 严格升序排列的正整数数组 arr 和一个整数 k
请你找到这个数组里第 k 个缺失的正整数

输入：arr = [2,3,4,7,11], k = 5
输出：9
解释：缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9

输入：arr = [1,2,3,4], k = 2
输出：6
解释：缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6

https://leetcode.cn/problems/kth-missing-positive-number/


问题分析:

- 数组是严格升序排列的，因此可以利用其有序性进行高效查找。
- 我们需要确定每个元素之前的缺失数目，从而定位到第k个缺失的正整数的位置。

关键观察:

- 对于数组中的第i个元素arr[i]，假设它之前的元素没有缺失，那么它的值应该是i+1。因此，实际值与理想值的差值即为到该位置为止的缺失数目。
- 通过计算每个元素的差值arr[i] - (i+1)，我们可以确定到该位置为止的缺失数目。

算法选择:

- 使用二分查找来找到最大的索引i，使得到该索引位置的缺失数目小于k。这样，第k个缺失的数将位于该索引之后。

复杂度分析:

- 时间复杂度: O(log n)，其中n是数组的长度。二分查找的时间复杂度为对数级别。
- 空间复杂度: O(1)，仅使用常数级别的额外空间。

"""


"""二分查找实现"""

def findKthPositive(nums, k):

    left, right = 0, len(nums) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        # 计算缺失的数目 关键步骤
        missing = nums[mid] - (mid + 1)
        if missing < k:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return k + (ans + 1)



if __name__ == '__main__':
    
    nums = [2, 3, 4, 7, 11]
    print(findKthPositive(nums, 5))
    nums2 = [1, 2, 3, 4]
    print(findKthPositive(nums2, 2))
