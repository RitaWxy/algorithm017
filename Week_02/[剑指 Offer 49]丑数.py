# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。 
# 
#  
# 
#  示例: 
# 
#  输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。 
# 
#  说明: 
# 
#  
#  1 是丑数。 
#  n 不超过1690。 
#  
# 
#  注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/ 
#  Related Topics 数学 
#  👍 76 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 三指针
        # num2 = 【1*2，2*2，3*2，4*2，...】
        # num3 = 【1*3，2*3，3*3，4*3，...】
        # num5 = 【1*5，2*5，3*5，4*5，...】
        # num2, num3, num5 = [1], [1], [1]
        # p2, p3, p5 = 0, 0, 0
        # for i in range(n):
        #     res = min(num2[p2], num3[p3], num5[p5])
        #     num2.append(res * 2)
        #     num3.append(res * 3)
        #     num5.append(res * 5)
        #     if res == num2[p2]:
        #         p2 += 1
        #     if res == num3[p3]:
        #         p3 += 1
        #     if res == num5[p5]:
        #         p5 += 1
        # return res

        # 动态规划：第i个丑数等于2/3/5乘上之前某一个丑数的最小值
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            dp[i] = min(2 * dp[a], 3 * dp[b], 5 * dp[c])
            if dp[i] == 2 * dp[a]: a += 1
            if dp[i] == 3 * dp[b]: b += 1
            if dp[i] == 5 * dp[c]: c += 1
        return dp[n - 1]

# leetcode submit region end(Prohibit modification and deletion)
