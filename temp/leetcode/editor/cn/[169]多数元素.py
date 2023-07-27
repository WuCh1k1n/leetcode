# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。 
# 
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：[3,2,3]
# 输出：3 
# 
#  示例 2： 
# 
#  
# 输入：[2,2,1,1,1,2,2]
# 输出：2
#  
# 
#  
# 
#  进阶： 
# 
#  
#  尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。 
#  
#  Related Topics 位运算 数组 分治算法 
#  👍 838 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    # def majorityElement(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #
    # def majority_element_rec(low, high):
    #     if low == high: return nums[low]
    #     mid = (high - low) // 2 + low
    #     left = majority_element_rec(low, mid)
    #     right = majority_element_rec(mid + 1, high)
    #     if left == right: return left
    #     left_count = sum(1 for i in range(low, high + 1) if nums[i] == left)
    #     right_count = sum(1 for i in range(low, high + 1) if nums[i] == right)
    #     return left if left_count > right_count else right
    #
    # return majority_element_rec(0, len(nums) - 1)
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
# leetcode submit region end(Prohibit modification and deletion)
