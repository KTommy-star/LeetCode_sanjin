'''

102. 二叉树的层序遍历
中等
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
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
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        #图中的广度优先搜索BFS，来应用到二叉树中，就是实现层序遍历
        #广度优先需要用队列作为辅助结构，我们先将根节点放到队列中，然后不断遍历队列。
        if not root:
            return []
        result=[]
        queue=[root]#初始时，队列中只有根节点
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
            result.append(tmp)#每一层加一次
        return result