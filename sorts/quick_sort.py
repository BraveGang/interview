from typing import List

"""
快速排序, 函数递归+双指针实现
"""

def quick_sort(nums, left, right, reverse=False):

    # 判断:递归终止条件
    if left >= right:
        return
    
    # 找到分区点
    pivot = partition(nums, left, right, reverse)
    
    # 递归排序左半部分
    quick_sort(nums, left, pivot - 1, reverse)
    
    # 递归排序右半部分
    quick_sort(nums, pivot + 1, right, reverse)


def partition(nums, left, right, reverse):
    # 以 nums[left] 为基准数
    i, j = left, right

    while i < j:

        if reverse:
            # 从右到左找到首个大于基准数据的元素
            while i < j and nums[j] <= nums[left]:
                j -= 1
            # 从左到右找到首个小于基准数据的元素
            while i < j and nums[i] >= nums[left]:
                i += 1
        else:
            # 从右到左找到首个小于基准数据的元素
            while i < j and nums[j] >= nums[left]:
                j -= 1
            # 从左到右找到首个大于基准数据的元素
            while i < j and nums[i] <= nums[left]:
                i += 1
        # 元素交换
        nums[i], nums[j] = nums[j], nums[i]

    # 将基准数交换至两子数组的分界线
    nums[i], nums[left] = nums[left], nums[i]

    # 返回基准数的索引
    return i


if __name__ == '__main__':
    nums = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    print("sort before: ", nums)
    quick_sort(nums, 0, len(nums) - 1, False)
    print("sort after:", nums)
