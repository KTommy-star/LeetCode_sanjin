'''

538. 把二叉搜索树转换为累加树
中等
给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
提醒一下，二叉搜索树满足下列约束条件：
节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。
注意：本题和 1038: https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/ 相同

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
    def __init__(self):
        self.pre=0
    def traversal(self,root):
        if not root:
            return None
        self.traversal(root.right)
        root.val+=self.pre
        self.pre=root.val
        self.traversal(root.left)
    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        #对于任意一个二叉搜索树的根节点，其右子树的值都比他大，所以可以通过右子树累加和，来替换根节点的值
        #常规来讲，如果转换成数组，那就能很轻松的指导是东侯往前进行累加就可以了，那么懂了二叉搜索树的结构，其实也可以就按照右中左的顺序来遍历，这样在中间节点逻辑的时候就进行累加操作就可以
        self.pre=0
        self.traversal(root)
        return root