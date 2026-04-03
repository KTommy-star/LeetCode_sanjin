'''
654. 最大二叉树
中等
给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:
创建一个根节点，其值为 nums 中的最大值。
递归地在最大值 左边 的 子数组前缀上 构建左子树。
递归地在最大值 右边 的 子数组后缀上 构建右子树。
返回 nums 构建的 最大二叉树 。

name:sanjin
date:2026.4.3
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        #看完题目初步思路，就是找到最大值及其索引，然后根据索引吧数组分成两部分，然后分别构造子树，最后返回根节点
        if len(nums)==1:
            return TreeNode(nums[0])
        node=TreeNode(0)#初始创建一个节点
        maxvalue=0
        maxvaluindex=0
        #用一个for循环，来找到最大值及其索引
        for i in range(len(nums)):
            if nums[i] > maxvalue:
                maxvalue=nums[i]
                maxvaluindex=i
        node.val=maxvalue#将最大值赋值给节点
        #左递归生成左子树
        if maxvaluindex > 0:
            node.left=self.constructMaximumBinaryTree(nums[:maxvaluindex])
        #右递归生成右子树
        if maxvaluindex < len(nums) - 1:
            node.right=self.constructMaximumBinaryTree(nums[maxvaluindex+1:])
        return node