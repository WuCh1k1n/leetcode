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
from typing import List


class Solution:
    def max_heapify(self, heap, root, heap_len):
        p = root
        while p * 2 + 1 < heap_len:
            l, r = p * 2 + 1, p * 2 + 2
            if heap_len <= r or heap[r] < heap[l]:
                nex = l
            else:
                nex = r
            if heap[p] < heap[nex]:
                heap[p], heap[nex] = heap[nex], heap[p]
                p = nex
            else:
                break

    def build_heap(self, heap):
        for i in range(len(heap) - 1, -1, -1):
            self.max_heapify(heap, i, len(heap))

    def heap_sort(self, nums):
        self.build_heap(nums)
        for i in range(len(nums) - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.max_heapify(nums, 0, i)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.heap_sort(nums)
        return nums
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().sortArray([4, 6, 8, 5, 9])
