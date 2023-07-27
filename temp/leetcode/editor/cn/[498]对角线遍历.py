"""
给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。 

 

 示例 1： 
 
 
输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,4,7,5,3,6,8,9]
 

 示例 2： 

 
输入：mat = [[1,2],[3,4]]
输出：[1,2,3,4]
 

 

 提示： 

 
 m == mat.length 
 n == mat[i].length 
 1 <= m, n <= 10⁴ 
 1 <= m * n <= 10⁴ 
 -10⁵ <= mat[i][j] <= 10⁵ 
 

 Related Topics 数组 矩阵 模拟 👍 443 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = list()
        m, n = len(mat), len(mat[0])
        for i in range(m + n - 1):
            if i % 2:
                x = 0 if i < n else i - n + 1
                y = i if i < n else n - 1
                while x < m and y >= 0:
                    res.append(mat[x][y])
                    x, y = x + 1, y - 1
            else:
                x = i if i < m else m - 1
                y = 0 if i < m else i - m + 1
                while x >= 0 and y < n:
                    res.append(mat[x][y])
                    x, y = x - 1, y + 1
        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    # print(Solution().findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # print(Solution().findDiagonalOrder([[1, 2], [3, 4]]))
    print(Solution().findDiagonalOrder([[2, 5], [8, 4], [0, -1]]))
