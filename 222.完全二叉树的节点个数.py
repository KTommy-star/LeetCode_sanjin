'''

222. 完全二叉树的节点个数
简单
给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层（从第 0 层开始），则该层包含 1~2h 个节点。
name:sanjin
date:2026.3.31
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #求节点个数，还是可以用很熟悉的层序遍历的模版来做
        if not root:
            return 0
        count=0
        queue=[root]
        while queue:
            length=len(queue)
            for i in range(length):
                node=queue.pop(0)
                count+=1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return count
    #第二种方法，利用完全二叉树的性质，来计算节点个数
    def countNodes_v2(self,root):
        #核心是计算树的高度，如果左子树和右子树的高度相同，那么说明左子树是满二叉树，节点个数为2^h-1
        #这是算法效率最高的解
        if not root:
            return 0
        left=root.left
        right=root.right
        left_depth=0
        right_depth=0
        while left:
            left=left.left
            left_depth+=1
        while right:
            right=right.right
            right_depth+=1
        if left_depth==right_depth:
            return 2**(left_depth+1)-1
        return self.countNodes_v2(root.left)+self.countNodes_v2(root.right)+1#根节点要算，所以+1