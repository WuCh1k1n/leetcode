"""
一个序列的 宽度 定义为该序列中最大元素和最小元素的差值。 

 给你一个整数数组 nums ，返回 nums 的所有非空 子序列 的 宽度之和 。由于答案可能非常大，请返回对 10⁹ + 7 取余 后的结果。 

 子序列 定义为从一个数组里删除一些（或者不删除）元素，但不改变剩下元素的顺序得到的数组。例如，[3,6,2,7] 就是数组 [0,3,1,6,2,2,7] 的
一个子序列。 

 

 示例 1： 

 
输入：nums = [2,1,3]
输出：6
解释：子序列为 [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3] 。
相应的宽度是 0, 0, 0, 1, 1, 2, 2 。
宽度之和是 6 。
 

 示例 2： 

 
输入：nums = [2]
输出：0
 

 

 提示： 

 
 1 <= nums.length <= 10⁵ 
 1 <= nums[i] <= 10⁵ 
 

 Related Topics 数组 数学 排序 👍 115 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        res = 0

        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().sumSubseqWidths([2,1,3])
