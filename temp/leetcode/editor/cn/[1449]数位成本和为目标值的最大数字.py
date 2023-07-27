"""
给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数： 

 
 给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。 
 总成本必须恰好等于 target 。 
 添加的数位中没有数字 0 。 
 

 由于答案可能会很大，请你以字符串形式返回。 

 如果按照上述要求无法得到任何整数，请你返回 "0" 。 

 

 示例 1： 

 
输入：cost = [4,3,2,5,6,7,2,5,5], target = 9
输出："7772"
解释：添加数位 '7' 的成本为 2 ，添加数位 '2' 的成本为 3 。所以 "7772" 的代价为 2*3+ 3*1 = 9 。 "977" 也是满足要求的
数字，但 "7772" 是较大的数字。
 数字     成本
  1  ->   4
  2  ->   3
  3  ->   2
  4  ->   5
  5  ->   6
  6  ->   7
  7  ->   2
  8  ->   5
  9  ->   5
 

 示例 2： 

 
输入：cost = [7,6,5,5,5,6,8,7,8], target = 12
输出："85"
解释：添加数位 '8' 的成本是 7 ，添加数位 '5' 的成本是 5 。"85" 的成本为 7 + 5 = 12 。
 

 示例 3： 

 
输入：cost = [2,4,6,2,4,6,4,4,4], target = 5
输出："0"
解释：总成本是 target 的条件下，无法生成任何整数。
 

 示例 4： 

 
输入：cost = [6,10,15,40,40,40,40,40,40], target = 47
输出："32211"
 

 

 提示： 

 
 cost.length == 9 
 1 <= cost[i] <= 5000 
 1 <= target <= 5000 
 

 Related Topics 数组 动态规划 👍 163 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # dp[i+1][j]=x，从前 i 个数的成本组成 j 的最长数位为 x
        dp = [[float("-inf")] * (target + 1) for _ in range(10)]
        # where[i+1][j]=y，前 i 个数的成本组成 j 从 y 转移过来
        where = [[0] * (target + 1) for _ in range(10)]
        dp[0][0] = 0

        for i, c in enumerate(cost):
            for j in range(target + 1):
                if j < c:
                    dp[i + 1][j] = dp[i][j]
                    where[i + 1][j] = j
                else:
                    if dp[i][j] > dp[i + 1][j - c] + 1:
                        dp[i + 1][j] = dp[i][j]
                        where[i + 1][j] = j
                    else:
                        dp[i + 1][j] = dp[i + 1][j - c] + 1
                        where[i + 1][j] = j - c

        if dp[9][target] < 0:
            return "0"

        ans = list()
        i, j = 9, target
        while i > 0:
            if j == where[i][j]:
                i -= 1
            else:
                ans.append(str(i))
                j = where[i][j]

        return "".join(ans)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().largestNumber([4, 3, 2, 5, 6, 7, 2, 5, 5], 9)
