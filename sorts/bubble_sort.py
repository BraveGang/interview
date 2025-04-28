'''冒泡排序'''


def bubble_sort(nums):
    length = len(nums)

    if length <= 1:
        return

    for i in range(length):
        flag = False
        for j in range(length - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True

        if not flag:
            break


'''冒泡排序'''


def bubble_sort2(nums):
    length = len(nums)
    if length <= 1:
        return
    for i in range(length):
        for j in range(i + 1, length):
            if nums[j] < nums[i]:
                nums[j], nums[i] = nums[i], nums[j]


if __name__ == '__main__':
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    print("sort before: ", array)
    bubble_sort2(array)
    print("sort after: ", array)
