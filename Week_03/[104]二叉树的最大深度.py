# 给定一个二叉树，找出其最大深度。 
# 
#  二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例： 
# 给定二叉树 [3,9,20,null,null,15,7]， 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  返回它的最大深度 3 。 
#  Related Topics 树 深度优先搜索 
#  👍 728 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 遍历
    # def maxDepth(self, root: TreeNode) -> int:
    #
    #     return len(self.helper(root,1,[]))
    #
    # def helper(self,root,level,res):
    #     if not root: return res
    #     if len(res) < level: res.append([])
    #     res[level-1].append(root.val)
    #     self.helper(root.left,level+1,res)
    #     self.helper(root.right,level+1,res)
    #     return res
    # BFS
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        res = 0
        queue = [root]
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res += 1
        return res
    
    # 递归
    # def maxDepth(self, root: TreeNode) -> int:
    #     if not root: return 0
    #     return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))





# leetcode submit region end(Prohibit modification and deletion)
