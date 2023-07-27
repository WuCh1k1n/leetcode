# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上
# 被小偷闯入，系统会自动报警。 
# 
#  给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。 
# 
#  示例 2： 
# 
#  输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 100 
#  0 <= nums[i] <= 400 
#  
#  Related Topics 动态规划 
#  👍 1264 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution(object):
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [[0] * n for _ in range(2)]
        # dp[1][0] = nums[0]
        # for i in range(1, n):
        #     dp[0][i] = max(dp[0][i - 1], dp[1][i - 1])
        #     dp[1][i] = dp[0][i - 1] + nums[i]
        # return max(dp[0][-1], dp[1][-1])

        # cur_not_rob, cur_rob = 0, nums[0]
        # for num in nums[1:]:
        #     pre_not_rob, pre_rob = cur_not_rob, cur_rob
        #     cur_not_rob = max(pre_not_rob, pre_rob)
        #     cur_rob = pre_not_rob + num
        # return max(cur_not_rob, cur_rob)

        cur = pre = 0
        for num in nums:
            cur, pre = max(pre + num, cur), cur
        return cur
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().rob([2, 7, 9, 3, 1])
