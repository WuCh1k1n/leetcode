# 编写一个程序，通过填充空格来解决数独问题。 
# 
#  一个数独的解法需遵循如下规则： 
# 
#  
#  数字 1-9 在每一行只能出现一次。 
#  数字 1-9 在每一列只能出现一次。 
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。 
#  
# 
#  空白格用 '.' 表示。 
# 
#  
# 
#  一个数独。 
# 
#  
# 
#  答案被标成红色。 
# 
#  提示： 
# 
#  
#  给定的数独序列只包含数字 1-9 和字符 '.' 。 
#  你可以假设给定的数独只有唯一解。 
#  给定数独永远是 9x9 形式的。 
#  
#  Related Topics 哈希表 回溯算法 
#  👍 747 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def backtrack(n: int = 0) -> bool:
            if n == len(empty):
                return True
            i, j = empty[n]
            block = i // 3 * 3 + j // 3
            for val in rows[i] & cols[j] & blocks[block]:
                rows[i].remove(val)
                cols[j].remove(val)
                blocks[block].remove(val)
                board[i][j] = str(val)
                if backtrack(n + 1):
                    return True
                rows[i].add(val)
                cols[j].add(val)
                blocks[block].add(val)
                board[i][j] = '.'
            return False

        rows = [set(range(1, 10)) for _ in range(9)]
        cols = [set(range(1, 10)) for _ in range(9)]
        blocks = [set(range(1, 10)) for _ in range(9)]
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    rows[i].remove(val)
                    cols[j].remove(val)
                    blocks[i // 3 * 3 + j // 3].remove(val)
                else:
                    empty.append((i, j))
        backtrack()
# leetcode submit region end(Prohibit modification and deletion)
