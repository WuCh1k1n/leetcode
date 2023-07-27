"""
给定一组 n 人（编号为 1, 2, ..., n）， 我们想把每个人分进任意大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。 

 给定整数 n 和数组 dislikes ，其中 dislikes[i] = [ai, bi] ，表示不允许将编号为 ai 和 bi的人归入同一组。当可以用这种
方法将所有人分进两组时，返回 true；否则返回 false。 

 

 
 

 示例 1： 

 
输入：n = 4, dislikes = [[1,2],[1,3],[2,4]]
输出：true
解释：group1 [1,4], group2 [2,3]
 

 示例 2： 

 
输入：n = 3, dislikes = [[1,2],[1,3],[2,3]]
输出：false
 

 示例 3： 

 
输入：n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
输出：false
 

 

 提示： 

 
 1 <= n <= 2000 
 0 <= dislikes.length <= 10⁴ 
 dislikes[i].length == 2 
 1 <= dislikes[i][j] <= n 
 ai < bi 
 dislikes 中每一组都 不同 
 

 

 Related Topics 深度优先搜索 广度优先搜索 并查集 图 👍 336 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class UF:
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if self.size[root_p] >= self.size[root_q]:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]
        else:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]

    def connected(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        return root_p == root_q

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def count(self):
        return self.count


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = [[] for _ in range(n)]
        for x, y in dislikes:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)
        uf = UF(n)
        for x, nodes in enumerate(g):
            for y in nodes:
                uf.union(nodes[0], y)
                if uf.connected(x, y):
                    return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
