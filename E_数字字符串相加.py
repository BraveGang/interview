"""

滴滴一面: 考察字符串和数字转换, 以及对进位的处理, 计算器原理

求两个数字字符串相加的和:

给定两个字符串形式的非负整数num1 和 num2，计算它们的和并同样以字符串形式返回。
你不能使用任何內建的用于处理大整数的库（比如 BigInteger），
也不能直接将输入的字符串转换为整数形式。

输入：num1 = "11", num2 = "123"
输出："134"

输入：num1 = "456", num2 = "77"
输出："533"

输入：num1 = "0", num2 = "0"
输出："0"

https://leetcode.cn/problems/add-strings/

"""


'''指针相加'''


def addStrings(num1, num2):
    res = ""
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0

    while i >= 0 or j >= 0:
        x = int(num1[i]) if i >= 0 else 0
        y = int(num2[j]) if j >= 0 else 0
        sum_x_y = x + y + carry
        carry = sum_x_y // 10
        res = str(sum_x_y % 10) + res
        i -= 1
        j -= 1

    return str(carry) + res if carry else res


if __name__ == '__main__':
    str1 = '4444444'
    str2 = '77778'
    print(addStrings(str1, str2))
