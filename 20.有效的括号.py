'''

20. 有效的括号
简单
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。

name:sanjin
date:2026-3-15
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #符号匹配问题就是经典的用栈和字典来做
        #用字典建立好一一对应的关系，然后用栈来存储左括号，当遇到右括号，就从栈顶弹出一个
        #如果弹出的不是和右括号对应的左括号，就说明不匹配，直接返回false，如果最后栈不为空，也说明不匹配，返回false
        stack=[]
        mapping={'(':')','{':'}','[':']'}
        for char in s:
            if char in mapping:
                stack.append(char)
            else:
                if not stack:
                    return False
                top=stack.pop()
                if mapping[top] != char:
                    return False
        return not stack#如果最后栈为空，说明就完全匹配上了