'''

107. 二叉树的层序遍历 II
中等
给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
name:sanjin
date:2026-3-23
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        #这个题其实就是相比102题，在最后一步，那数组结果顺序反过来就可以了
        #也就是最后返回return result[::-1]
        if not root:
            return []
        result=[]
        queue=[root]
        while queue:
            length=len(queue)
            tmp=[]
            for i in range(length):
                node=queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(tmp)
        return result[::-1]