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
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows = len(matrix)
        if rows == 0: return 0
        cols = len(matrix[0])

        ans = 0
        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 + dp[i][j - 1]

        for i in range(rows - 1, -1, -1):
            for j in range(cols):
                w, h = dp[i][j], 1
                k = i
                while k >= 0 and matrix[k][j] == '1':
                    w = min(dp[k][j], w)
                    ans = max(ans, w * h)
                    h += 1
                    k -= 1

        return ans
# leetcode submit region end(Prohibit modification and deletion)
