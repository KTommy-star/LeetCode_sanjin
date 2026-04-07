'''

236. 二叉树的最近公共祖先
中等
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
name:sanjin
date:2026.4.7
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #首先想到的思路肯定是自底向上查看，就找p和q的最近祖先。
        #那这样就能想到需要回溯（自底向上），后序遍历的左右中结构就适合这个问题，因为对于一个根节点，我们先遍历左右，把p和q取出来，如果左右都取到了，说明该根节点就是pq的最近祖先
        if not root or root==p or root==q:
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root
        elif left is not None and right is None:
            return left
        else:
            return right
