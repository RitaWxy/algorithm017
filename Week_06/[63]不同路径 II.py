# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。 
# 
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。 
# 
#  现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？ 
# 
#  
# 
#  网格中的障碍物和空位置分别用 1 和 0 来表示。 
# 
#  说明：m 和 n 的值均不超过 100。 
# 
#  示例 1: 
# 
#  输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
#  
#  Related Topics 数组 动态规划 
#  👍 441 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0]==1:return 0
        if obstacleGrid==[[0]]:return 1

        m,n = len(obstacleGrid),len(obstacleGrid[0])
        # dp = [[0 for _ in range(n)] for _ in range(m)]
        # # 初始化
        # for col in range(n):
        #     if obstacleGrid[0][col] == 1: break
        #     dp[0][col] = 1
        # for row in range(1,m):
        #     if obstacleGrid[row][0] == 1: break
        #     dp[row][0] = 1
        # # 递推
        # for i in range(1,m):
        #     for j in range(1,n):
        #         if obstacleGrid[i][j] != 1:
        #             dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # print(dp)
        # return dp[-1][-1]

        # 降维
        dp = [0 for _ in range(n)]
        for col in range(n):
            if obstacleGrid[0][col] == 1: break
            dp[col] = 1
        for i in range(1,m):
            for j in range(0,n):
                if j == 0: # 第一列初始化
                    if dp[j]==0 or obstacleGrid[i][j]==1: dp[j] = 0
                    else: dp[j] = 1
                    continue
                if obstacleGrid[i][j] != 1:
                    dp[j] += dp[j-1]
                else: dp[j] = 0
        return dp[-1]

# leetcode submit region end(Prohibit modification and deletion)
