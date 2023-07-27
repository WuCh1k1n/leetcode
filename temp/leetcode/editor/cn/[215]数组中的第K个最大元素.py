# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。 
# 
#  请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#  
# 
#  示例 2: 
# 
#  
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= nums.length <= 104 
#  -104 <= nums[i] <= 104 
#  
#  Related Topics 数组 分治 快速选择 排序 堆（优先队列） 
#  👍 1323 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 堆排序
        # heapq.heapify(nums)
        # for _ in range(len(nums) - k):
        #     heapq.heappop(nums)
        # return nums[0]

        # 快速排序
        self.quickSort(nums, 0, len(nums) - 1)
        return nums[-k]

    def quickSort(self, nums: List[int], start: int, end: int) -> None:
        def partition(nums: List[int], start: int, end: int) -> int:
            pivot, counter = end, start
            for i in range(start, end):
                if nums[i] < nums[pivot]:
                    nums[i], nums[counter] = nums[counter], nums[i]
                    counter += 1
            nums[counter], nums[pivot] = nums[pivot], nums[counter]
            return counter

        if start >= end:
            return
        pivot = partition(nums, start, end)
        self.quickSort(nums, start, pivot - 1)
        self.quickSort(nums, pivot + 1, end)
# leetcode submit region end(Prohibit modification and deletion)
