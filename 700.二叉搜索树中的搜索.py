'''

700. 二叉搜索树中的搜索
简单
给定二叉搜索树（BST）的根节点 root 和一个整数值 val。
你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 null 。

name:sanjin
date:2026.4.5
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        #二叉搜索树的定义是：对于每一个节点，左子树的值都比他小，右子树的值都比他大
        #由于这个有序性质，我们就可以通过判定大小，类似于二分查找的思路，来看是要递归左子树还是右子树，直到找到目标节点或者遍历到空节点为止
        #题目中说的返回相应节点为根的子树，其实就是返回这个节点本身，在这里不要被迷惑了
        if not root:
            return None
        if root.val==val:
            return root
        if root.val>val:
            return self.searchBST(root.left,val)
        if root.val<val:
            return self.searchBST(root.right,val)
