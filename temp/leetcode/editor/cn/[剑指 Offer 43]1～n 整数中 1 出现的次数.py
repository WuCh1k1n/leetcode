# 输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。 
# 
#  例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 12
# 输出：5
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 13
# 输出：6 
# 
#  
# 
#  限制： 
# 
#  
#  1 <= n < 2^31 
#  
# 
#  注意：本题与主站 233 题相同：https://leetcode-cn.com/problems/number-of-digit-one/ 
#  Related Topics 数学 
#  👍 137 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0: return 0
        if n < 10: return 1
        last = int(str(n)[1:])
        power = 10 ** (len(str(n)) - 1)
        high = int(str(n)[0])
        if high == 1:
            return last + 1 + self.countDigitOne(power - 1) + self.countDigitOne(last)
        else:
            return power + high * self.countDigitOne(power - 1) + self.countDigitOne(last)
# leetcode submit region end(Prohibit modification and deletion)
