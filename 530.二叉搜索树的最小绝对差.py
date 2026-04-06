'''
530. 二叉搜索树的最小绝对差
简单
给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
差值是一个正数，其数值等于两值之差的绝对值。
name:sanjin
date:2026.4.6
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.min_diff=float('inf')
        self.prev=None
    def traversal(self,root):
        if not root:
            return []
        self.traversal(root.left)
        if self.prev is not None:
            self.min_diff=min(self.min_diff,abs(root.val-self.prev.val))
        self.prev=root#更新一下prev节点的值
        self.traversal(root.right)
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #这个题跟98.验证二叉搜索树基本一样，只是在有序遍历的时候，要更新一下最小绝对差
        self.traversal(root)
        return self.min_diff

