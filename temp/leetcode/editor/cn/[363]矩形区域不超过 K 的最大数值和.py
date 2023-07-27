# 给定一个非空二维矩阵 matrix 和一个整数 k，找到这个矩阵内部不大于 k 的最大矩形和。 
# 
#  示例: 
# 
#  输入: matrix = [[1,0,1],[0,-2,3]], k = 2
# 输出: 2 
# 解释: 矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
#  
# 
#  说明： 
# 
#  
#  矩阵内的矩形区域面积必须大于 0。 
#  如果行数远大于列数，你将如何解答呢？ 
#  
#  Related Topics 队列 二分查找 动态规划 
#  👍 154 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # # 动态规划
        # rows, columns = len(matrix), len(matrix[0])
        # max_sum = float('-inf')
        # dp = [[[[0] * (columns + 1) for _ in range(rows + 1)] for _ in range(columns + 1)] for _ in range(rows + 1)]
        # for i1 in range(1, rows + 1):
        #     for j1 in range(1, columns + 1):
        #         dp[i1][j1][i1][j1] = matrix[i1 - 1][j1 - 1]
        #         for i2 in range(i1, rows + 1):
        #             for j2 in range(j1, columns + 1):
        #                 dp[i1][j1][i2][j2] = dp[i1][j1][i2 - 1][j2] + dp[i1][j1][i2][j2 - 1] - dp[i1][j1][i2 - 1][
        #                     j2 - 1] + matrix[i2 - 1][j2 - 1]
        #                 if dp[i1][j1][i2][j2] <= k:
        #                     max_sum = max(max_sum, dp[i1][j1][i2][j2])
        # return max_sum

        # # 动态规划 + 状态压缩
        # rows, columns = len(matrix), len(matrix[0])
        # max_sum = float('-inf')
        # for i1 in range(1, rows + 1):
        #     for j1 in range(1, columns + 1):
        #         dp = [[0] * (columns + 1) for _ in range(rows + 1)]
        #         dp[i1][j1] = matrix[i1 - 1][j1 - 1]
        #         for i2 in range(i1, rows + 1):
        #             for j2 in range(j1, columns + 1):
        #                 dp[i2][j2] = dp[i2 - 1][j2] + dp[i2][j2 - 1] - dp[i2 - 1][j2 - 1] + matrix[i2 - 1][j2 - 1]
        #                 if dp[i2][j2] <= k:
        #                     max_sum = max(max_sum, dp[i2][j2])
        # return max_sum

        # 前缀和 + 二分
        import bisect
        row = len(matrix)
        col = len(matrix[0])
        res = float('-inf')
        for left in range(col):
            # 以 left 为左边界，每行的总和
            _sum = [0] * row
            for right in range(left, col):
                for j in range(row):
                    _sum[j] += matrix[j][right]
                # 在 left，right 为边界下的矩阵，求不超过 K 的最大数值和
                arr = [0]
                cur = 0
                for tmp in _sum:
                    cur += tmp
                    # 二分法
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr):
                        res = max(cur - arr[loc], res)
                    # 把累加和加入
                    bisect.insort(arr, cur)
        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2)
