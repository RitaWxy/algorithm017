# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  
# 
#  上图为 8 皇后问题的一种解法。 
# 
#  给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。 
# 
#  每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
# 
#  
# 
#  示例： 
# 
#  输入：4
# 输出：[
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#  
# 
#  
# 
#  提示： 
# 
#  
#  皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。 
#  
#  Related Topics 回溯算法 
#  👍 687 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        self.DFS(n,0,0,0,0,[])
        return [ ['.'*col + 'Q' + '.'*(n-col-1) for col in path] for path in self.res]
    def DFS(self,n,level,col,pie,na,cur):
        if level >= n:
            self.res.append(cur)
            return
        # 当前层
        bits = (~(col | pie | na)) & ((1<<n)-1)
        while bits:
            pos = bits & -bits
            bits = bits & (bits-1) # 现在还能放的位置

            # 取最低位1的index：放在哪里了：bin(pos-1).count('1')
            self.DFS(n,level+1,col|pos,(pie|pos)<<1,(na|pos)>>1,cur+[bin(pos-1).count('1')])




# leetcode submit region end(Prohibit modification and deletion)
