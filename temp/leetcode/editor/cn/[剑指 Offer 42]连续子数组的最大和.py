# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。 
# 
#  要求时间复杂度为O(n)。 
# 
#  
# 
#  示例1: 
# 
#  输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^5 
#  -100 <= arr[i] <= 100 
#  
# 
#  注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/ 
# 
#  
#  Related Topics 分治算法 动态规划 
#  👍 213 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划
        # for i in range(1, len(nums)):
        #     nums[i] += max(nums[i - 1], 0)
        # return max(nums)

        # 分治
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            max_left = self.maxSubArray(nums[0:len(nums) // 2])
            max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        return max(max_right, max_left, max_l + max_r)
# leetcode submit region end(Prohibit modification and deletion)
