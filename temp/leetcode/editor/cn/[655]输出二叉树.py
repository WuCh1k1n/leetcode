"""
给你一棵二叉树的根节点 root ，请你构造一个下标从 0 开始、大小为 m x n 的字符串矩阵 res ，用以表示树的 格式化布局 。构造此格式化布局矩阵需
要遵循以下规则： 

 
 树的 高度 为 height ，矩阵的行数 m 应该等于 height + 1 。 
 矩阵的列数 n 应该等于 2ʰᵉⁱᵍʰᵗ⁺¹ - 1 。 
 根节点 需要放置在 顶行 的 正中间 ，对应位置为 res[0][(n-1)/2] 。 
 对于放置在矩阵中的每个节点，设对应位置为 res[r][c] ，将其左子节点放置在 res[r+1][c-2ʰᵉⁱᵍʰᵗ⁻ʳ⁻¹] ，右子节点放置在 res[
r+1][c+2ʰᵉⁱᵍʰᵗ⁻ʳ⁻¹] 。 
 继续这一过程，直到树中的所有节点都妥善放置。 
 任意空单元格都应该包含空字符串 "" 。 
 

 返回构造得到的矩阵 res 。 

 

 

 示例 1： 
 
 
输入：root = [1,2]
输出：
[["","1",""],
 ["2","",""]]
 

 示例 2： 
 
 
输入：root = [1,2,3,null,4]
输出：
[["","","","1","","",""],
 ["","2","","","","3",""],
 ["","","4","","","",""]]
 

 

 提示： 

 
 树中节点数在范围 [1, 2¹⁰] 内 
 -99 <= Node.val <= 99 
 树的深度在范围 [1, 10] 内 
 

 Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 214 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1

        def dfs(node: Optional[TreeNode], row: int, col: int) -> None:
            if not node:
                return
            res[row][col] = str(node.val)
            dfs(node.left, row + 1, col - 2 ** (height - row - 1))
            dfs(node.right, row + 1, col + 2 ** (height - row - 1))

        height = get_height(root) - 1
        m = height + 1
        n = 2 ** (height + 1) - 1
        res = [[""] * n for _ in range(m)]
        dfs(root, 0, (n - 1) // 2)
        return res
# leetcode submit region end(Prohibit modification and deletion)
