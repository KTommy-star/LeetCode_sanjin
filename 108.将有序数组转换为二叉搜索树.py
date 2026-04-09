'''
108. 将有序数组转换为二叉搜索树
简单
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。
name:sanjin
date:2026.4.9
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        #本题重点在于找到中间点，来作为根节点，然后左右递归来构成树
        def traversal(left,right):
            if left > right:
                return None
            mid=(left+right)//2
            root=TreeNode(nums[mid])
            root.left=traversal(left,mid-1)
            root.right=traversal(mid+1,right)
            return root
        return traversal(0,len(nums)-1)
