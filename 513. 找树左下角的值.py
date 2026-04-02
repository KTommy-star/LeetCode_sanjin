'''
513. 找树左下角的值
中等
给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
假设二叉树中至少有一个节点。
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
    def findBottomLeftValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #本题又是层序遍历的模版题，只需要遍历到最后一层时，取最左边的值记录下来就可以了
        if not root:
            return None
        queue=[root]
        result=0
        while queue:
            length=len(queue)
            for i in range(length):
                node=queue.pop(0)
                if i==0:#这是在记录每一层的最后一个节点的值，这样在遍历到最后一层时，记录的就是最左边的值了
                    result=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result