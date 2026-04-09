'''
669. 修剪二叉搜索树
中等
给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。
通过修剪二叉搜索树，使得所有节点的值在[low, high]中。
修剪树 不应该 改变保留在树中的元素的相对结构 (即，如果没有被移除，原有的父代子代关系都应当保留)。 可以证明，存在 唯一的答案 。
所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。

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
    def trimBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: Optional[TreeNode]
        """
        #还是通过递归来找到符合区间的节点，重点是这里接入符合条件的左右孩子节点
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right,low,high)
        if root.val > high:
            return self.trimBST(root.left,low,high)
        #上面的逻辑上筛选出符合区间的节点了，接下来就是要把符合条件的节点的左右孩子节点也要进行修剪了，用递归调用非常的方便
        root.left=self.trimBST(root.left,low,high)
        root.right=self.trimBST(root.right,low,high)
    def trimBST_iteration(self,root,low,high):
        if not root:
            return None
        #迭代的思路就是先找到符合条件的根节点，然后再对这个根节点的左右子树进行修剪
        while root and (root.val<low or root.val>high):
            if root.val < low:
                root=root.right
            if root.val > high:
                root=root.left
        cur=root
        while cur:
            while cur.left and cur.left.val<low:
                cur.left=cur.left.right
            cur=cur.left
        cur=root
        while cur:
            while cur.right and cur.right.val > high:
                cur.right=cur.right.left
            cur=cur.right
        return root