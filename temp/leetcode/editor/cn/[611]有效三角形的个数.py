"""
给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。 

 

 示例 1: 

 
输入: nums = [2,2,3,4]
输出: 3
解释:有效的组合是: 
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3
 

 示例 2: 

 
输入: nums = [4,2,3,4]
输出: 4 

 

 提示: 

 
 1 <= nums.length <= 1000 
 0 <= nums[i] <= 1000 
 

 Related Topics 贪心 数组 双指针 二分查找 排序 👍 541 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        nums.sort()
        for i in range(0, n):
            k = i
            for j in range(i + 1, n):
                while k + 1 < n and nums[k + 1] < nums[i] + nums[j]:
                    k += 1
                res += max(k - j, 0)
        return res
# leetcode submit region end(Prohibit modification and deletion)
