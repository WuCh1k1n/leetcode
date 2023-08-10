"""
给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。 

 返回 你可以获得的最大乘积 。 

 

 示例 1: 

 
输入: n = 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。 

 示例 2: 

 
输入: n = 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。 

 

 提示: 

 
 2 <= n <= 58 
 

 Related Topics 数学 动态规划 👍 1244 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
