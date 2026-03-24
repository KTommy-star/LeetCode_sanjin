'''
429. N 叉树的层序遍历
中等

给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。
树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。
name:sanjin
date:2026.3.24
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        #这个题也是层序遍历的模版题，只是在queue添加的时候，有一个for循环，去添加该节点的所有子节点
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
                for child in node.children:
                        queue.append(child)
            result.append(tmp)
        return result