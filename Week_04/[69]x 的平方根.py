# 实现 int sqrt(int x) 函数。 
# 
#  计算并返回 x 的平方根，其中 x 是非负整数。 
# 
#  由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。 
# 
#  示例 1: 
# 
#  输入: 4
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
#      由于返回类型是整数，小数部分将被舍去。
#  
#  Related Topics 数学 二分查找 
#  👍 531 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分查找
        # if x==0 or x==1: return x
        # left,right = 0,x//2
        # while math.floor(left)<math.floor(right):
        #     mid = 0.5*(left+right)
        #     if mid*mid >x:
        #         right = mid
        #     else: left = mid
        # return math.floor(left)

        # 死循环，l=1,r=3时总是更新l
        # if x== 0 or x ==1: return x
        # l,r = 1,math.floor(x/2)
        # while l < r:
        #     mid = math.floor((l+(r-l))/2)
        #     if mid*mid == x:
        #         break
        #     elif mid*mid <x: l = mid
        #     else: r = mid
        # return mid
        
        # 牛顿迭代
        if x<2: return x
        ans = x//2
        while abs(ans*ans - x)>1e-6:
            ans = (ans+x/ans)/2
        return int(ans)


# leetcode submit region end(Prohibit modification and deletion)
