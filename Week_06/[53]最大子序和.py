# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  示例: 
# 
#  输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#  
# 
#  进阶: 
# 
#  如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。 
#  Related Topics 数组 分治算法 动态规划 
#  👍 2610 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i][0]不取这个数，dp[i][1]取这个数
        # if len(nums)==1: return nums[0]
        # dp = [[0 for _ in range(2)] for _ in range(len(nums))]
        # for i in range(len(nums)):
        #     if i == 0: dp[i][0]=dp[i][1] = nums[0]
        #     else:
        #         dp[i][0]=max(dp[i-1][0],dp[i-1][1])
        #         dp[i][1] = max(dp[i-1][1]+nums[i],nums[i])
        # print(dp)
        # return max(dp[-1][0],dp[-1][1])
        # 降维
        # dp=[nums[0],nums[0]]
        # res = max(dp)
        # for i in range(1,len(nums)):
        #     dp[0] = max(dp)
        #     dp[1] = max(dp[1]+nums[i],nums[i])
        #     res = max(res,dp[0],dp[1])
        # return res

        '''
        dp:当前元素自身最大，或者包含前i-1个最大
        dp[i] = max(dp[i-1],nums[i])
        包含第i个元素的最大值
        :param nums:
        :return:
        '''
        for i in range(1,len(nums)):
            nums[i] = max(nums[i-1]+nums[i],nums[i])
        return max(nums)

# leetcode submit region end(Prohibit modification and deletion)
