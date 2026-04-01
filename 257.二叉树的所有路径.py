'''

257. 二叉树的所有路径
简单
给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
叶子节点 是指没有子节点的节点。

name:sanjin
date:2026.4.1
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        #如果要记录路径，那最好的方式就是前序遍历，因为前序遍历的顺序就是根节点-左子树-右子树，这样我们在访问到叶子节点的时候就可以把路径记录下来
        #首先使用迭代法
        if not root:
            return []
        stack=[root]
        path_st=[str(root.val)]
        result=[]
        while stack:
            node=stack.pop()
            path=path_st.pop()
            if not node.left and not node.right:
                result.append(path)
            if node.right:
                stack.append(node.right)
                path_st.append(path+'->'+str(node.right.val))#拼接出根节点到右子节点的完整路径，并将其压入路径栈（path_st）
            if node.left:
                stack.append(node.left)
                path_st.append(path+'->'+str(node.left.val))
        return result
    #当然也可以使用递归法，递归法的思路和迭代法一样，只是递归法更简洁好写
    def dfs(self,node,path,result):
        path.append(node.val)
        if not node.left and not node.right:
            result.append('->'.join(map(str,path)))#map(str,path)是把 path 列表中的所有元素都转换成字符串，然后用'->'连接起来，最后加入结果数组
            return #这里要return是因为如果当前节点是叶子节点了，那么就不需要继续往下递归了，直接返回就好了
        if node.left:
            self.dfs(node.left,path,result)
            path.pop()#回溯
        if node.right:
            self.dfs(node.right,path,result)
            path.pop()
    def binaryTreePaths_recursion(self,root):
        if not root:
            return []
        result=[]
        path=[]
        self.dfs(root,path,result)
        return result


