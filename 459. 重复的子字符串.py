'''

459. 重复的子字符串
简单

给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。
示例 1:
输入: s = "abab"
输出: true
解释: 可由子串 "ab" 重复两次构成。
示例 2:
输入: s = "aba"
输出: false
示例 3:
输入: s = "abcabcabcabc"
输出: true
解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)

提示：
1 <= s.length <= 104
s 由小写英文字母组成

name:sanjin
date:2026-3-14

'''


class Solution(object):
    def get_next(self,next,s):
        next[0]=-1
        j=-1
        for i in range(1,len(s)):
            while j >= 0 and s[i] != s[j+1]:
                j=next[j]
            if s[i] == s[j+1]:
                j+=1
            next[i]=j
        return next
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
    #这道题可以通过拼接两个s，来判断拼接过后的s，是否还出现一个s，如果有的话，就可以说明s是由重复子串构成的
    #在一个串中查找是否出现另一个串，就是KMP算法的领地
    #如果字符串 s 由重复子串构成，那么：最小重复子串长度 = 原字符串长度 - 最长相等前后缀长度
        if len(s) == 0:
            return False
        next=[0]*len(s)
        self.get_next(next,s)
        if next[-1] != -1 and len(s) % (len(s)-(next[-1] + 1)) == 0:
            #next[-1]是最长相等先后缀长度-1，+1就是最长相等前后缀长度，len(S)减去其，就变成了最小重复子串长度
            #然后如果整体的长度能整除这个最小重复子串长度，就说嘛s可以由重复子串构成
            return True
        return False
