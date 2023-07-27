# 
#  
#  有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连
# 。 
# 
#  省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。 
# 
#  给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 
# isConnected[i][j] = 0 表示二者不直接相连。 
# 
#  返回矩阵中 省份 的数量。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 200 
#  n == isConnected.length 
#  n == isConnected[i].length 
#  isConnected[i][j] 为 1 或 0 
#  isConnected[i][i] == 1 
#  isConnected[i][j] == isConnected[j][i] 
#  
#  
#  
#  Related Topics 深度优先搜索 并查集 
#  👍 488 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 深度优先
    # def findCircleNum(self, isConnected):
    #     """
    #     :type isConnected: List[List[int]]
    #     :rtype: int
    #     """
    #     def dfs(i):
    #         for j in range(city_num):
    #             if isConnected[i][j] == 1 and j not in visited:
    #                 visited.add(j)
    #                 dfs(j)
    #
    #     ans = 0
    #     city_num = len(isConnected)
    #     visited = set()
    #
    #     for i in range(city_num):
    #         if i not in visited:
    #             dfs(i)
    #             ans += 1
    #     return ans

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    uf.union(i, j)
        return uf.getcount()


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
