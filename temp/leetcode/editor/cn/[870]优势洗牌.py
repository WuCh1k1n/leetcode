# 给定两个大小相等的数组 A 和 B，A 相对于 B 的优势可以用满足 A[i] > B[i] 的索引 i 的数目来描述。 
# 
#  返回 A 的任意排列，使其相对于 B 的优势最大化。 
# 
#  
# 
#  示例 1： 
# 
#  输入：A = [2,7,11,15], B = [1,10,4,11]
# 输出：[2,11,7,15]
#  
# 
#  示例 2： 
# 
#  输入：A = [12,24,8,32], B = [13,25,32,11]
# 输出：[24,32,8,12]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length = B.length <= 10000 
#  0 <= A[i] <= 10^9 
#  0 <= B[i] <= 10^9 
#  
#  Related Topics 贪心 数组 排序 
#  👍 139 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        sortedA = sorted(A)
        sortedB = sorted(B)

        # assigned[b] = list of a that are assigned to beat b
        # remaining = list of a that are not assigned to any b
        assigned = {b: [] for b in B}
        remaining = []

        # populate (assigned, remaining) appropriately
        # sortedB[j] is always the smallest unassigned element in B
        j = 0
        for a in sortedA:
            if a > sortedB[j]:
                assigned[sortedB[j]].append(a)
                j += 1
            else:
                remaining.append(a)

        # Reconstruct the answer from annotations (assigned, remaining)
        return [assigned[b].pop() if assigned[b] else remaining.pop() for b in B]
# leetcode submit region end(Prohibit modification and deletion)
