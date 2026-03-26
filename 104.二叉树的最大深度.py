'''
104. 二叉树的最大深度
简单
给定一个二叉树 root ，返回其最大深度。
二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #如果使用迭代法，就可以用层序遍历来实现，在遍历的时候记录下层数
        if not root:
            return 0
        depth=0
        queue=[root]
        while queue:
            depth+=1#在这里记录层数即可
            length=len(queue)
            for i in range(length):
                node=queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth