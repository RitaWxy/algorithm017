# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例： 
# 
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#  
#  Related Topics 字符串 回溯算法 
#  👍 1390 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n: return []
        self.res = []
        self.n = n
        self.helper(0,0,'')
        return self.res

    def helper(self,left,right,subres):
        if left == right and left == self.n:
            self.res.append(subres)
            return
        if left < self.n: self.helper(left+1,right,subres+'(')
        if left > right and right<= self.n: self.helper(left,right+1,subres+')')

# leetcode submit region end(Prohibit modification and deletion)
