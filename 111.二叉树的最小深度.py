'''

111. 二叉树的最小深度
简单
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。
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
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #最小深度也可以用层序遍历的模版来做，只是加一个判定是叶子节点的逻辑
        if not root:
            return 0
        queue=[root]
        depth=0
        while queue:
            depth+=1
            length=len(queue)
            for i in range(length):
                node=queue.pop(0)
                if not node.left and not node.right:#判定是否为叶子节点
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth