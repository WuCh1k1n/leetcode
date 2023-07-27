# 给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。 
# 
#  注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 12
# 输出：21
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 21
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2³¹ - 1 
#  
#  Related Topics 数学 双指针 字符串 👍 178 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num = list(str(n))
        i = len(num) - 2
        while i >= 0 and num[i] >= num[i + 1]:
            i -= 1
        if i >= 0:
            j = len(num) - 1
            while j >= i and num[j] <= num[i]:
                j -= 1
            num[i], num[j] = num[j], num[i]
        else:
            return -1

        l, r = i + 1, len(num) - 1
        while l < r:
            num[l], num[r] = num[r], num[l]
            l += 1
            r -= 1
        res = int(''.join(num))
        return res if res <= 2 ** 31 - 1 else -1
# leetcode submit region end(Prohibit modification and deletion)
