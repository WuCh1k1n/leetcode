"""
给你一个整数数组 nums 和一个整数 k ，找出 nums 中和至少为 k 的 最短非空子数组 ，并返回该子数组的长度。如果不存在这样的 子数组 ，返回 -1
 。 

 子数组 是数组中 连续 的一部分。 

 

 
 

 示例 1： 

 
输入：nums = [1], k = 1
输出：1
 

 示例 2： 

 
输入：nums = [1,2], k = 4
输出：-1
 

 示例 3： 

 
输入：nums = [2,-1,2], k = 3
输出：3
 

 

 提示： 

 
 1 <= nums.length <= 10⁵ 
 -10⁵ <= nums[i] <= 10⁵ 
 1 <= k <= 10⁹ 
 

 Related Topics 队列 数组 二分查找 前缀和 滑动窗口 单调队列 堆（优先队列） 👍 556 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import deque


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pre_sum_arr = [0]
        res = float('inf')
        for num in nums:
            pre_sum_arr.append(pre_sum_arr[-1] + num)
        print(pre_sum_arr)
        q = deque()
        for i, cur_sum in enumerate(pre_sum_arr):
            while q and cur_sum - pre_sum_arr[q[0]] >= k:
                res = min(res, i - q.popleft())
            while q and pre_sum_arr[q[-1]] >= cur_sum:
                q.pop()
            q.append(i)
        return res if res != float('inf') else -1
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    Solution().shortestSubarray([84, -37, 32, 40, 95], 167)
