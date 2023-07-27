# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ] 
#  Related Topics 回溯算法 
#  👍 1069 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(candidates: List[int], path: List[int]) -> None:
            if not candidates:
                res.append(path)
                return
            for i in range(len(candidates)):
                backtrack(candidates[:i] + candidates[i + 1:], path + [candidates[i]])

        res = []
        backtrack(nums, [])
        return res
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    Solution().permute([1, 2, 3])
