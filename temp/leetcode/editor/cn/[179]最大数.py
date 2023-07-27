# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。 
# 
#  注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [10,2]
# 输出："210" 
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出："1"
#  
# 
#  示例 4： 
# 
#  
# 输入：nums = [10]
# 输出："10"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 10⁹ 
#  
#  Related Topics 贪心 字符串 排序 👍 821 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = map(str, nums)

        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b > b + a:
                return 1
            else:
                return -1

        strs = sorted(strs, key=functools.cmp_to_key(cmp), reverse=True)
        return ''.join(strs) if strs[0] != '0' else '0'
# leetcode submit region end(Prohibit modification and deletion)