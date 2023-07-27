# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 
# 
#  
# 
#  示例: 
# 
#  board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false 
# 
#  
# 
#  提示： 
# 
#  
#  board 和 word 中只包含大写和小写英文字母。 
#  1 <= board.length <= 200 
#  1 <= board[i].length <= 200 
#  1 <= word.length <= 10^3 
#  
#  Related Topics 数组 回溯算法 
#  👍 766 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def backtrace(i: int, j: int, target: str) -> bool:
            if not target:
                return True
            if 0 <= i < m and 0 <= j < n and board[i][j] != '#' and board[i][j] == target[0]:
                temp = board[i][j]
                board[i][j] = '#'
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if backtrace(i + dx, j + dy, target[1:]):
                        return True
                board[i][j] = temp
            return False

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if backtrace(i, j, word):
                    return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
