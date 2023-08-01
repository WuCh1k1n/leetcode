# 给你一个整数数组 nums，请你将该数组升序排列。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
#  
# 
#  示例 2： 
# 
#  输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 50000 
#  -50000 <= nums[i] <= 50000 
#  
#  Related Topics 数组 分治 桶排序 计数排序 基数排序 排序 堆（优先队列） 归并排序 
#  👍 390 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums: List[int], l: int, r: int) -> None:
        def randomized_partition(nums: List[int]) -> int:
            pivot, counter = random.randint(l, r), l
            nums[pivot], nums[r] = nums[r], nums[pivot]
            for i in range(l, r):
                if nums[i] < nums[r]:
                    nums[i], nums[counter] = nums[counter], nums[i]
                    counter += 1
            nums[counter], nums[r] = nums[r], nums[counter]
            return counter

        if l > r:
            return
        pivot = randomized_partition(nums)
        l_upper = r_lower = pivot
        while l_upper > 0 and nums[l_upper] == nums[l_upper - 1]:
            l_upper -= 1
        self.quickSort(nums, l, l_upper - 1)
        while r_lower < r and nums[r_lower] == nums[r_lower + 1]:
            r_lower += 1
        self.quickSort(nums, pivot + 1, r)
# leetcode submit region end(Prohibit modification and deletion)
