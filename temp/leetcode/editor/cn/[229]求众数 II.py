# 给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。 
# 
#  进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：[3,2,3]
# 输出：[3] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1]
# 输出：[1]
#  
# 
#  示例 3： 
# 
#  
# 输入：[1,1,1,3,3,2,2,2]
# 输出：[1,2] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5 * 104 
#  -109 <= nums[i] <= 109 
#  
#  Related Topics 数组 
#  👍 324 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        if not nums:
            return res

        # cand1 = cand2 = nums[0]
        # count1 = count2 = 0
        # for num in nums:
        #     if num == cand1:
        #         count1 += 1
        #         continue
        #     if num == cand2:
        #         count2 += 1
        #         continue
        #     if count1 == 0:
        #         cand1 = num
        #         count1 += 1
        #         continue
        #     if count2 == 0:
        #         cand2 = num
        #         count2 += 1
        #         continue
        #     count1 -= 1
        #     count2 -= 1
        #
        # count1 = count2 = 0
        # for num in nums:
        #     if num == cand1:
        #         count1 += 1
        #     elif num == cand2:
        #         count2 += 1
        # if count1 > len(nums) / 3:
        #     res.append(cand1)
        # if count2 > len(nums) / 3:
        #     res.append(cand2)

        counter = collections.Counter(nums)
        for k in counter.keys():
            if counter[k] > len(nums) / 3:
                res.append(k)
        return res
# leetcode submit region end(Prohibit modification and deletion)
