'''

637. 二叉树的层平均值
简单
给定一个非空二叉树的根节点 root , 以数组的形式返回每一层节点的平均值。与实际答案相差 10-5 以内的答案可以被接受。
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
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        #还是按照层序遍历来写，只是result数组变成每一层遍历的时候，加入的是计算一下平均值
        if not root:
            return []
        result=[]
        queue=[root]
        while queue:
            length=len(queue)
            level_sum=0.0#这里一定要是浮点数类型，否则会出现整数除法的报错
            for i in range(length):
                node=queue.pop(0)
                level_sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_sum / length)
        return result
