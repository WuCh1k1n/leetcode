# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的
# 房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。 
# 
#  给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,1]
# 输出：4
# 解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
#      偷窃到的最高金额 = 1 + 3 = 4 。 
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 1000 
#  
#  Related Topics 动态规划 
#  👍 457 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution(object):
    def rob(self, nums: List[int]) -> int:
        def helper(nums: List[int]) -> int:
            cur = pre = 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        return max(helper(nums[:-1]), helper(nums[1:])) if len(nums) != 1 else nums[0]
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().rob([1, 2, 3, 1]))
