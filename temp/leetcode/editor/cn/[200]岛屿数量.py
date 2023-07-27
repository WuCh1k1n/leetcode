# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] 的值为 '0' 或 '1' 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 939 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution(object):
    # DFS
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x: int, y: int) -> None:
            if not (0 <= x < height and 0 <= y < width and grid[x][y] == '1'):
                return
            grid[x][y] = '0'
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(x + dx, y + dy)

        res = 0
        height, width = len(grid), len(grid[0])
        for h in range(height):
            for w in range(width):
                if grid[h][w] == '1':
                    res += 1
                    dfs(h, w)
        return res

    # UnionFind
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     height, width = len(grid), len(grid[0])
    #     uf = UnionFind(height * width + 1)
    #     dummy = height * width
    #     for h in range(height):
    #         for w in range(width):
    #             if grid[h][w] == '0':
    #                 uf.union(dummy, h * width + w)
    #             else:
    #                 for (x, y) in ((h + 1, w), (h, w + 1)):
    #                     if 0 <= x < height and 0 <= y < width and grid[x][y] == '1':
    #                         uf.union(h * width + w, x * width + y)
    #     return uf.getcount() - 1


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
