'''

117. 填充每个节点的下一个右侧节点指针 II
中等

给定一个二叉树：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL 。
初始状态下，所有 next 指针都被设置为 NULL 。
name:sanjin
date:2026.3.25
'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        queue=[root]
        while queue:
            length=len(queue)
            prev=None
            for i in range(length):
                node=queue.pop(0)
                if prev:
                    prev.next=node
                prev=node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root