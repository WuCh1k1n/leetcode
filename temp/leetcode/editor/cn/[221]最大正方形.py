# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]
# ,["1","0","0","1","0"]]
# 输出：4
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [["0"]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 300 
#  matrix[i][j] 为 '0' 或 '1' 
#  
#  Related Topics 动态规划 
#  👍 665 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution(object):
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, columns = len(matrix), len(matrix[0])
        if rows * columns == 0:
            return 0

        dp = [[0] * columns for _ in range(rows)]
        max_side = 0
        for i in range(rows):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                max_side = max(max_side, dp[i][0])
        for j in range(columns):
            if matrix[0][j] == '1':
                dp[0][j] = 1
                max_side = max(max_side, dp[0][j])

        for i in range(1, rows):
            for j in range(1, columns):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side
# leetcode submit region end(Prohibit modification and deletion)
