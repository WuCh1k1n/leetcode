# 返回 s 字典序最小的子序列，该子序列包含 s 的所有不同字符，且只包含一次。 
# 
#  注意：该题与 316 https://leetcode.com/problems/remove-duplicate-letters/ 相同 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "bcabc"
# 输出："abc"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbacdcbc"
# 输出："acdb" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 由小写英文字母组成 
#  
#  Related Topics 栈 贪心 字符串 单调栈 
#  👍 109 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        remaining_cnt = Counter(s)
        for c in s:
            if c not in stack:
                while stack and stack[-1] > c and remaining_cnt[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            remaining_cnt[c] -= 1
        return ''.join(stack)
# leetcode submit region end(Prohibit modification and deletion)
