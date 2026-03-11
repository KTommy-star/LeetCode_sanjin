'''
344. 反转字符串
简单

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
示例1：
输入：s = ["h", "e", "l", "l", "o"]
输出：["o", "l", "l", "e", "h"]
示例2：
输入：s = ["H", "a", "n", "n", "a", "h"]
输出：["h", "a", "n", "n", "a", "H"]

name:sanjin
date:2026-3-11
'''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #交换字符串的字符，本质上跟聊表有区别，比链表简单。
        #其实就是交换对应位置首尾的字符，一直到中间位置为止
        #本题用双指针法，左右一次交换，然后收拢到中间
        left=0
        right=len(s)-1
        while left < right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1

