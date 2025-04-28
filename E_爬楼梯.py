"""
给定一个共有 𝑛 阶的楼梯，你每步可以上 1 阶或者 2 阶，请问有多少种方案可以爬到楼顶?
"""


'''爬楼梯:空间优化后的动态规划'''


def climbing_stairs_dp_comp(n):

    if n == 1 or n == 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    print(climbing_stairs_dp_comp(9))
