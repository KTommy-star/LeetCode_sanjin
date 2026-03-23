'''

145. 二叉树的后序遍历
简单
给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。

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
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        #后序遍历：左子树->右子树->根节点
        #第一种，递归法
        result=[]
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)
        dfs(root)
        return result
    #第二种，迭代法
    def postorderTraversal_iteration(self, root):
        if not root:
            return []
        result=[]
        stack=[root]
        while stack:
            node=stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]#后序遍历的结果是根节点在最后，所以需要反转一下

    def postorderTraversal_unified(self, root):
        result=[]
        st=[]
        if root:
            st.append(root)
        while st:
            node=st.pop()
            if node != None:
                st.append(node)
                st.append(None)
                if node.right:
                    st.append(node.right)
                if node.left:
                    st.append(node.left)
            else:
                node=st.pop()
                result.append(node.val)
        return result