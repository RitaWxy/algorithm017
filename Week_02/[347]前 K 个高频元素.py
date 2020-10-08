# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。 
# 
#  
# 
#  示例 1: 
# 
#  输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#  
# 
#  示例 2: 
# 
#  输入: nums = [1], k = 1
# 输出: [1] 
# 
#  
# 
#  提示： 
# 
#  
#  你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。 
#  你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。 
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。 
#  你可以按任意顺序返回答案。 
#  
#  Related Topics 堆 哈希表 
#  👍 538 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 哈希表 o(nlogn)
        hash_map = {}
        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1
        res = sorted(hash_map.keys(), key=lambda x: hash_map[x], reverse=True)
        return res[:k]



    # 使用计数器之后构建最小堆
    # 堆的元素可以是元组类型
    # 因为求前 K 个高频元素，python 默认最小堆，则将频次取负再入堆
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     dic = collections.Counter(nums)
    #     heap, ans = [], []
    #     for i in dic:
    #         heapq.heappush(heap, (-dic[i], i))
    #     for _ in range(k):
    #         ans.append(heapq.heappop(heap)[1])
    #     return ans






# leetcode submit region end(Prohibit modification and deletion)
