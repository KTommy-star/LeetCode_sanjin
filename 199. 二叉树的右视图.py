'''

199. 二叉树的右视图
中等
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
name:sanjin
date:2026-3-23
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        #从右边看是看每一层的最后一个节点（从左往右）
        #所以我们只需要在层序遍历的时候每一层记录一下最后一个节点就可以了
        if not root:
            return []
        result=[]
        queue=[root]
        while queue:
            length=len(queue)
            for i in range(length):
                node=queue.pop(0)
                if i==length-1:#代表遍历到了每一层的最后一个节点
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

    def rightSideView_dfs(self, root):
        #第二种方法使用dfs
        #我们在dfs的过程中，记录当前的层数，如果当前层数等于结果数组的长度，说明这是该层第一次访问到的节点，也就是最右边的节点
        result=[]
        def dfs(node,depth):
            if not node:
                return
            # 当当前深度等于结果列表长度时，记录该节点（即当前层第一个被访问的节点）,因为这是一个右递归的写法，做一新的一层第一个访问的节点，就是该层的最后一个节点
            if depth==len(result):
                result.append(node.val)
            # 先递归右子树，再递归左子树
            dfs(node.right,depth+1)
            dfs(node.left,depth+1)
        dfs(root,0)
        return result
