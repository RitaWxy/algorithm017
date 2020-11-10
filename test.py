class Solution:
    def jump(self, nums) :
        self.nums = nums
        self.res = len(nums)
        return self.dfs([0])

    def dfs(self,curPos):
        if curPos[-1] >= len(self.nums)-1:
            self.res = min(self.res,len(curPos)-1)
            return

        for i in range(1,self.nums[curPos[-1]]+1):
            self.dfs(curPos + [curPos[-1] + i])
        return self.res

a=Solution()
print(a.jump([2,3,1,1,4]))
