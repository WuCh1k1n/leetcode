# 给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。 
# 
#  注意：1 ≤ k ≤ n ≤ 10⁹。 
# 
#  示例 : 
# 
#  
# 输入:
# n: 13   k: 2
# 
# 输出:
# 10
# 
# 解释:
# 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
#  
#  Related Topics 字典树 👍 250 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # 十叉树，返回在字典序序列中[n1, n2)有多少个数字
        def cal_steps(n1: int, n2: int) -> int:
            steps = 0
            while n1 <= n:
                steps += min(n2, n + 1) - n1
                n1 *= 10
                n2 *= 10
            return steps

        cur = 1
        k -= 1
        while k > 0:
            steps = cal_steps(cur, cur + 1)
            if steps <= k:
                k -= steps
                cur += 1
            else:
                k -= 1
                cur *= 10
        return cur
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().findKthNumber(13, 5)
