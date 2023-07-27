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
    def randomized_partition(self, nums, l, r):
        pivot = random.randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        counter = l
        for i in range(l, r):
            if nums[i] < nums[r]:
                nums[i], nums[counter] = nums[counter], nums[i]
                counter += 1
        nums[counter], nums[r] = nums[r], nums[counter]
        return counter

    def randomized_quicksort(self, nums, l, r):
        if l > r:
            return
        mid = self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums
# leetcode submit region end(Prohibit modification and deletion)
