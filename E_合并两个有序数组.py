"""

小红书: 考察排序 或 双指针

给你两个按 非递减顺序 排列的整数数组nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中
为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6]
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。合并结果是 [1]

输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。合并结果是 [1]
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中

https://leetcode.cn/problems/merge-sorted-array/


为了合并两个已排序的非递减数组 nums1 和 nums2，我们可以利用双指针从后向前合并，以避免覆盖 nums1 中未处理的元素。具体步骤如下：
- 初始化指针：设置三个指针 p1（指向 nums1 的最后一个有效元素）、p2（指向 nums2 的最后一个元素）和 p（指向 nums1 的末尾）。
- 从后向前比较：每次将较大的元素放入 p 指向的位置，并移动相应的指针。
- 处理剩余元素：若 nums2 还有剩余元素，直接复制到 nums1 的前面。

"""

'''双指针法'''


def merge_two_array(nums1, m, nums2, n):

    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # 处理 nums2 剩余元素（若 p2 >= 0）
    # 无需处理 nums1 剩余，因为它们已在正确位置
    nums1[:p2 + 1] = nums2[:p2 + 1]


''' 切片拼接,再排序'''


def merge_two_array2(nums1, m, nums2, n):
    # 数组切片赋值
    nums1[m:] = nums2
    nums1.sort()


''' 这类写法更具备兼容性,但是会临时申请存储空间'''


def merge_two_array3(nums1, m, nums2, n):

    tmp = []
    p1, p2 = 0, 0

    while p1 < m or p2 < n:
        if p1 == m:
            tmp.append(nums2[p2])
            p2 += 1
        elif p2 == n:
            tmp.append(nums1[p1])
            p1 += 1
        elif nums1[p1] < nums2[p2]:
            tmp.append(nums1[p1])
            p1 += 1
        else:
            tmp.append(nums2[p2])
            p2 += 1

    nums1[:] = tmp


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m, n = 3, 3
    merge_two_array(nums1, m, nums2, n)
    # merge_two_array2(nums1, m, nums2, n)
    # merge_two_array3(nums1, m, nums2, n)
    print(nums1)
