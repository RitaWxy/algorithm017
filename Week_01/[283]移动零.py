# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。 
# 
#  示例: 
# 
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0] 
# 
#  说明: 
# 
#  
#  必须在原数组上操作，不能拷贝额外的数组。 
#  尽量减少操作次数。 
#  
#  Related Topics 数组 双指针 
#  👍 757 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[j] = nums[i]
        #         if i != j: nums[i] = 0
        #         j += 1

        # 交换0
        j=0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j],nums[i] = nums[i],nums[j]
                j += 1

        # 循环计数
        # nums = [x for x in nums if x != 0] + [0] * nums.count(0)

        # 循环删除添加 时间复杂度高o(n^2)
        # for i in nums[:]: # in nums则错
        #     if i == 0:
        #         nums.append(0)
        #         nums.remove(0)
# leetcode submit region end(Prohibit modification and deletion)
