'''
28. 找出字符串中第一个匹配项的下标
简单
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
如果 needle 不是 haystack 的一部分，则返回  -1 。
示例 1：
输入：haystack = "sadbutsad", needle = "sad"
输出：0
解释："sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。
示例 2：
输入：haystack = "leetcode", needle = "leeto"
输出：-1
解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。

name:sanjin
date:2026-3-13
'''
class Solution(object):
    def build_next(self,next,s):
        #构建next数组，也就是前缀表
        #next数组的每个位置记录了该位置之前的字符串的最长相同前后缀的长度
        next[0]=-1#初始化第一个位置
        j=-1#前缀指针初始值
        for i in range(1,len(s)): # 从i=1开始遍历（i=0已经初始化），i是后缀指针，j是前缀指针
            while j >= 0 and s[i] != s[j+1]:
                j=next[j]#利用已经计算的next数组，当出现不匹配时，跳转到前一个最长相同前后缀的位置继续比较
            if s[i] == s[j+1]:#如果当前字符与前缀指针指向的字符匹配，则前缀指针向前移动一位，表示长度加一
                j+=1
            next[i]=j#记录当前i位置的最长相同前后缀长度
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #本题用到了KMP算法
        #KMP的主要思想就是当出现字符串不匹配的时候，可以知道一部分之前已经匹配的内容，可以利用这些信息避免从头去做匹配
        '''
        最长相同前后缀（也叫最长相等前后缀 / 最长真前后缀），指的是一个字符串中不包含自身的前缀和不包含自身的后缀完全匹配时的最大长度。简单来说：
            前缀：从字符串开头开始的子串（不能是字符串本身），比如 "abcab" 的前缀有 "a"、"ab"、"abc"、"abca"；
            后缀：从字符串末尾结束的子串（不能是字符串本身），比如 "abcab" 的后缀有 "b"、"ab"、"cab"、"bcab"；
            最长相同前后缀就是两者中完全匹配的最长子串长度。在上面的例子中，ab就是最长相同前后缀，长度为2。
        '''
        #前缀表就是记录了每个字符位置的最长相同前后缀的长度
        #在本题中用到的next数组，就是前缀表的基础上，每一个数值减一，这样当文本串指针i和模式串指针j不匹配时，就可以直接跳转到next[j]的位置继续比较，而不需要回退文本串指针i，这也是一种方便的做法
        #整体做法如下，在代码中有所批注
        if not needle:
            return 0
        next=[0]*len(needle)
        self.build_next(next,needle)#构建前缀表
        j=-1#模式串指针初始值
        for i in range(len(haystack)):
            while j >= 0 and haystack[i] != needle[j+1]:#当文本串指针i和模式串指针j不匹配时，利用前缀表跳转模式串指针j到next[j]的位置继续比较，这也是KMP的核心
                j=next[j]
            if haystack[i] == needle[j+1]:
                j+=1#如果当前字符匹配，则模式串指针向前移动一位，表示已经匹配了一个字符
            if j == len(needle)-1:#如果模式串指针已经到达模式串的末尾，说明已经完全匹配了模式串
                return i-len(needle)+1
        return -1

