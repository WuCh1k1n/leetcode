"""
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。 

 返回这三个数的和。 

 假定每组输入只存在恰好一个解。 

 

 示例 1： 

 
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 

 示例 2： 

 
输入：nums = [0,0,0], target = 1
输出：0
 

 

 提示： 

 
 3 <= nums.length <= 1000 
 -1000 <= nums[i] <= 1000 
 -10⁴ <= target <= 10⁴ 
 

 Related Topics 数组 双指针 排序 👍 1378 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = nums[0] + nums[1] + nums[2]
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                cur_sum = nums[left] + nums[right] + nums[i]
                if abs(cur_sum - target) < abs(res - target):
                    res = cur_sum
                if cur_sum < target:
                    left += 1
                elif cur_sum > target:
                    right -= 1
                else:
                    return res
        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2)
