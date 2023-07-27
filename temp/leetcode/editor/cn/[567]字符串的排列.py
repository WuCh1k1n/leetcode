# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。 
# 
#  换句话说，s1 的排列之一是 s2 的 子串 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
#  
# 
#  示例 2： 
# 
#  
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s1.length, s2.length <= 104 
#  s1 和 s2 仅包含小写字母 
#  
#  Related Topics 哈希表 双指针 字符串 滑动窗口 
#  👍 396 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def checkInclusion(self, pattern: str, string: str) -> bool:
        pattern_counter = collections.Counter(pattern)
        window_counter = collections.Counter(string[:len(pattern)])

        if window_counter == pattern_counter:
            return True

        window_start = 0
        for window_end, value in enumerate(string[len(pattern):]):
            window_counter[value] += 1
            window_start_char = string[window_start]
            window_counter[window_start_char] -= 1
            if window_counter[window_start_char] == 0:
                del window_counter[window_start_char]
            window_start += 1
            if window_counter == pattern_counter:
                return True

        return False
# leetcode submit region end(Prohibit modification and deletion)
