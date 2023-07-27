# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。 
# 
#  字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。 
# 
#  说明： 
# 
#  
#  字母异位词指字母相同，但排列不同的字符串。 
#  不考虑答案输出的顺序。 
#  
# 
#  示例 1: 
# 
#  
# 输入:
# s: "cbaebabacd" p: "abc"
# 
# 输出:
# [0, 6]
# 
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#  
# 
#  示例 2: 
# 
#  
# 输入:
# s: "abab" p: "ab"
# 
# 输出:
# [0, 1, 2]
# 
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
#  
#  Related Topics 哈希表 
#  👍 463 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, string: str, pattern: str) -> List[int]:
        ans = []
        string_cnt = Counter(string[:len(pattern)])
        pattern_cnt = Counter(pattern)
        if string_cnt == pattern_cnt:
            ans.append(0)

        for i, ch in enumerate(string[len(pattern):], len(pattern)):
            string_cnt[ch] += 1
            string_cnt[string[i - len(pattern)]] -= 1
            if string_cnt[string[i - len(pattern)]] == 0:
                del string_cnt[string[i - len(pattern)]]
            if string_cnt == pattern_cnt:
                ans.append(i - len(pattern) + 1)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().findAnagrams("cbaebabacd", "abc")
