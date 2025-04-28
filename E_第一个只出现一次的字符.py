"""

美团二面: 考察 哈希表 对数组的计数

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s只包含小写字母。

输入：s = "abaccdeff"
输出：'b'

输入：s = ""
输出：' '

https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/

"""


def first_uniq_char(s: str):
    
    # 哈希表辅助方法
    char_count = dict()
    
    # 遍历字符,对出现的频次进行计数
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # 找到第一个出现次数为 1 的字符
    for char in s:
        if char_count[char] == 1:
            return char

    # 如果没有符合条件的字符，返回单空格
    return ' '


if __name__ == '__main__':
    s = "abaccdeff"
    print(first_uniq_char(s))
