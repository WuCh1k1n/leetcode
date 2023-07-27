# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
# 
#  输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  限制： 
# 
#  
#  0 <= matrix.length <= 100 
#  0 <= matrix[i].length <= 100 
#  
# 
#  注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/ 
#  Related Topics 数组 
#  👍 203 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        rows, columns = len(matrix), len(matrix[0])
        visited = [[False] * columns for _ in range(rows)]
        total = rows * columns
        ans = [0] * total

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, column = 0, 0
        directions_index = 0

        for i in range(total):
            ans[i] = matrix[row][column]
            visited[row][column] = True
            next_row, next_column = row + directions[directions_index][0], column + directions[directions_index][1]
            if not (0 <= next_row < rows and 0 <= next_column < columns and not visited[next_row][next_column]):
                directions_index = (directions_index + 1) % 4
            row += directions[directions_index][0]
            column += directions[directions_index][1]
        return ans
# leetcode submit region end(Prohibit modification and deletion)
