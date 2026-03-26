'''
101. 对称二叉树
简单
给你一个二叉树的根节点 root ， 检查它是否轴对称

name:sanjin
date:2026.3.26
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        #要判断是不是对称二叉树，其实核心逻辑就是翻转过后不变
        #此题用递归解非常方便，写一个dfs函数，然后写下True和False的边界条件，再对内万仓的判断调用dfs递归就可以了
        def dfs(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            outside=dfs(left.left, right.right)
            inside=dfs(left.right,right.left)
            return outside and inside
        return dfs(root.left,root.right)
