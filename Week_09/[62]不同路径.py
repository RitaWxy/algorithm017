# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。 
# 
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。 
# 
#  问总共有多少条不同的路径？ 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：m = 3, n = 7
# 输出：28 
# 
#  示例 2： 
# 
#  
# 输入：m = 3, n = 2
# 输出：3
# 解释：
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
#  
# 
#  示例 3： 
# 
#  
# 输入：m = 7, n = 3
# 输出：28
#  
# 
#  示例 4： 
# 
#  
# 输入：m = 3, n = 3
# 输出：6 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= m, n <= 100 
#  题目数据保证答案小于等于 2 * 109 
#  
#  Related Topics 数组 动态规划 
#  👍 825 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        #   return self.helper(m-1,n-1)
        #
        # # 分治
        # def helper(self,row,col):
        #     if row <0 or col<0: return 0
        #     if row == 0 or col == 0: return 1
        #     return self.helper(row-1,col)+self.helper(row,col-1)

        # dp = [[0] *n]*m
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 or j == 0: dp[i][j]=1
        #         else: dp[i][j] = dp[i-1][j]+dp[i][j-1]
        # return dp[m-1][n-1]

        dp = [1] * n
        for i in range(1, m):
            for j in range(n):
                if j == 0: continue
                dp[j] += dp[j - 1]
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
