# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。 
# 
#  
# 
#  示例： 
# 
#  s = "leetcode"
# 返回 0
# 
# s = "loveleetcode"
# 返回 2
#  
# 
#  
# 
#  提示：你可以假定该字符串只包含小写字母。 
#  Related Topics 哈希表 字符串 
#  👍 348 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        frequency = collections.Counter(s)
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return i
        return -1
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().firstUniqChar("loveleetcode")
