'''
541. 反转字符串 II
简单

给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。
如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

示例 1：
输入：s = "abcdefg", k = 2
输出："bacdfeg"
示例 2：
输入：s = "abcd", k = 2
输出："bacd"

name:sanjin
date:2026-3-11
'''
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        #跟344.反转字符串相比，其实就是多了一个跨度2k里k个反转
        #所以只需要先写好一个反转函数，然后实在主函数里面每次跨度2k，然后反转该区间的前k个字符
        def reverse(chars):

            left,right=0,len(chars)-1
            while left < right:
                chars[left],chars[right]=chars[right],chars[left]
                left+=1
                right-=1
            return chars

        result=list(s)#字符串不可变，所以需要转换成列表
        for i in range(0,len(s),2*k):
            result[i:i+k]=reverse(result[i:i+k])
        return ''.join(result)
