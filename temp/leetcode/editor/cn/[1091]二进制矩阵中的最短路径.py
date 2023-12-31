# 在一个 N × N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。 
# 
#  一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格 C_1, C_2, ..., C_k 组成： 
# 
#  
#  相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通（此时，C_i 和 C_{i+1} 不同且共享边或角） 
#  C_1 位于 (0, 0)（即，值为 grid[0][0]） 
#  C_k 位于 (N-1, N-1)（即，值为 grid[N-1][N-1]） 
#  如果 C_i 位于 (r, c)，则 grid[r][c] 为空（即，grid[r][c] == 0） 
#  
# 
#  返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[[0,1],[1,0]]
# 
# 输出：2
# 
#  
# 
#  示例 2： 
# 
#  输入：[[0,0,0],[1,1,0],[1,1,0]]
# 
# 输出：4
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length == grid[0].length <= 100 
#  grid[i][j] 为 0 或 1 
#  
#  Related Topics 广度优先搜索 
#  👍 83 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import heapq
from collections import deque
from typing import List


class Solution(object):
    # def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    #     n = len(grid)
    #     if not grid or grid[0][0] or grid[-1][-1]:
    #         return -1
    #     elif n <= 2:
    #         return n
    #
    #     def heuristic(x, y):
    #         return max(abs(n - 1 - x), abs(n - 1 - y))
    #
    #     h = []
    #     heapq.heappush(h, (0, (0, 0, 1)))
    #     visited = set()
    #     while h:
    #         _, (i, j, step) = heapq.heappop(h)
    #         if (i, j) in visited:
    #             continue
    #         visited.add((i, j))
    #         for dx, dy in [(-1, -1), (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1)]:
    #             next_i, next_j = i + dx, j + dy
    #             if next_i == n - 1 and next_j == n - 1:
    #                 return step + 1
    #             if 0 <= next_i < n and 0 <= next_j < n and grid[next_i][next_j] == 0:
    #                 heapq.heappush(h, (step + heuristic(next_i, next_j), (next_i, next_j, step + 1)))
    #     return -1

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = 1
        q = deque([(0, 0)])
        while q:
            x, y = q.popleft()
            if x == y == n - 1:
                return dist[x][y]
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    new_x, new_y = x + dx, y + dy
                    if not (0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] != 1):
                        continue
                    if dist[x][y] + 1 < dist[new_x][new_y]:
                        dist[new_x][new_y] = dist[x][y] + 1
                        q.append((new_x, new_y))
        return -1
# leetcode submit region end(Prohibit modification and deletion)
