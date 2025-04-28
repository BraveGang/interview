"""
给定一个未排序的整数数组 nums , 找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9

进阶：可以设计并实现时间复杂度为 O(n) 的解决方案吗？

https://leetcode.cn/problems/longest-consecutive-sequence/


方法思路:

1.使用哈希集合：首先将所有元素存入哈希集合中，以便在O(1)时间内检查元素是否存在。
2.遍历元素：遍历哈希集合中的每个元素，检查当前元素是否可以作为某个连续序列的起点（即当前元素的前一个元素不在集合中）。
3.扩展序列：对于每个可能的起点元素，依次检查其后续元素是否存在，统计当前连续序列的长度。
4.更新最大值：在遍历过程中，不断更新最长连续序列的长度。

这种方法的时间复杂度为O(n)，其中n是数组的长度，因为每个元素最多被访问两次（一次作为起点，一次作为连续序列中的元素）。空间复杂度为O(n)，用于存储哈希集合。

"""

def longestConsecutive(nums):
    # set 集合辅助验证,升序排列
    nums_set = set(nums)
    max_length = 0

    for num in nums_set:
        # 某个连续序列的起点
        if num - 1 not in nums_set:
            current_num = num
            current_length = 1

            while current_num + 1 in nums_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length


if __name__ == '__main__':
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(longestConsecutive(nums))
