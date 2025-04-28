"""
计数排序

1、找出待排序的数组中最大和最小的元素
2、统计数组中每个值为i的元素出现的次数，存入数组C的第i项
3、对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）
4、反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1
"""

from typing import List


def counting_sort(nums: List[int]):
    length = len(nums)
    if length <= 1:
        return
    # a中有counts[i]个数不大于i
    counts = [0] * (max(nums) + 1)
    for num in nums:
        counts[num] += 1
    # counts = list(itertools.accumulate(counts))
    for i in range(1, length):  # 计算每一位数字下标位置
        counts[i] = counts[i] + counts[i - 1]
    # 临时数组，储存排序之后的结果
    a_sorted = [0] * length
    for num in reversed(nums):  # 反向填充保障数据稳定性
        index = counts[num] - 1
        a_sorted[index] = num
        counts[num] -= 1
    nums[:] = a_sorted


if __name__ == "__main__":

    array = [4, 5, 0, 9, 3, 3, 1, 9, 8, 7]
    print("sort before: ", array)
    counting_sort(array)
    print("sort after: ", array)
