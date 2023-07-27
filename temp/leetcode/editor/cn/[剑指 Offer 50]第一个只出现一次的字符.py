# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。 
# 
#  示例: 
# 
#  s = "abaccdeff"
# 返回 "b"
# 
# s = "" 
# 返回 " "
#  
# 
#  
# 
#  限制： 
# 
#  0 <= s 的长度 <= 50000 
#  Related Topics 哈希表 
#  👍 77 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> str:
        count = Counter(s)
        for key in count.keys():
            if count[key] == 1:
                return key
        return ' '
# leetcode submit region end(Prohibit modification and deletion)
