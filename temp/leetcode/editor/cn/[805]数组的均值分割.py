"""
给定你一个整数数组
 nums 

 我们要将
 nums 数组中的每个元素移动到 A 数组 或者 B 数组中，使得 A 数组和
 B 数组不为空，并且
 average(A) == average(B) 。 

 如果可以完成则返回true ， 否则返回 false 。 

 注意：对于数组
 arr , 
 average(arr) 是
 arr 的所有元素的和除以
 arr 长度。 

 

 示例 1: 

 
输入: nums = [1,2,3,4,5,6,7,8]
输出: true
解释: 我们可以将数组分割为 [1,4,5,8] 和 [2,3,6,7], 他们的平均值都是4.5。
 

 示例 2: 

 
输入: nums = [3,1]
输出: false
 

 

 提示: 

 
 1 <= nums.length <= 30 
 0 <= nums[i] <= 10⁴ 
 

 Related Topics 位运算 数组 数学 动态规划 状态压缩 👍 290 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        def backtrack(i: int, bucket_sum: int, bucket_len: int, start: int, used: List[bool], target: int) -> bool:
            if i == 0:
                return True
            if bucket_len and bucket_sum / bucket_len == target:
                return backtrack(i - 1, 0, 0, 0, used, target)
            for j in range(start, len(nums)):
                if used[j]:
                    continue
                bucket_sum += nums[j]
                bucket_len += 1
                used[j] = True
                if backtrack(i, bucket_sum, bucket_len, j + 1, used, target):
                    return True
                bucket_sum -= nums[j]
                bucket_len -= 1
                used[j] = False
            return False

        s, n = sum(nums), len(nums)
        k = 2
        return backtrack(k, 0, 0, 0, [False] * n, s / n)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().splitArraySameAverage([1, 2, 3, 4, 5, 6, 7, 8]))
    print(Solution().splitArraySameAverage([3, 1]))
