'''

501. 二叉搜索树中的众数
简单
给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。
如果树中有不止一个众数，可以按 任意顺序 返回。
假定 BST 满足如下定义：
结点左子树中所含节点的值 小于等于 当前节点的值
结点右子树中所含节点的值 大于等于 当前节点的值
左子树和右子树都是二叉搜索树
name:sanjin
date:2026.4.7
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.count=0
        self.max_count=0
        self.result=[]
        self.prev=None#需要定义一个prev节点来记录上一个节点的值，用于比较
    def searchBST(self,root):
        if not root:
            return []
        self.searchBST(root.left)
        if self.prev == None:
            self.count=1
        elif self.prev.val==root.val:
            self.count+=1
        else:
            self.count=1
        self.prev=root
        if self.count==self.max_count:
            self.result.append(root.val)
        elif self.count > self.max_count:
            self.max_count=self.count
            self.result=[root.val]#如果最大值发生了更新，那么就需要把结果数组重置一下，因为之前的众数已经不再是众数了
        self.searchBST(root.right)
        return
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.count=0
        self.max_count=0
        self.prev=None
        self.result=[]

        self.searchBST(root)
        return self.result