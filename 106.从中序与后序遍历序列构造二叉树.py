'''
106. 从中序与后序遍历序列构造二叉树
中等
给定两个整数数组 inorder 和 postorder ，
其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树
name:sanjin
date:2026.4.2
'''
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        #本题的核心逻辑就是：根据中序遍历和后序遍历来构造二叉树
        #我们可以用递归来实现，递归的话需要用后序遍历的模版来写，因为我们需要先对当前节点进行操作，再判断左子树和右子树的值
        #所以我们可以用递归来判断每个节点的值是否等于后序遍历的最后一个元素，因为后序的最后一个元素相当于是“中”如果等于就返回这个节点，如果不等于就继续递归判断它的左子树和右子树，直到遍历到叶子节点为止

        #第一步：如果后序遍历的列表为空，说明没有节点了，直接返回None
        if not postorder:
            return None
        #第二步，取后序数组的最后一个元素作为节点元素
        root_val=postorder[-1]
        #第三步：找到该元素在中序数组的位置，作为切割点
        location=inorder.index(root_val)
        #第四步：根据切割点把中序数组分成左右两部分，
        #左子树的中序数组是inorder[:location]，右子树的中序数组是inorder[location+1:]
        inorder_left=inorder[:location]
        inorder_right=inorder[location+1:]
        #第五步：根据切割点把后序数组分成左右两部分，
        #左子树的后序数组是postorder[:location]，右子树的后序数组是postorder[location:-1]，注意这里要去掉最后一个元素，因为它是根节点了
        postorder_left=postorder[:location]
        postorder_right=postorder[location:-1]
        #第六步则是递归构造左子树和右子树
        root=TreeNode(root_val)#首先需要创建节点
        root.left=self.buildTree(inorder_left,postorder_left)
        root.right=self.buildTree(inorder_right,postorder_right)
        return root

