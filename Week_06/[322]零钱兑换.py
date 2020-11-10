# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回
#  -1。 
# 
#  你可以认为每种硬币的数量是无限的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3 
# 解释：11 = 5 + 5 + 1 
# 
#  示例 2： 
# 
#  
# 输入：coins = [2], amount = 3
# 输出：-1 
# 
#  示例 3： 
# 
#  
# 输入：coins = [1], amount = 0
# 输出：0
#  
# 
#  示例 4： 
# 
#  
# 输入：coins = [1], amount = 1
# 输出：1
#  
# 
#  示例 5： 
# 
#  
# 输入：coins = [1], amount = 2
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= coins.length <= 12 
#  1 <= coins[i] <= 231 - 1 
#  0 <= amount <= 104 
#  
#  Related Topics 动态规划 
#  👍 908 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 递归

        # BFS
        # queue = [amount]
        # res = 0
        # visited = set()
        # while queue:
        #     for _ in range(len(queue)):
        #         curCoin = queue.pop(0)
        #         if curCoin == 0: return res
        #         if (curCoin>0) and (curCoin not in visited):
        #             visited.add(curCoin)
        #             for i in coins:
        #                 queue.append(curCoin-i)
        #     res += 1
        # return -1

        # DP(类似爬楼梯)
        # DP[n]凑到面值为n的最少的硬币个数 = min(DP[n-k] for k in coins)+1
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1,amount+1):
            for k in coins:
                if k <= i: dp[i] = min(dp[i],dp[i-k]+1)
        return -1 if dp[amount]>=amount+1 else dp[amount]


# leetcode submit region end(Prohibit modification and deletion)
