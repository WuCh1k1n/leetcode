# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：nums = [1,2,3,4]
# 输出：[1,3,2,4] 
# 注：[3,1,2,4] 也是正确的答案之一。 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 50000 
#  1 <= nums[i] <= 10000 
#  
#  👍 84 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] & 1:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        return nums
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().exchange([1, 2, 3, 4])
