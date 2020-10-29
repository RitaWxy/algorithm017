# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。 
# 
#  假设一个二叉搜索树具有如下特征： 
# 
#  
#  节点的左子树只包含小于当前节点的数。 
#  节点的右子树只包含大于当前节点的数。 
#  所有左子树和右子树自身必须也是二叉搜索树。 
#  
# 
#  示例 1: 
# 
#  输入:
#     2
#    / \
#   1   3
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
#  
#  Related Topics 树 深度优先搜索 
#  👍 817 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def isValidBST(self, root: TreeNode) -> bool:
    #     # self.res = []
    #     res = self.helper(root)
    #     return res == sorted(list(set(res)))
    #
    # def helper(self,root):
    #     # 中序遍历
    #     if not root:return []
    #     # self.helper(root.left)
    #     # self.res.append(root.val)
    #     # self.helper(root.right)
    #     return self.helper(root.left) + [root.val] +self.helper(root.right)

    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(float('-inf'),float('inf'),root)

    def helper(self,low,high,root):
        if not root: return True
        if root.val <= low or root.val >= high: return False
        if not self.helper(low,root.val,root.left): return False
        if not self.helper(root.val,high,root.right): return False
        return True


# leetcode submit region end(Prohibit modification and deletion)
