'''
383. 赎金信
简单
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。如果可以，返回 true ；否则返回 false 。
magazine 中的每个字符只能在 ransomNote 中使用一次。
示例 1：
输入：ransomNote = "a", magazine = "b"
输出：false
示例 2：
输入：ransomNote = "aa", magazine = "aab"
输出：true

name:sanjin
date:2026-3-11
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #本题经典思路就是用哈希法，统计字符出现次数，满足ransomNote中每个字符出现的次数都不大于magazine中对应字符出现的次数即可
        ransom_count=[0]*26
        magazine_count=[0]*26
        for char in ransomNote:
            ransom_count[ord(char)-ord('a')]+=1
        for char in magazine:
            magazine_count[ord(char)-ord('a')]+=1
        for i in range(26):
            if ransom_count[i] > magazine_count[i]:
                return False
        return True