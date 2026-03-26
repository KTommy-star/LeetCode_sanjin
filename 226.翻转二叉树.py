'''

226. 翻转二叉树
简单
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

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
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        #用递归法最简单最好写，注意，本题用前序遍历和后续遍历都可以，但是不能用中序遍历
        if not root:
            return None
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    #当然也可以使用迭代法，迭代法就是利用栈
    def invertTree_iteration(self,root):
        if not root:
            return None
        #下面的模版和层序遍历很像，只是把队列换成了栈，先进后出
        #下面写的是用迭代的前序遍历来实现翻转二叉树
        stack=[root]
        while stack:
            node=stack.pop()
            node.left,node.right=node.right,node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root