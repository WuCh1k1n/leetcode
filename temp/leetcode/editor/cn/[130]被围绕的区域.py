# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。 
# 
#  找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。 
# 
#  示例: 
# 
#  X X X X
# X O O X
# X X O X
# X O X X
#  
# 
#  运行你的函数后，矩阵变为： 
# 
#  X X X X
# X X X X
# X X X X
# X O X X
#  
# 
#  解释: 
# 
#  被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被
# 填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 468 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution(object):
    # DFS
    # def solve(self, board: List[List[str]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #
    #     def dfs(x: int, y: int) -> None:
    #         if not (0 <= x < height and 0 <= y < width and board[x][y] == 'O'):
    #             return
    #         board[x][y] = "#"
    #         for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    #             dfs(x + dx, y + dy)
    #
    #     height, width = len(board), len(board[0])
    #     for h in range(height):
    #         dfs(h, 0)
    #         dfs(h, width - 1)
    #     for w in range(width):
    #         dfs(0, w)
    #         dfs(height - 1, w)
    #
    #     for h in range(height):
    #         for w in range(width):
    #             if board[h][w] == '#':
    #                 board[h][w] = 'O'
    #             elif board[h][w] == 'O':
    #                 board[h][w] = 'X'

    # UnionFind
    def solve(self, board: List[List[str]]) -> None:
        def dfs(x, y):
            if not (0 <= x < height and 0 <= y < width and board[x][y] == 'O'):
                return
            uf.union(dummy, x * width + y)
            board[x][y] = '#'
            for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(x + dx, y + dy)

        height, width = len(board), len(board[0])
        uf = UnionFind(height * width + 1)
        dummy = height * width
        for h in range(height):
            dfs(h, 0)
            dfs(h, width - 1)
        for w in range(width):
            dfs(0, w)
            dfs(height - 1, w)
        for h in range(height):
            for w in range(width):
                if board[h][w] == 'O' and not uf.connected(dummy, h * width + w):
                    board[h][w] = 'X'
                elif board[h][w] == '#':
                    board[h][w] = 'O'


class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def union(self, p, q):
        root_p, root_q = self.find(p), self.find(q)
        if root_p == root_q:
            return
        if self.size[root_p] > self.size[root_q]:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]
        else:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        self.count -= 1

    def connected(self, p, q):
        root_p, root_q = self.find(p), self.find(q)
        return root_p == root_q

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def getcount(self):
        return self.count
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]])
