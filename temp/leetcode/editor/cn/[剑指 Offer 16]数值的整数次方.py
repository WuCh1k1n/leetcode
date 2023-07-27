# 实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数
# 问题。 
# 
#  
# 
#  示例 1: 
# 
#  输入: 2.00000, 10
# 输出: 1024.00000
#  
# 
#  示例 2: 
# 
#  输入: 2.10000, 3
# 输出: 9.26100
#  
# 
#  示例 3: 
# 
#  输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25 
# 
#  
# 
#  说明: 
# 
#  
#  -100.0 < x < 100.0 
#  n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。 
#  
# 
#  注意：本题与主站 50 题相同：https://leetcode-cn.com/problems/powx-n/ 
#  Related Topics 递归 
#  👍 123 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(num):
            if num == 0:
                return 1
            y = quickMul(num // 2)
            return y * y if num % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
# leetcode submit region end(Prohibit modification and deletion)
