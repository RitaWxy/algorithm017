# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。 
# 
#  相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。 
# 
#  
# 
#  例如，给定三角形： 
# 
#  [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#  
# 
#  自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。 
# 
#  
# 
#  说明： 
# 
#  如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。 
#  Related Topics 数组 动态规划 
#  👍 639 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle: return 0
    # 递归，超时 o(2^n)
    #     self.triangle = triangle
    #     return self.helper(len(triangle)-1,0,0,triangle[0][0])
    #
    # def helper(self,maxLevel,i,j,curRes):
    #     if i >= maxLevel:
    #         return curRes
    #
    #     a=self.helper(maxLevel,i+1,j,curRes+self.triangle[i+1][j])
    #     b=self.helper(maxLevel,i+1,j+1,curRes+self.triangle[i+1][j+1])
    #     return min(a,b)

    # 自顶向下DP
    # a. 重复性(分治) f(i,j) = min(sub(i+1,j),sub(i+1,j+1)) + triangle(i,j)
    # b. 定义状态数组 f(i,j)
    # c. DP方程
    #     dp = triangle
    #     for i in range(1,len(triangle)):
    #         for j in range(len(triangle[i])):
    #             if j == 0: dp[i][j] += dp[i-1][j]
    #             elif j == len(triangle[i])-1: dp[i][j] += dp[i-1][j-1]
    #             else: dp[i][j] += min(dp[i-1][j-1],dp[i-1][j])
    #     return min(dp[-1])

    # 自底向上
    #     dp = triangle
    #     for i in range(len(triangle)-2,-1,-1):
    #         for j in range(len(triangle[i])):
    #             dp[i][j] += min(dp[i + 1][j], dp[i + 1][j+1])
    #     return dp[0][0]

    # 自底向上 降维
        dp = triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j],dp[j+1]) + triangle[i][j]
        return dp[0]







# leetcode submit region end(Prohibit modification and deletion)
