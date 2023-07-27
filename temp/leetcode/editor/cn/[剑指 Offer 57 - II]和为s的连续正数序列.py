# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。 
# 
#  序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。 
# 
#  
# 
#  示例 1： 
# 
#  输入：target = 9
# 输出：[[2,3,4],[4,5]]
#  
# 
#  示例 2： 
# 
#  输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
#  
# 
#  
# 
#  限制： 
# 
#  
#  1 <= target <= 10^5 
#  
# 
#  
#  👍 246 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left, right, s, res = 1, 2, 3, []
        while left < right:
            if s == target:
                res.append(list(range(left, right + 1)))
            if s >= target:
                s -= left
                left += 1
            else:
                right += 1
                s += right
        return res
# leetcode submit region end(Prohibit modification and deletion)
