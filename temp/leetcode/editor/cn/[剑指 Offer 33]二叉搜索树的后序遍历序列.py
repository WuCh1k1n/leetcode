# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。 
# 
#  
# 
#  参考以下这颗二叉搜索树： 
# 
#       5
#     / \
#    2   6
#   / \
#  1   3 
# 
#  示例 1： 
# 
#  输入: [1,6,3,2,5]
# 输出: false 
# 
#  示例 2： 
# 
#  输入: [1,3,2,6,5]
# 输出: true 
# 
#  
# 
#  提示： 
# 
#  
#  数组长度 <= 1000 
#  
#  👍 203 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        # 递归分治
        # def recur(i, j):
        #     if i >= j: return True
        #     p = i
        #     while postorder[p] < postorder[j]: p += 1
        #     m = p
        #     while postorder[p] > postorder[j]: p += 1
        #     return p == j and recur(i, m - 1) and recur(m, j - 1)
        # return recur(0, len(postorder) - 1)

        # 辅助单调栈
        stack, root = [], float("+inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root:
                return False
            while stack and postorder[i] < stack[-1]:
                root = stack.pop()
            stack.append(postorder[i])
        return True
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    Solution().verifyPostorder([1, 3, 2, 6, 5])
