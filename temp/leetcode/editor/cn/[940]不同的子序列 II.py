"""
给定一个字符串 s，计算 s 的 不同非空子序列 的个数。因为结果可能很大，所以返回答案需要对 10^9 + 7 取余 。 

 字符串的 子序列 是经由原字符串删除一些（也可能不删除）字符但不改变剩余字符相对位置的一个新字符串。 

 
 例如，"ace" 是 "abcde" 的一个子序列，但 "aec" 不是。 
 

 

 示例 1： 

 
输入：s = "abc"
输出：7
解释：7 个不同的子序列分别是 "a", "b", "c", "ab", "ac", "bc", 以及 "abc"。
 

 示例 2： 

 
输入：s = "aba"
输出：6
解释：6 个不同的子序列分别是 "a", "b", "ab", "ba", "aa" 以及 "aba"。
 

 示例 3： 

 
输入：s = "aaa"
输出：3
解释：3 个不同的子序列分别是 "a", "aa" 以及 "aaa"。
 

 

 提示： 

 
 1 <= s.length <= 2000 
 s 仅由小写英文字母组成 
 

 

 Related Topics 字符串 动态规划 👍 239 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        ans, mod = 0, 10 ** 9 + 7
        n = len(s)
        # last[i]代表字母str(ord('a')+i)上次出现的位置
        last = [-1] * 26
        # f[i]代表以字母s[i]结束的子序列的个数
        f = [1] * n
        for i, ch in enumerate(s):
            for j in range(26):
                if last[j] != -1:
                    f[i] = (f[i] + f[last[j]]) % mod
            last[ord(ch) - ord("a")] = i
        for i in range(26):
            if last[i] != -1:
                ans = (ans + f[last[i]]) % mod
        return ans
# leetcode submit region end(Prohibit modification and deletion)
