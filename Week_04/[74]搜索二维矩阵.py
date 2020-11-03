# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性： 
# 
#  
#  每行中的整数从左到右按升序排列。 
#  每行的第一个整数大于前一行的最后一个整数。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [], target = 0
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  0 <= m, n <= 100 
#  -104 <= matrix[i][j], target <= 104 
#  
#  Related Topics 数组 二分查找 
#  👍 271 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if (not matrix) or (not matrix[0]): return False
        m,n = len(matrix),len(matrix[0])
        # low,high= 0,n-1
        # for line in range(m):
        #     if target > matrix[line][n-1]:continue
        #     if target < matrix[line][0]:return False
        #     while low <= high:
        #         mid = (low+high)//2
        #         if target == matrix[line][mid]:return True
        #         if target>matrix[line][mid]:
        #             low = mid + 1
        #         else: high = mid - 1
        # return False

        # 行号 = idx//n,列数 = idx % n
        low,high = 0,m*n-1
        while low <= high:
            mid = (low+high)//2
            if target == matrix[mid//n][mid%n]:
                return True
            if target < matrix[mid // n][mid % n]:
                high = mid - 1
            else: low = mid +1
        return False


# leetcode submit region end(Prohibit modification and deletion)
