"""

字节-云视频二面:

调整数组顺序使奇数位于偶数前面,其中奇数部分降序排列,偶数部分升序排列 (进阶: 且空间复杂度最优)

输入: nums = [1, 2, 3, 4, 7, 5, 8]
输出: [7, 5, 3, 1, 2, 4, 8]


解法:
1. 通过位运算进行奇数和偶数进行调整
2. 数组内进行排序(不新增空间开销)

"""


'''双指针 + 位运算 + 快速排序'''


def exchange(num):
    left, right = 0, len(num) - 1
    while left < right:
        # 位运算
        while left < right and num[left] & 1 == 1:  # 奇数
            left += 1
        while left < right and num[right] & 1 == 0:  # 偶数
            right -= 1
        num[left], num[right] = num[right], num[left]

    quick_sort(num, 0, left - 1, reverse=True)
    quick_sort(num, left, len(num) - 1, reverse=False)

    return num


def quick_sort(nums, left, right, reverse=False):

    # 递归终止条件
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
    nums = [1, 2, 3, 4, 7, 5, 8]
    print(nums)
    print(exchange(nums))
