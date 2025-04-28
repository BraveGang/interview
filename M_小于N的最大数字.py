"""
Tiktok: 递归 + 回溯 + 减枝

小于N的最大数字

给定一个数 n,如 23121; 给定一组数字 A 如 {2,4,9},
求由 A 中元素组成的、小于 n 的最大数，如小于 23121 的最大数为 22999

"""

"""
回溯+剪枝
"""


def max_number_less_than_n(n, A):

    n_str = str(n)
    A = sorted(A, reverse=True)
    result = []

    def backtrack(index, is_tight, path):
        if index == len(n_str):
            return int(''.join(path))

        limit = int(n_str[index]) if is_tight else 9
        for d in A:
            if d > limit:
                continue
            path.append(str(d))
            res = backtrack(index + 1, is_tight and (d == limit), path)
            if res is not None:
                return res
            path.pop()

        return None

    result = backtrack(0, True, [])

    # 处理特殊情况，如无法构造相同位数的数字
    if result is None:
        if len(n_str) == 1:
            return None
        # 构造少一位的最大数
        return int(''.join([str(max(A))] * (len(n_str) - 1)))

    return result


'''
迭代+贪心算法
'''


def max_number_less_than_n2(n, A):
    n_str = str(n)
    A = sorted(A)
    result = []

    for i in range(len(n_str)):
        # 尝试找到等于或小于当前位的最大数字
        found = False
        for d in reversed(A):
            if int(n_str[i]) > d:
                result.append(str(d))
                found = True
                break
            elif int(n_str[i]) == d:
                result.append(str(d))
                found = True
                break

        if not found:
            # 当前位没有可选数字，需要回溯
            for j in range(i-1, -1, -1):
                # 尝试减小前一位
                for d in reversed(A):
                    if d < int(result[j]):
                        result[j] = str(d)
                        # 后面所有位填充最大值
                        return int(''.join(result) + str(max(A)) * (len(n_str)-j-1))
            # 如果第一位就无法满足，返回少一位的最大数
            return int(str(max(A)) * (len(n_str)-1)) if len(n_str) > 1 else None

        # 检查是否已经小于n的前i+1位
        if ''.join(result) < n_str[:i+1]:
            # 后面所有位填充最大值
            return int(''.join(result) + str(max(A)) * (len(n_str)-i-1))

    # 如果完全相等，需要减小最后一位
    for d in reversed(A):
        if d < int(result[-1]):
            result[-1] = str(d)
            return int(''.join(result))

    # 如果最后一位无法减小，需要回溯
    for j in range(len(result)-2, -1, -1):
        for d in reversed(A):
            if d < int(result[j]):
                result[j] = str(d)
                return int(''.join(result) + str(max(A)) * (len(n_str)-j-1))

    return int(str(max(A)) * (len(n_str)-1)) if len(n_str) > 1 else None


if __name__ == '__main__':
    n = 23121
    A = {2, 4, 9}
    print(max_number_less_than_n(n, A))
    print(max_number_less_than_n2(n, A))
