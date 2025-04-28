

'''选择排序'''


def selection_sort(nums):
    length = len(nums)
    if length <= 1:
        return
    for i in range(length):
        min_index = i
        for j in range(i, length):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]


if __name__ == '__main__':
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    print("sort before: ", array)
    selection_sort(array)
    print("sort after:", array)
