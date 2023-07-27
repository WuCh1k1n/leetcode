# 给定一个整数数组 nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。 
# 
#  示例 1： 
# 
#  输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= len(nums) <= 16 
#  0 < nums[i] < 10000 
#  
#  Related Topics 位运算 记忆化搜索 数组 动态规划 回溯 状态压缩 
#  👍 398 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 以数字的视角
        # def backtrace(nums: List[int], index: int, buckets: List[int], target: int) -> bool:
        #     if index == len(nums):
        #         for bucket in buckets:
        #             if bucket != target:
        #                 return False
        #         return True
        #     for i in range(len(buckets)):
        #         buckets[i] += nums[index]
        #         if buckets[i] <= target:
        #             if backtrace(nums, index + 1, buckets, target):
        #                 return True
        #         buckets[i] -= nums[index]
        #     return False

        # 以桶的视角
        def backtrace(i: int, bucket_sum: int, nums: List[int], start: int, used: List[bool], target: int) -> bool:
            if i == 0:
                return True
            if bucket_sum == target:
                return backtrace(i - 1, 0, nums, 0, used, target)
            for j in range(start, len(nums)):
                if used[j]:
                    continue
                bucket_sum += nums[j]
                used[j] = True
                if bucket_sum <= target:
                    if backtrace(i, bucket_sum, nums, j + 1, used, target):
                        return True
                bucket_sum -= nums[j]
                used[j] = False
            return False

        s = sum(nums)
        if s % k:
            return False
        buckets = [0] * k
        return backtrace(k, 0, nums, 0, [False] * len(nums), s // k)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)
