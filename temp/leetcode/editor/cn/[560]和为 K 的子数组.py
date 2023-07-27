"""
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。 

 

 示例 1： 

 
输入：nums = [1,1,1], k = 2
输出：2
 

 示例 2： 

 
输入：nums = [1,2,3], k = 3
输出：2
 

 

 提示： 

 
 1 <= nums.length <= 2 * 10⁴ 
 -1000 <= nums[i] <= 1000 
 -10⁷ <= k <= 10⁷ 
 

 Related Topics 数组 哈希表 前缀和 👍 1834 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import Counter


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        pre_sum, counter = [0] * (n + 1), Counter()
        counter[0] = 1
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]
            res += counter[pre_sum[i + 1] - k]
            counter[pre_sum[i + 1]] += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().subarraySum([1, 1, 1], 2)
