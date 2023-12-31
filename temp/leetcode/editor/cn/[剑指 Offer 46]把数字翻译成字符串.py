# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可
# 能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。 
# 
#  
# 
#  示例 1: 
# 
#  输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi" 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= num < 231 
#  
#  👍 197 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def translateNum(self, num: int) -> int:
        def dfs(s):
            if not s:
                self.res += 1
                return
            dfs(s[1:])
            if len(s) > 1 and '10' <= s[:2] <= '25':
                dfs(s[2:])

        self.res = 0
        dfs(str(num))
        return self.res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution.translateNum(12258)
