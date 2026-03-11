'''
54. 替换数字（第八期模拟笔试）
题目描述
给定一个字符串 s，它包含小写字母和数字字符，请编写一个函数，将字符串中的字母字符保持不变，而将每个数字字符替换为number。 例如，对于输入字符串 "a1b2c3"，函数应该将其转换为 "anumberbnumbercnumber"。
输入描述
输入一个字符串 s,s 仅包含小写字母和数字字符。
输出描述
打印一个新的字符串，其中每个数字字符都被替换为了number
输入示例
a1b2c3
输出示例
anumberbnumbercnumber
提示信息
数据范围：
1 <= s.length < 10000。

name:sanjin
date:2026-3-11
'''
#很多数组填充类问题，做法都是：先预先给数组扩容带填充后的大小，然后在从后向前进行操作。
class Solution(object):
    def subsitute_numbers(self, s):
        """
        :type s: str
        :rtype: str
        """
        sum=0
        for char in s:
            if char.isdigit():
                sum+=1
        expand_len=len(s)+sum*5
        result=['']*expand_len

        new_index=expand_len-1
        old_index=len(s)-1

        while old_index >= 0:
            if s[old_index].isdigit():
                result[new_index-5:new_index+1]="number"
                new_index-=6
            else:
                result[new_index]=s[old_index]
                new_index-=1
            old_index-=1
        return ''.join(result)

if __name__ == "__main__":
    solution = Solution()

    while True:
        try:
            s = input()
            result = solution.subsitute_numbers(s)
            print(result)
        except EOFError:
            break