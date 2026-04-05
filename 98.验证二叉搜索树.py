'''

98. 验证二叉搜索树
中等
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
有效二叉搜索树定义如下：
节点的左子树只包含 严格小于 当前节点的数。
节点的右子树只包含 严格大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
name:sanjin
date:2026.4.5
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.result=[]
    def traversal(self,root):
        if not root:
            return []
        self.traversal(root.left)
        self.result.append(root.val)
        self.traversal(root.right)
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.result=[]
        self.traversal(root)#先进行中序遍历，来得到一个有序的列表
        for i in range(1,len(self.result)):
            if self.result[i] <= self.result[i-1]:
                return False
        return True
class Solution_1(object):
    def __init__(self):
        self.maxval=float('inf')
    def isvalibst(self,root):
        #第二种方式是利用中序遍历的顺序，在遍历的时候，同时也比较节点值和上一个节点值，如果有发生前一个大于后一个的情况，就说明false
        if not root:
            return True
        left=self.isvalibst(root.left)
        if self.maxval <= root.val:
            self.maxval=root.val
        else:
            return False
        right=self.isvalibst(root.right)

        return left and right
