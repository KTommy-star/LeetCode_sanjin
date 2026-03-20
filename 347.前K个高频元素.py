'''

347. 前 K 个高频元素
中等

给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
示例 1：
输入：nums = [1,1,1,2,2,3], k = 2
输出：[1,2]
示例 2：
输入：nums = [1], k = 1
输出：[1]
示例 3：
输入：nums = [1,2,1,2,1,2,3,1,3,2], k = 2
输出：[1,2]

name:sanjin
date:2026-3-19
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #本题的思路是：先统计每个元素出现的频率，然后根据频率进行排序，最后返回前k个元素
        #统计频率的时候，先用字典来统计每个元素的频率，然后用一个新的字典，以频率为键，元素列表为值，来统计每个频率对应的元素列表，最后根据频率进行排序，返回前k个元素
        times_dict={}
        for num in nums:
            times_dict[num]=times_dict.get(num,0)+1
        freq_dict={}
        for num,times in times_dict.items():
            if times not in freq_dict:
                freq_dict[times]=[num]
            else:
                freq_dict[times].append(num)
        key = list(freq_dict.keys())
        key.sort(reverse=True)
        result=[]
        count=0
        while key and count < k:
            result+=(freq_dict[key[0]])#这里直接把这个频率对应的元素列表加到结果列表中，因为可能有多个元素出现了同样的频率，所以需要把这个频率对应的元素列表全部加到结果列表中，
            # 但是不能用.append()，因为append只能添加一个元素，而这里需要添加一个列表，所以需要用+=来添加这个列表中的所有元素
            count+=len(freq_dict[key[0]])
            key.pop(0)
        return result[0:k]#因为可能最后一次添加的元素超过了k，所以需要切片一下