"""

字节-飞书-二面:

给你一个字符串 s, 找到s中最长的回文子串。
如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

输入：s = "cbbd"
输出："bb"


1. 回文串的长度可能是奇数或偶数。对于奇数长度的回文串，中心是一个字符；对于偶数长度的回文串，中心是两个字符。

2. 我们可以遍历字符串中的每一个字符，将其作为中心，向左右扩展，找到最长的回文子串。

3. 同时，我们也要考虑偶数长度的回文串，即以两个字符为中心的情况。


"""

'''中心扩展算法'''


def longestPalindrome(s):

    if not s:
        return ""

    def expand_around_center(left, right):
        # 从中心向左右扩展，找到最长的回文子串
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 返回当前找到的回文子串,列表切片-> 左闭右开
        return s[left + 1:right]

    # 初始化最长回文子串为空
    longest = ""

    for i in range(len(s)):
        # 奇数长度的回文子串
        odd = expand_around_center(i, i)
        # 偶数长度的回文子串
        even = expand_around_center(i, i + 1)
        # 更新最长的回文子串
        longest = max(longest, odd, even, key=len)

    return longest


'''中心扩展算法 --> 计算长度和小标, 最后进行截取返回'''


def longestPalindrome2(s):

    if not s:
        return ""

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # 返回 回文长度

    start = 0
    max_len = 0
    n = len(s)

    for i in range(n):
        odd = expand(i, i)  # 奇数长度的回文
        even = expand(i, i + 1)  # 偶数长度的回文
        curr_len = max(odd, even)

        if curr_len > max_len:
            max_len = curr_len
            start = i - (curr_len - 1) // 2  # 计算起始位置

    return s[start:start + max_len]


if __name__ == '__main__':
    s = "babad"
    print(longestPalindrome(s))
    print(longestPalindrome2(s))
