# 给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符： 
# 
#  
#  'A' : Absent，缺勤 
#  'L' : Late，迟到 
#  'P' : Present，到场 
#  
# 
#  如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。 
# 
#  你需要根据这个学生的出勤记录判断他是否会被奖赏。 
# 
#  示例 1: 
# 
#  输入: "PPALLP"
# 输出: True
#  
# 
#  示例 2: 
# 
#  输入: "PPALLL"
# 输出: False
#  
#  Related Topics 字符串 
#  👍 67 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # a_num, l_num = 0, 0
        # for a in s:
        #     if a == "A":
        #         a_num += 1
        #         if a_num >= 2: return False
        #         l_num = 0
        #     elif a == "L":
        #         l_num += 1
        #         if l_num >= 3: return False
        #     else:
        #         l_num = 0
        # return True

        count, i = 0, 0
        while i < len(s) and count < 2:
            if s[i] == 'A':
                count += 1
            i += 1
        return count < 2 and s.find('LLL') < 0
# leetcode submit region end(Prohibit modification and deletion)
