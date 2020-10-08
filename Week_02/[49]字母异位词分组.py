# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。 
# 
#  示例: 
# 
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ] 
# 
#  说明： 
# 
#  
#  所有输入均为小写字母。 
#  不考虑答案输出的顺序。 
#  
#  Related Topics 哈希表 字符串 
#  👍 483 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def __init__(self):
    #     self.dic = {}
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     for i in strs:
    #         if not self.dic.get(''.join(sorted(i))):
    #             self.dic[''.join(sorted(i))] = []
    #         self.dic[''.join(sorted(i))].append(i)
    #     return list(self.dic.values())
    from collections import  defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in strs:
            ans[tuple(sorted(i))].append(i)
        return list(ans.values())

# leetcode submit region end(Prohibit modification and deletion)
