'''

404. 左叶子之和
简单
给定二叉树的根节点 root ，返回所有左叶子之和。
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
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #左叶子节点的定义是：一个节点的左子树是一个叶子节点
        #可以用递归，递归的话需要用后序遍历的模版来写，因为我们需要先判断左子树和右子树的值，再对当前节点进行操作
        #所以我们可以用递归来判断每个节点的左子树是否是一个叶子节点，如果是就把它的值加到结果中，如果不是就继续递归判断它的左子树和右子树
        #当然在这里用迭代法也可以，迭代法的话就是用栈来实现，模版和前序遍历很像，只是加一个判断左子树是否是叶子节点的逻辑，下面是迭代法来实现
        if not root:
            return 0
        stack=[root]
        result=0
        while stack:
            node=stack.pop()
            if node.left and not node.left.left and not node.left.right:
                result+=node.left.val
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
