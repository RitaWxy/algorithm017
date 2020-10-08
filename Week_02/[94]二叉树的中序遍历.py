# 给定一个二叉树，返回它的中序 遍历。 
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
# 输出: [1,3,2] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 哈希表 
#  👍 738 👎 0


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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        # if root:
        #     self.inorderTraversal(root.left)
        #     self.travel_path.append(root.val)
        #     self.inorderTraversal(root.right)
        #     return self.travel_path

        # 迭代
        # stack = []
        # if not root:return []
        # while root or stack != []:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     self.travel_path.append(root.val)
        #     root = root.right
        # return self.travel_path

        # 颜色标记 -本质栈递归
        white,gray =0,1 # 0未访问，1访问
        stack = [(white,root)]
        while stack:
            color,node = stack.pop()
            if not node:continue
            if color == white:
                stack.append((white,node.right))
                stack.append((gray,node))
                stack.append((white,node.left))
            else:
                self.travel_path.append(node.val)
        return self.travel_path




        
# leetcode submit region end(Prohibit modification and deletion)
