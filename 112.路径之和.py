'''
112. 路径总和
简单
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。
判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。
叶子节点 是指没有子节点的节点。
name:sanjin
date:2026.4.2
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        #本题的核心逻辑就是：从根节点到叶子节点的路径上所有节点值相加等于目标和 targetSum
        #所以我们可以用递归来实现，递归的话需要用前序遍历的模版来写，因为我们需要先对当前节点进行操作，再判断左子树和右子树的值
        #所以我们可以用递归来判断每个节点的值是否等于目标和，如果等于就返回true，如果不等于就继续递归判断它的左子树和右子树，直到遍历到叶子节点为止
        if not root:
            return False
        if not root.left and not root.right and root.val==targetSum:
            return True
        targetSum-=root.val
        #以上是递归的核心逻辑，就是利用递减来逐渐逼近targetSum
        left=self.hasPathSum(root.left,targetSum)
        right=self.hasPathSum(root.right,targetSum)
        return left or right