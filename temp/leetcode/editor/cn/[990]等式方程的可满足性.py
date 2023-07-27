# 给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!
# =b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。 
# 
#  只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：["a==b","b!=a"]
# 输出：false
# 解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。
#  
# 
#  示例 2： 
# 
#  输入：["b==a","a==b"]
# 输出：true
# 解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。
#  
# 
#  示例 3： 
# 
#  输入：["a==b","b==c","a==c"]
# 输出：true
#  
# 
#  示例 4： 
# 
#  输入：["a==b","b!=c","c==a"]
# 输出：false
#  
# 
#  示例 5： 
# 
#  输入：["c==c","b==d","x!=z"]
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= equations.length <= 500 
#  equations[i].length == 4 
#  equations[i][0] 和 equations[i][3] 是小写字母 
#  equations[i][1] 要么是 '='，要么是 '!' 
#  equations[i][2] 是 '=' 
#  
#  Related Topics 并查集 图 数组 字符串 
#  👍 185 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from string import ascii_lowercase


class UnionFind(object):
    def __init__(self, n):
        # 记录连通分量个数
        self.count = n
        # 存储若干棵树
        self.parent = [i for i in range(n)]
        # 记录树的重量
        self.size = [1] * n

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if self.size[root_p] > self.size[root_q]:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]
        else:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        self.count -= 1

    def connected(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        return root_p == root_q

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def getcount(self):
        return self.count


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(len(ascii_lowercase))
        for eq in equations:
            if eq[1] == '=':
                x, y = ord(eq[0]) - ord('a'), ord(eq[-1]) - ord('a')
                uf.union(x, y)
        for eq in equations:
            if eq[1] == '!':
                x, y = ord(eq[0]) - ord('a'), ord(eq[-1]) - ord('a')
                if uf.connected(x, y):
                    return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
