# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 8 
#  -10 <= nums[i] <= 10 
#  
#  Related Topics 回溯算法 
#  👍 557 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(candidates, path):
            if not candidates:
                return res.append(path) if path not in res else None
            for i in range(len(candidates)):
                backtrack(candidates[:i] + candidates[i + 1:], path + [candidates[i]])
        res = []
        backtrack(nums, [])
        return res
# leetcode submit region end(Prohibit modification and deletion)
