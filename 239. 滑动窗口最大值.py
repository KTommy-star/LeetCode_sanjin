'''

239. 滑动窗口最大值
困难

给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回 滑动窗口中的最大值 。

示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
示例 2：
输入：nums = [1], k = 1
输出：[1]
name:sanjin
date:2026.3.16
'''
from collections import deque
def update_kept_nums(kept_nums,num):
    while kept_nums and num > kept_nums[-1]:
        kept_nums.pop()
    kept_nums.append(num)
class Solution(object):

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #单调递减队列的思路是：队列中只保留当前窗口可能成为窗口最大值的元素，且队列头部永远是当前窗口的最大值，时间复杂度可优化到 O (n)
        max_list=[]
        kept_nums=deque() # 单调递减队列，存的是nums的元素值
        for i in range(len(nums)):
            #维护单调递减队列，移除队列中比当前元素小的数
            update_kept_nums(kept_nums,nums[i])
            #左侧旧元素如果等于单调队列头元素，就需要移除头元素
            if i >= k and nums[i-k] == kept_nums[0]:#i>=k表示窗口至少滑动过一次，nums[i-k]表示刚刚从左边离开窗口的那个元素；如果离开的匀速恰好是队列头部最大值，说明这个最大值已经不在当前窗口，需要从队列移除
                kept_nums.popleft()
            if i >= k-1:
                max_list.append(kept_nums[0])#i>=k-1表示窗口已经形成，就从队列里面加上这个窗口的元素最大值，队列里面是单调递减队列，所以kept_nums[0]表示的是最大值
        return max_list