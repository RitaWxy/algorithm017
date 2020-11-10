# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#  
# 
#  示例 2: 
# 
#  输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 
#  Related Topics 数组 动态规划 
#  👍 829 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp[i][0] 最小值，dp[i][1]最大值
        if not nums: return 0
        dp_max,dp_min,max_res = nums[0],nums[0],nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0: dp_max,dp_min = dp_min,dp_max
            dp_max = max(dp_max * nums[i],nums[i])
            dp_min = min(dp_min * nums[i],nums[i])
            max_res = max(dp_max,max_res)
        return max_res

# leetcode submit region end(Prohibit modification and deletion)
