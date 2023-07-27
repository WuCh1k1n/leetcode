# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [7,5,6,4]
# 输出: 5 
# 
#  
# 
#  限制： 
# 
#  0 <= 数组长度 <= 50000 
#  👍 356 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        return self.mergeSort(nums, 0, n - 1)

    def mergeSort(self, nums: List[int], left: int, right: int) -> int:
        count = 0
        if left >= right:
            return count
        mid = (left + right) // 2
        count = self.mergeSort(nums, left, mid) + self.mergeSort(nums, mid + 1, right)
        i, j, k = left, mid + 1, 0
        tmp = [0] * (right - left + 1)
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                tmp[k] = nums[i]
                i += 1
                count += (j - (mid + 1))
            else:
                tmp[k] = nums[j]
                j += 1
            k += 1
        for p in range(i, mid + 1):
            tmp[k] = nums[p]
            k += 1
            count += (j - (mid + 1))
        for p in range(j, right + 1):
            tmp[k] = nums[p]
            k += 1
        nums[left:right + 1] = tmp
        return count
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().reversePairs([3, 4, 1, 2]))
