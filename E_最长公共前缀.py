"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

输入：strs = ["flower","flow","flight"]
输出："fl"

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

https://leetcode.cn/problems/longest-common-prefix/

"""


def longestCommonPrefix(strs):
    if not strs:
        return ""
    base = strs[0]
    for i in range(len(base)):
        for s in strs[1:]:
            # 依次判断 公共前缀是否相等; 横向对比
            if i >= len(s) or s[i] != base[i]:
                return base[:i]
    return base


if __name__ == '__main__':
    strs = ["flower", "flight", "flow", ]
    print(strs)
    print(longestCommonPrefix(strs))
