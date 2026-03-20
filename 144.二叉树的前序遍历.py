'''

144. 二叉树的前序遍历
简单
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

name:sanjin
date:2026-3-20
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        #前序遍历：跟节点->左子树->右子树
        #第一种，递归法
        result=[]
        def dfs(node):
            if not node:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return result
    #第二种，迭代法
    def preorderTraversal_iterration(self, root):
        if not root:
            return []
        result=[]
        stack=[root]#先把一开始的根节点放入栈中
        while stack:
            node=stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

