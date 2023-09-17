"""
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。 

 

 示例 1： 

 
输入:a = "11", b = "1"
输出："100" 

 示例 2： 

 
输入：a = "1010", b = "1011"
输出："10101" 

 

 提示： 

 
 1 <= a.length, b.length <= 10⁴ 
 a 和 b 仅由字符 '0' 或 '1' 组成 
 字符串如果不是 "0" ，就不含前导零 
 

 Related Topics 位运算 数学 字符串 模拟 👍 1097 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        while i >= 0 or j >= 0:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0
            _sum = x + y + carry
            res = str(_sum % 2) + res
            carry = _sum // 2
            i -= 1
            j -= 1
        if carry > 0:
            res = str(carry) + res
        return res
# leetcode submit region end(Prohibit modification and deletion)
