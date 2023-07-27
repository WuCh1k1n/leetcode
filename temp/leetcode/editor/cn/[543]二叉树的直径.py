# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。 
# 
#  
# 
#  示例 : 
# 给定二叉树 
# 
#            1
#          / \
#         2   3
#        / \     
#       4   5    
#  
# 
#  返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。 
# 
#  
# 
#  注意：两结点之间的路径长度是以它们之间边的数目表示。 
#  Related Topics 树 深度优先搜索 二叉树 👍 833 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_path = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.max_path

    def dfs(self, root: TreeNode) -> int:
        if not root:
            return 0
        l, r = self.dfs(root.left), self.dfs(root.right)
        self.max_path = max(self.max_path, l + r)
        return max(l, r) + 1
# leetcode submit region end(Prohibit modification and deletion)
