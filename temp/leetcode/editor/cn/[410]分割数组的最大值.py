# 给定一个非负整数数组 nums 和一个整数 m ，你需要将这个数组分成 m 个非空的连续子数组。 
# 
#  设计一个算法使得这 m 个子数组各自和的最大值最小。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [7,2,5,10,8], m = 2
# 输出：18
# 解释：
# 一共有四种方法将 nums 分割为 2 个子数组。 其中最好的方式是将其分为 [7,2,5] 和 [10,8] 。
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,4,5], m = 2
# 输出：9
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,4,4], m = 3
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 1000 
#  0 <= nums[i] <= 106 
#  1 <= m <= min(50, nums.length) 
#  
#  Related Topics 二分查找 动态规划 
#  👍 430 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # # 动态规划
        # n = len(nums)
        # dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        # dp[0][0] = 0
        #
        # sub = [0]
        # for num in nums:
        #     sub.append(sub[-1] + num)
        #
        # for i in range(1, n + 1):
        #     for j in range(1, min(i, m) + 1):
        #         for k in range(i):
        #             dp[i][j] = min(dp[i][j], max(dp[k][j - 1], sub[i] - sub[k]))
        #
        # return dp[-1][-1]

        # 二分查找 + 贪心
        def check(x: int) -> bool:
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= m

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
# leetcode submit region end(Prohibit modification and deletion)
