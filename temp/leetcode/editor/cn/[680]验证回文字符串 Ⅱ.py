# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。 
# 
#  示例 1: 
# 
#  
# 输入: "aba"
# 输出: True
#  
# 
#  示例 2: 
# 
#  
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
#  
# 
#  注意: 
# 
#  
#  字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。 
#  
#  Related Topics 字符串 
#  👍 317 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validPalindrome(self, s: str) -> bool:

        def checkPalindrome(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return checkPalindrome(low + 1, high) or checkPalindrome(low, high - 1)
        return True
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().validPalindrome("abca"))
