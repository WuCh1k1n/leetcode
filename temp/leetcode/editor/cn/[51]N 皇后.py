# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。 
# 
#  
#  
#  每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[["Q"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 9 
#  皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。 
#  
#  
#  
#  Related Topics 回溯算法 
#  👍 722 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def generate_board():
            board = list()
            for i in range(n):
                rows[queens[i]] = 'Q'
                board.append(''.join(rows))
                rows[queens[i]] = '.'
            return board

        def backtrack(row):
            if row == n:
                board = generate_board()
                res.append(board)
                return
            for col in range(n):
                if col in columns or row + col in diagonal1 or row - col in diagonal2:
                    continue
                queens[row] = col
                columns.add(col)
                diagonal1.add(row + col)
                diagonal2.add(row - col)
                backtrack(row + 1)
                columns.remove(col)
                diagonal1.remove(row + col)
                diagonal2.remove(row - col)

        res = list()
        queens = [-1] * n
        rows = ['.'] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        backtrack(0)
        return res
# leetcode submit region end(Prohibit modification and deletion)
