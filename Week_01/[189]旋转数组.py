# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。 
# 
#  示例 1: 
# 
#  输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#  
# 
#  示例 2: 
# 
#  输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100] 
# 
#  说明: 
# 
#  
#  尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。 
#  要求使用空间复杂度为 O(1) 的 原地 算法。 
#  
#  Related Topics 数组 
#  👍 709 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 循环
        # for i in range(k): o(n*k)
        #     nums.insert(0, nums.pop())

        # 创建新数组 下标变为(i+k)%len o(n)
        # new = [0]*len(nums)
        # for i in range(len(nums)):
        #     new[(i+k)%(len(nums))] = nums[i]
        # nums[:] = new[:]

        # 环状代替
        if (len(nums) == 1 or len(nums) == k or k == 0): return
        if k>len(nums): k %= len(nums)
        start,end = 0,0 # 每次替换的两个位置
        init = 0 # 每一轮的起始位置
        orig = nums[start] # 被移动的值
        for i in range(len(nums)): # 每个都遍历一遍
            end = (start+k)%len(nums)
            temp = nums[end] # 被替换掉的值
            nums[end] = orig
            start = end
            if init == start:
                start += 1
                init = start
                orig = nums[init]
            else:
                orig = temp






# leetcode submit region end(Prohibit modification and deletion)
