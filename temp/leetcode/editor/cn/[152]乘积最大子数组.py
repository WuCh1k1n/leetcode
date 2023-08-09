# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#  
# 
#  示例 2: 
# 
#  输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 
#  Related Topics 数组 动态规划 
#  👍 925 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution(object):
    def maxProduct(self, nums: List[int]) -> int:
        dp = [nums[:], nums[:]]
        for i in range(1, len(nums)):
            dp[0][i] = max(nums[i], nums[i] * dp[0][i - 1], nums[i] * dp[1][i - 1])
            dp[1][i] = min(nums[i], nums[i] * dp[0][i - 1], nums[i] * dp[1][i - 1])
        return max(dp[0])


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    Solution().maxProduct([-2, 3, 4])
