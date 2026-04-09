'''

235. 二叉搜索树的最近公共祖先
中等
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

name:sanjin
date:2026.4.9
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traversal(self,root,p,q):
        if not root:
            return root
        if root.val >p.val and root.val >q.val:#此时太大了，需要想左递归
            left=self.traversal(root.left,p,q)
            if left:
                return left
        if root.val<p.val and root.val<q.val:
            right=self.traversal(root.right,p,q)
            if right:
                return right
        return root#如果不满足上面两种情况，说明root.val在[p,q]之间了，那么就说明root就是pq的最近公共祖先了，直接返回root就可以了
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #由于二叉搜索树咋有序性，所以经过推导，我们只需要在遍历的时候，
        #判断root和左右子节点的值的大小，如果又出现在[p,q]之内，那就说明就是最近公共祖先了，其他情况需要考虑向左或者向右递归
        #由于只是判断值的大小，中间节点没有特殊的；逻辑，所以前中后序遍历顺序无所谓
        return self.traversal(root,p,q)