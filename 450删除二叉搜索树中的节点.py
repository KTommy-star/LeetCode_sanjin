'''

450. 删除二叉搜索树中的节点
中等
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
一般来说，删除节点可分为两个步骤：
首先找到需要删除的节点；
如果找到了，删除它。
name:sanjin
date:2026.4.9
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        #删除节点，则是在前面需要通过正常比较大小的便利，来找到目标节点的位置
        #找到目标节点后，有三种情况：1.目标节点是叶子节点，这样直接删除；2.目标节点只有一个节点，那就直接把该节点用子节点替换；
        #3.目标节点有两个子节点，这样就需要找到右子树的最小节点，来替换目标节点，这样才不会破坏二叉搜索树的结构
        if not root:
            return None
        if root.val > key:
            root.left=self.deleteNode(root.left,key)
            return root
        if root.val < key:
            root.right=self.deleteNode(root.right,key)
            return root
        #接下来是找到了目标节点的情况，也就是==key
        if not root.left and not root.right:
            return None
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        if root.left and root.right:
            min_node=root.right
            while min_node.left:
                min_node=min_node.left
            root.val=min_node.val#用右子树的最小节点来替换目标节点
            root.right=self.deleteNode(root.right,min_node.val)#因为已经替换了，所以在原本的那个右子树的最小节点需要删除
        return root
