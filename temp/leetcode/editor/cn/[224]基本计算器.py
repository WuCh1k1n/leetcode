"""
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。 

 注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。 

 

 示例 1： 

 
输入：s = "1 + 1"
输出：2
 

 示例 2： 

 
输入：s = " 2-1 + 2 "
输出：3
 

 示例 3： 

 
输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23
 

 

 提示： 

 
 1 <= s.length <= 3 * 10⁵ 
 s 由数字、'+'、'-'、'('、')'、和 ' ' 组成 
 s 表示一个有效的表达式 
 '+' 不能用作一元运算(例如， "+1" 和 "+(2 + 3)" 无效) 
 '-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 是有效的) 
 输入中不存在两个连续的操作符 
 每个数字和运行的计算将适合于一个有符号的 32位 整数 
 

 Related Topics 栈 递归 数学 字符串 👍 859 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        i, n = 0, len(s)
        sign, ops = 1, [1]
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                res += sign * num
        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
