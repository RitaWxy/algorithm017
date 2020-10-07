# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 
# 
#  
# 
#  上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Mar
# cos 贡献此图。 
# 
#  示例: 
# 
#  输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6 
#  Related Topics 栈 数组 双指针 
#  👍 1725 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        # 针对每个位置循环
        # ans = 0
        # for i in range(0,len(height)):
        #     l_max = max(height[:i+1])
        #     r_max = max(height[i:])
        #     ans += min(l_max,r_max)-height[i]
        # return ans

        # 双指针
        left,right = 0,len(height)-1
        l_max,r_max = 0,0
        ans = 0
        while left < right:
            if height[left] < height[right]:
                if height[left]>=l_max:
                    l_max = height[left]
                else:
                    ans += l_max - height[left]
                left += 1
            else:
                if height[right]>=r_max:
                    r_max = height[right]
                else:
                    ans += r_max - height[right]
                right -= 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
