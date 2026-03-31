'''

110. 平衡二叉树
简单
给定一个二叉树，判断它是否是 平衡二叉树

name:sanjin
date:2026.3.31
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        #平衡二叉树的定义是：每个节点的左右子树的高度差不超过1
        #所以我们可以用递归来计算每个节点的高度，同时在计算高度的过程中判断是否满足平衡二叉树的条件，如果不满足就返回-1，最后判断返回值是否为-1即可
        def dfs(node):
            if not node:
                return 0
            left_depth=dfs(node.left)
            if left_depth==-1:
                return -1
            right_depth=dfs(node.right)
            if right_depth==-1:
                return -1
            if abs(left_depth-right_depth)>1:
                return -1
            return max(left_depth,right_depth)+1#这里+1是因为要算上当前节点的高度，所以要在左右子树的高度基础上加1
        return dfs(root)!=-1