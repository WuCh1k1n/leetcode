# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。 
# 
#  在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。 
# 
#  注意: 
# 假设字符串的长度不会超过 1010。 
# 
#  示例 1: 
# 
#  
# 输入:
# "abccccdd"
# 
# 输出:
# 7
# 
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
#  
#  Related Topics 哈希表 
#  👍 269 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        count = collections.Counter(s)
        for v in count.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
