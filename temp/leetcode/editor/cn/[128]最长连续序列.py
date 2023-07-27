# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。 
# 
#  请你设计并实现时间复杂度为 O(n) 的算法解决此问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
#  Related Topics 并查集 数组 哈希表 👍 978 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak

        # res, n = 0, len(nums)
        # nums.sort()
        # counter = collections.Counter()
        # for i in range(n):
        #     if counter[nums[i] - 1] > 0:
        #         counter[nums[i]] = counter[nums[i] - 1] + 1
        #     else:
        #         counter[nums[i]] = 1
        #     res = max(res, counter[nums[i]])
        # return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
