# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。 
# 
#  注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct
# -characters 相同 
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
#  1 <= s.length <= 104 
#  s 由小写英文字母组成 
#  
#  Related Topics 栈 贪心 字符串 单调栈 
#  👍 577 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        remaining_cnt = Counter(s)
        for digit in s:
            if digit not in stack:
                while stack and stack[-1] > digit and remaining_cnt[stack[-1]] > 0:
                    stack.pop()
                stack.append(digit)
            remaining_cnt[digit] -= 1
        return ''.join(stack)
# leetcode submit region end(Prohibit modification and deletion)
