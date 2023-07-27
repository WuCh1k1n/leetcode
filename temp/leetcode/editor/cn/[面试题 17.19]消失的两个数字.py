"""
给定一个数组，包含从 1 到 N 所有的整数，但其中缺了两个数字。你能在 O(N) 时间内只用 O(1) 的空间找到它们吗？ 

 以任意顺序返回这两个数字均可。 

 示例 1: 

 输入: [1]
输出: [2,3] 

 示例 2: 

 输入: [2,3]
输出: [1,4] 

 提示： 

 
 nums.length <= 30000 
 

 Related Topics 位运算 数组 哈希表 👍 151 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        xorsum = 0
        n = len(nums) + 2
        for num in nums:
            xorsum ^= num
        for i in range(1, n + 1):
            xorsum ^= i
        lsb = xorsum ^ xorsum - 1
        type1 = type2 = 0
        for num in nums:
            if num & lsb:
                type1 ^= num
            else:
                type2 ^= num
        for i in range(1, n + 1):
            if i & lsb:
                type1 ^= i
            else:
                type2 ^= i
        return [type1, type2]
# leetcode submit region end(Prohibit modification and deletion)
