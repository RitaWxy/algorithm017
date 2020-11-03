# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。 
# 
#  说明：不要使用任何内置的库函数，如 sqrt。 
# 
#  示例 1： 
# 
#  输入：16
# 输出：True 
# 
#  示例 2： 
# 
#  输入：14
# 输出：False
#  
#  Related Topics 数学 二分查找 
#  👍 174 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2: return True
        l,r = 2,num//2
        while l<=r:
            mid = (l+r)//2
            if mid*mid == num: return True
            elif mid*mid >num: r = mid-1
            else:l=mid+1
        return False
        # 牛顿法
        # if num<2: return True
        # ans = num//2
        # while ans*ans > num:
        #     ans = (ans+num/ans)//2
        # return ans*ans == num
# leetcode submit region end(Prohibit modification and deletion)
