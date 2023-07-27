# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  1 <= nums[i] <= 100 
#  
#  Related Topics 数组 动态规划 
#  👍 937 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, s = len(nums), sum(nums)
        if s % 2:
            return False
        target_sum = s // 2

        dp = [[0] * (target_sum + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, target_sum + 1):
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
        return dp[-1][-1] > 0
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().canPartition([3, 3, 3, 4, 5])
