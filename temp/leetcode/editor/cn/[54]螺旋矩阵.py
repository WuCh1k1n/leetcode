# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 10 
#  -100 <= matrix[i][j] <= 100 
#  
#  Related Topics 数组 
#  👍 614 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution(object):
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res, visited = list(), set()
        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_idx = 0
        row = col = 0
        for _ in range(m * n):
            res.append(matrix[row][col])
            visited.add((row, col))
            dx, dy = directions[direction_idx]
            new_row, new_col = row + dx, col + dy
            if not (0 <= new_row < m and 0 <= new_col < n and (new_row, new_col) not in visited):
                direction_idx = (direction_idx + 1) % 4
            dx, dy = directions[direction_idx]
            row, col = row + dx, col + dy
        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
