"""

小米一面: 考察辅助栈的实现

给定一个只包括 '(',')','{','}','[',']' 的字符串s, 判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合
左括号必须以正确的顺序闭合
每个右括号都有一个对应的相同类型的左括号

https://leetcode.cn/problems/valid-parentheses/

"""

'''辅助栈思想'''


def isValid(str):

    if len(str) % 2 == 1:
        return False

    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []

    for ch in str:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)

    return not stack


if __name__ == '__main__':
    _str = '{[]}))[]'
    print(isValid(_str))
