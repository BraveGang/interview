"""
全排列_字符串:

输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

https://leetcode.cn/problems/zi-fu-chuan-de-pai-lie-lcof/

"""

from typing import List

'''

方法思路
排序字符数组：首先将输入的字符串转换为字符数组并排序。排序的目的是为了方便后续剪枝处理重复字符。
回溯算法：使用回溯算法来生成所有可能的排列。在每一步中，选择一个未被使用的字符添加到当前路径中，并递归地继续选择下一个字符。
剪枝处理重复：在递归过程中，如果当前字符与前一个字符相同，并且前一个字符未被使用，则跳过当前字符。这样可以避免生成重复的排列。

代码解释
排序字符数组：chars = sorted(s)将输入字符串转换为排序后的字符数组，以便后续剪枝处理。
回溯函数：backtrack函数递归地构建所有可能的排列。path参数记录当前路径的字符。
终止条件：当路径长度等于原字符串长度时，将路径转换为字符串并加入结果列表。
循环处理每个字符：遍历每个字符，跳过已使用的字符。通过检查当前字符与前一个字符是否相同且前一个字符未被使用来剪枝，避免重复排列。
回溯过程：标记当前字符为已使用，递归调用后恢复状态，继续尝试其他字符。

'''

class Solution:

    def permutation(self, s: str) -> List[str]:
        chars = sorted(s)
        res = []
        used = [False] * len(chars)

        def backtrack(path):
            if len(path) == len(chars):
                res.append(''.join(path))
                return
            for i in range(len(chars)):
                # 减枝判断
                if used[i]:
                    continue
                # 避免重复排列
                if i > 0 and chars[i] == chars[i-1] and not used[i-1]:
                    continue
                used[i] = True
                path.append(chars[i])
                # 递归调用
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return res


if __name__ == '__main__':
    print(Solution().permutation("abcd"))
