# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]
# ,["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = []
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [["0"]]
# 输出：0
#  
# 
#  示例 4： 
# 
#  
# 输入：matrix = [["1"]]
# 输出：1
#  
# 
#  示例 5： 
# 
#  
# 输入：matrix = [["0","0"]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  rows == matrix.length 
#  cols == matrix[0].length 
#  0 <= row, cols <= 200 
#  matrix[i][j] 为 '0' 或 '1' 
#  
#  Related Topics 栈 数组 哈希表 动态规划 
#  👍 816 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution(object):
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 + dp[i][j - 1] if j > 0 else 1
        res = 0
        for i in range(m - 1, -1, -1):
            for j in range(n):
                w, h = dp[i][j], 1
                k = i
                while k >= 0 and matrix[k][j] == '1':
                    w = min(w, dp[k][j])
                    res = max(res, w * h)
                    h += 1
                    k -= 1
        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().maximalRectangle([["1"]]))
