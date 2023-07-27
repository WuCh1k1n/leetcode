# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。 
# 
#  示例 1 : 
# 
#  
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
#  
# 
#  说明 : 
# 
#  
#  数组的长度为 [1, 20,000]。 
#  数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。 
#  
#  Related Topics 数组 哈希表 前缀和 
#  👍 1079 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        pre_sum = [0] * (len(nums) + 1)
        pre_sum_cnt = collections.defaultdict(int)
        pre_sum_cnt[0] = 1
        for i in range(len(nums)):
            pre_sum[i + 1] = pre_sum[i] + nums[i]
            delta = pre_sum[i + 1] - k
            if delta in pre_sum_cnt:
                res += pre_sum_cnt[delta]
            pre_sum_cnt[pre_sum[i + 1]] += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
