'''

515. 在每个树行中找最大值
中等
给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。

name:sanjin
date:2026.3.24

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        #这个题也是模版题，在层序遍历的时候。在单层遍历里面，每一次用一个max函数来更新最大值，然后吧最大值加入结果数组就好
        if not root:
            return []
        result=[]
        queue=[root]
        while queue:
            length=len(queue)
            max_val=float('-inf')

            for i in range(length):
                node=queue.pop(0)
                max_val=max(max_val,node.val)
                if node.left:
                   queue.append(node.left)
                if node.right:
                   queue.append(node.right)
            result.append(max_val)
        return result