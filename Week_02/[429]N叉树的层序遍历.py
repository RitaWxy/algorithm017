# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。 
# 
#  例如，给定一个 3叉树 : 
# 
#  
# 
#  
# 
#  
# 
#  返回其层序遍历: 
# 
#  [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
#  
# 
#  
# 
#  说明: 
# 
#  
#  树的深度不会超过 1000。 
#  树的节点总数不会超过 5000。 
#  Related Topics 树 广度优先搜索 
#  👍 111 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    import collections
    def __init__(self):
        self.travel_path = []
    # 递归
    # def _helper(self,root,level):
    #     if root:
    #         if len(self.travel_path)<level+1:
    #             self.travel_path.append([])
    #         self.travel_path[level].append(root.val)
    #
    #     for node in root.children:
    #         self._helper(node,level+1)
    #
    # def levelOrder(self, root: 'Node') -> List[List[int]]:
    #     if not root: return []
    #     self._helper(root,0)
    #     return self.travel_path

    # 双端队列实现BFS
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        queue = collections.deque([root])
        while queue:
            curlevel = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curlevel.append(node.val)
                queue.extend(node.children)
            self.travel_path.append(curlevel)
        return self.travel_path


        
# leetcode submit region end(Prohibit modification and deletion)
