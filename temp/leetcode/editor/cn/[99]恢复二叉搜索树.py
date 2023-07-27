# 给你二叉搜索树的根节点 root ，该树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。 
# 
#  进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用常数空间的解决方案吗？ 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [1,3,null,null,2]
# 输出：[3,1,null,null,2]
# 解释：3 不能是 1 左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [3,1,4,null,null,2]
# 输出：[2,1,4,null,null,3]
# 解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。 
# 
#  
# 
#  提示： 
# 
#  
#  树上节点的数目在范围 [2, 1000] 内 
#  -231 <= Node.val <= 231 - 1 
#  
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 
#  👍 500 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.firstNode = None
        self.secondNode = None
        self.preNode = TreeNode(float('-inf'))

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.firstNode is None and self.preNode.val >= root.val:
                self.firstNode = self.preNode
            if self.firstNode and self.preNode.val >= root.val:
                self.secondNode = root
            self.preNode = root
            inorder(root.right)

        inorder(root)
        self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val
# leetcode submit region end(Prohibit modification and deletion)
