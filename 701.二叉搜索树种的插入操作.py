'''

701. 二叉搜索树中的插入操作
中等
给定二叉搜索树（BST）的根节点 root 和要插入树中的值 value ，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。
注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。

name:sanjin
date:2026.4.9
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        #依据二叉搜索树的性质，我们在遍历的时候判断数值大小，就可以决定递归的方向
        #有一个区别就是，需要在遍历到空节点的时候，在该位置创建一个新的节点
        if not root:
            return TreeNode(val)
        if root.val>val:
            root.left=self.insertIntoBST(root.left,val)
        if root.val<val:
            root.right=self.insertIntoBST(root.right,val)
        return root