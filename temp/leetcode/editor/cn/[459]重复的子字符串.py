# 给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abab"
# 输出: true
# 解释: 可由子串 "ab" 重复两次构成。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "aba"
# 输出: false
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "abcabcabcabc"
# 输出: true
# 解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)
#  
# 
#  
# 
#  提示： 
# 
#  
# 
#  
#  1 <= s.length <= 10⁴ 
#  s 由小写英文字母组成 
#  
#  Related Topics 字符串 字符串匹配 👍 676 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                if all(s[j] == s[j - i] for j in range(i, n)):
                    return True
        return False
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().repeatedSubstringPattern("abcabcabcabc")
