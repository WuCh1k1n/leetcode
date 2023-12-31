# 给定一个非负整数数组，你最初位于数组的第一个位置。 
# 
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。 
# 
#  你的目标是使用最少的跳跃次数到达数组的最后一个位置。 
# 
#  示例: 
# 
#  输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#  
# 
#  说明: 
# 
#  假设你总是可以到达数组的最后一个位置。 
#  Related Topics 贪心算法 数组 
#  👍 802 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution(object):
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_pos, end, step = 0, 0, 0
        for i in range(n - 1):
            if i <= max_pos:
                max_pos = max(max_pos, i + nums[i])
                if i == end:
                    end = max_pos
                    step += 1
        return step
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().jump([2, 3, 1, 1, 4])
