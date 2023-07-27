"""
给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。 

 示例 1 : 

 
输入: 2736
输出: 7236
解释: 交换数字2和数字7。
 

 示例 2 : 

 
输入: 9973
输出: 9973
解释: 不需要交换。
 

 注意: 

 
 给定数字的范围是 [0, 10⁸] 
 

 Related Topics 贪心 数学 👍 308 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def maximumSwap(self, num: int) -> int:
    #     ans = num
    #     s = list(str(num))
    #     for i in range(len(s)):
    #         for j in range(i):
    #             s[i], s[j] = s[j], s[i]
    #             ans = max(ans, int(''.join(s)))
    #             s[i], s[j] = s[j], s[i]
    #     return ans

    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        max_idx = n - 1
        idx1 = idx2 = -1
        for i in range(n - 1, -1, -1):
            if s[i] > s[max_idx]:
                max_idx = i
            elif s[i] < s[max_idx]:
                idx1, idx2 = i, max_idx
        if idx1 < 0:
            return num
        s[idx1], s[idx2] = s[idx2], s[idx1]
        return int(''.join(s))
# leetcode submit region end(Prohibit modification and deletion)
