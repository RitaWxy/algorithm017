# 给定一个二叉树，返回它的 前序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]  
#    1
#     \
#      2
#     /
#    3 
# 
# 输出: [1,2,3]
#  
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 
#  👍 378 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.travel_path = []
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        self.travel_path.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.travel_path

        
# leetcode submit region end(Prohibit modification and deletion)
