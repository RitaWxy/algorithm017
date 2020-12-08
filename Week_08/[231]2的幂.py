# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。 
# 
#  示例 1: 
# 
#  输入: 1
# 输出: true
# 解释: 20 = 1 
# 
#  示例 2: 
# 
#  输入: 16
# 输出: true
# 解释: 24 = 16 
# 
#  示例 3: 
# 
#  输入: 218
# 输出: false 
#  Related Topics 位运算 数学 
#  👍 263 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
    # 是2的幂次=>有且仅有一个二进制位是1
    #     if n>0 and bin(n).count('1')==1: return True
    #     return False

        if n > 0 and n&(n-1) == 0: return True
        return False
        # return n > 0 and n&(n-1) == 0:

# leetcode submit region end(Prohibit modification and deletion)
