'''
151. 反转字符串中的单词
中等
相关标签
premium lock icon
相关企业
给你一个字符串 s ，请你反转字符串中 单词 的顺序。
单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。
注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

示例 1：
输入：s = "the sky is blue"
输出："blue is sky the"
示例 2：
输入：s = "  hello world  "
输出："world hello"
解释：反转后的字符串中不能存在前导空格和尾随空格。
示例 3：
输入：s = "a good   example"
输出："example good a"
解释：如果两个单词间有多余的空格，反转后的字符串需要将单词间的空格减少到仅有一个。

name:sanjin
date:2026-3-12
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #此题这里用到split函数，已经将单词的空格去掉，然后分为了一个一个的单词列表
        #这样就可以对这个列表进行收尾交换，也就达到了单词的首尾交换操作
        words=s.split()
        left,right=0,len(words)-1
        while left < right:
            words[left],words[right]=words[right],words[left]
            left+=1
            right-=1
        return ' '.join(words)