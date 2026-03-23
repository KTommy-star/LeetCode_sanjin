'''

94. 二叉树的中序遍历
简单
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

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
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        #中序遍历：左子树->根节点->右子树
        #第一种，递归法
        result=[]
        def dfs(node):
            if not node:
                dfs(node.left)
                result.append(node.val)
                dfs(node.right)
        dfs(root)
        return result
    #第二种，迭代法
    def inorderTraversa_iteration(self, root):
        if not root:
            return []
        result=[]
        stack=[]
        current=root#从根节点开始遍历，在中序遍历，需要用一个current指针来遍历树的节点
        #整个的迭代过程是先访问最底层的左子树节点，然后处理栈顶节点，最后访问右子树节点
        while current or stack:
            if current:
                # 先迭代访问最底层的左子树节点
                stack.append(current)
                current=current.left
            # 到达最左节点后处理栈顶节点
            else:
                current=stack.pop()
                result.append(current.val)
                current=current.right
        return result

    def inorderTraversal_unified(self, root):
        result=[]
        st=[]
        if root:
            st.append(root)
        while st:
            node=st.pop()
            if node != None:
                if node.right:
                    st.append(node.right)
                st.append(node)
                st.append(None)
                if node.left:
                    st.append(node.left)
            else:
                node=st.pop()
                result.append(node.val)
        return result