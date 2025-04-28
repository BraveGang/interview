'''二分查找: 遍历实现'''


def binary_search(nums, target):

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (high + low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


'''二分查找: 递归实现'''


def dfs(nums, target, i, j):

    # 若区间为空，代表无目标元素，则返回 -1
    if i > j:
        return -1

    # 计算中点索引 m
    m = (i + j) // 2

    if nums[m] < target:
        # 递归子问题 f(m+1, j)
        return dfs(nums, target, m + 1, j)
    elif nums[m] > target:
        # 递归子问题 f(i, m-1)
        return dfs(nums, target, i, m - 1)
    else:
        # 找到目标元素，返回其索引
        return m


def binary_recursion_search(nums, target):
    length = len(nums)
    # 求解问题 f(0, n-1)
    return dfs(nums, target, 0, length - 1)


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 注意 这里需要的是有序数组
    print(binary_search(array, 7))
    print(binary_recursion_search(array, 7))
