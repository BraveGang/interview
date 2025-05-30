"""
桶排序

桶排序(Bucket Sort)，也叫箱排序，其主要思想是：将待排序集合中处于同一个值域的元素存入同一个桶中，也就是根据元素值特性将集合拆分为多个区域，则拆分后形成的多个桶，从值域上看是处于有序状态的。对每个桶中元素进行排序，则所有桶中元素构成的集合是已排序的。
桶排序是计数排序的扩展版本，计数排序可以看成每个桶只存储相同元素，而桶排序每个桶存储一定范围的元素。桶排序需要尽量保证元素分散均匀，否则当所有数据集中在同一个桶中时，桶排序失效。

1.根据待排序集合中最大元素和最小元素的差值范围和映射规则，确定申请的桶个数；
2.遍历排序序列，将每个元素放到对应的桶里去；
3.对不是空的桶进行排序；
4.按顺序访问桶，将桶中的元素依次放回到原序列中对应的位置，完成排序。
"""
from typing import List


def bucket_sort(nums: List[int]):
    
    min_num = min(nums)
    max_num = max(nums)
    # 桶的大小
    bucket_range = (max_num - min_num) / len(nums)
    # 桶数组
    count_list = [[] for i in range(len(nums) + 1)]
    # 向桶数组填数
    for i in nums:
        count_list[int((i - min_num) // bucket_range)].append(i)
    nums.clear()

    # 回填，这里桶内部排序直接调用了sorted
    for i in count_list:
        for j in sorted(i):
            nums.append(j)


if __name__ == '__main__':
    import random

    random.seed(54)
    arr = [random.randint(0, 100) for _ in range(10)]
    print("原始数据：", arr)
    bucket_sort(arr)
    print("桶排序结果：", arr)
