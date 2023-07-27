# 给你一个整数 n ，请你在无限的整数序列 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...] 中找出并返回第 n 位上的数字。
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：3
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 11
# 输出：0
# 解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2³¹ - 1 
#  第 n 位上的数字是按计数单位（digit）从前往后数的第 n 个数，参见 示例 2 。 
#  
#  Related Topics 数学 二分查找 👍 287 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findNthDigit(self, n: int) -> int:
        d, count = 1, 9
        while n > d * count:
            n -= d * count
            d += 1
            count *= 10
        index = n - 1
        start = 10 ** (d - 1)
        num = start + index // d
        digitIndex = index % d
        return num // 10 ** (d - digitIndex - 1) % 10
# leetcode submit region end(Prohibit modification and deletion)
