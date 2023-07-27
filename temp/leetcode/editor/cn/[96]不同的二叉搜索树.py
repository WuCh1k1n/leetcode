# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：5
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 19 
#  
#  Related Topics 树 二叉搜索树 数学 动态规划 二叉树 
#  👍 1214 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 动态规划
    # def numTrees(self, n: int) -> int:
    #     G = [0] * (n + 1)
    #     G[0], G[1] = 1, 1
    #     for i in range(2, n + 1):
    #         for j in range(1, i + 1):
    #             G[i] += G[j - 1] * G[i - j]
    #     return G[n]

    # 数学
    # def numTrees(self, n: int) -> int:
    #     c = 1
    #     for i in range(0, n):
    #         c = c * 2 * (2 * i + 1) / (i + 2)
    #     return int(c)
    def numTrees(self, n: int) -> int:
        def helper(lo: int, hi: int) -> int:
            if lo > hi:
                return 1
            if memo[lo][hi] != 0:
                return memo[lo][hi]
            total = 0
            for i in range(lo, hi + 1):
                left = helper(lo, i - 1)
                right = helper(i + 1, hi)
                total += left * right
            memo[lo][hi] = total
            return total
        memo = [[0] * (n + 1) for _ in range(n + 1)]
        return helper(1, n)
# leetcode submit region end(Prohibit modification and deletion)
