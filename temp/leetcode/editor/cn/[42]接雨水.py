# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
#  
# 
#  示例 2： 
# 
#  
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == height.length 
#  0 <= n <= 3 * 104 
#  0 <= height[i] <= 105 
#  
#  Related Topics 栈 数组 双指针 
#  👍 1927 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution(object):
    def trap(self, heights: List[int]) -> int:
        res = 0
        mono_stack = list()
        for i in range(len(heights)):
            while mono_stack and heights[i] > heights[mono_stack[-1]]:
                top = mono_stack.pop()
                if not mono_stack:
                    break
                w = i - mono_stack[-1] - 1
                h = min(heights[i], heights[mono_stack[-1]]) - heights[top]
                res += w * h
            mono_stack.append(i)
        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(heights))
