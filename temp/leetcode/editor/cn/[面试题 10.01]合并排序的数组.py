"""
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。 

 初始化 A 和 B 的元素数量分别为 m 和 n。 

 示例: 

 输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

输出: [1,2,2,3,5,6] 

 说明: 

 
 A.length == n + m 
 

 Related Topics 数组 双指针 排序 👍 171 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        i, j = m - 1, n - 1
        p = m + n - 1
        while i >= 0 and j >= 0:
            if A[i] >= B[j]:
                A[p] = A[i]
                i -= 1
            else:
                A[p] = B[j]
                j -= 1
            p -= 1
        if j >= 0:
            A[:p + 1] = B[:j + 1]
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
