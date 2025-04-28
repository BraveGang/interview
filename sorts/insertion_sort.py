"""
插入排序
"""
from typing import List


def insertion_sort(nums: List[int]):
    
    # 外循环:已排序区间为 [0, i-1]
    for i in range(1, len(nums)):
        base = nums[i]
        j = i - 1
        # 内循环:将 base 插入到已排序区间 [0, i-1] 中的正确位置
        while j >= 0 and nums[j] > base:
            # 将 nums[j] 向右移动一位
            nums[j + 1] = nums[j]
            j -= 1
        # 将 base 赋值到正确位置
        nums[j + 1] = base


if __name__ == '__main__':
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    print("sort before: ", array)
    insertion_sort(array)
    print("sort after:", array)
