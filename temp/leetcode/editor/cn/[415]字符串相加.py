# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。 
# 
#  你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：num1 = "11", num2 = "123"
# 输出："134"
#  
# 
#  示例 2： 
# 
#  
# 输入：num1 = "456", num2 = "77"
# 输出："533"
#  
# 
#  示例 3： 
# 
#  
# 输入：num1 = "0", num2 = "0"
# 输出："0"
#  
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= num1.length, num2.length <= 104 
#  num1 和num2 都只包含数字 0-9 
#  num1 和num2 都不包含任何前导零 
#  
#  Related Topics 数学 字符串 模拟 
#  👍 461 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().addStrings("456", "77"))
