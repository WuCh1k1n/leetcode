"""
给你一个大小为 n x n 二进制矩阵 grid 。最多 只能将一格 0 变成 1 。 

 返回执行此操作后，grid 中最大的岛屿面积是多少？ 

 岛屿 由一组上、下、左、右四个方向相连的 1 形成。 

 

 示例 1: 

 
输入: grid = [[1, 0], [0, 1]]
输出: 3
解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
 

 示例 2: 

 
输入: grid = [[1, 1], [1, 0]]
输出: 4
解释: 将一格0变成1，岛屿的面积扩大为 4。 

 示例 3: 

 
输入: grid = [[1, 1], [1, 1]]
输出: 4
解释: 没有0可以让我们变成1，面积依然为 4。 

 

 提示： 

 
 n == grid.length 
 n == grid[i].length 
 1 <= n <= 500 
 grid[i][j] 为 0 或 1 
 

 Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 285 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        tag = [[0] * n for _ in range(n)]
        area = Counter()

        def dfs(i: int, j: int) -> None:
            tag[i][j] = t
            area[t] += 1
            for x, y in [(i - 1, j), [i + 1, j], [i, j - 1], [i, j + 1]]:
                if 0 <= x < n and 0 <= y < n and grid[x][y] and tag[x][y] == 0:
                    dfs(x, y)

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x and tag[i][j] == 0:
                    t = i * n + j + 1
                    dfs(i, j)
        ans = max(area.values(), default=0)

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 0:
                    new_area = 1
                    connected = {0}
                    for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                        if 0 <= x < n and 0 <= y < n and tag[x][y] not in connected:
                            new_area += area[tag[x][y]]
                            connected.add(tag[x][y])
                    ans = max(ans, new_area)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
