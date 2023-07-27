"""
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b],
 nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）： 

 
 0 <= a, b, c, d < n 
 a、b、c 和 d 互不相同 
 nums[a] + nums[b] + nums[c] + nums[d] == target 
 

 你可以按 任意顺序 返回答案 。 

 

 示例 1： 

 
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
 

 示例 2： 

 
输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]
 

 

 提示： 

 
 1 <= nums.length <= 200 
 -10⁹ <= nums[i] <= 10⁹ 
 -10⁹ <= target <= 10⁹ 
 

 Related Topics 数组 双指针 排序 👍 1579 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, n = list(), len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for l in self.threeSum(nums[i + 1:], target - nums[i]):
                res.append([nums[i]] + l)
        return res

    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = list()
        # nums.sort()
        for k in range(len(nums) - 2):
            # if nums[k] > target:
            #     break
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                t = nums[i] + nums[j] + nums[k]
                if t == target:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                elif t < target:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                else:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11)
