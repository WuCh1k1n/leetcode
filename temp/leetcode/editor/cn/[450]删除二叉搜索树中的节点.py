# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的
# 根节点的引用。 
# 
#  一般来说，删除节点可分为两个步骤： 
# 
#  
#  首先找到需要删除的节点； 
#  如果找到了，删除它。 
#  
# 
#  说明： 要求算法时间复杂度为 O(h)，h 为树的高度。 
# 
#  示例: 
# 
#  
# root = [5,3,6,2,4,null,7]
# key = 3
# 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
# 
# 给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
# 
# 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
# 
#     5
#    / \
#   4   6
#  /     \
# 2       7
# 
# 另一个正确答案是 [5,2,6,null,4,null,7]。
# 
#     5
#    / \
#   2   6
#    \   \
#     4   7
#  
#  Related Topics 树 二叉搜索树 二叉树 
#  👍 481 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def successor(self, root: TreeNode) -> int:
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root: TreeNode) -> int:
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root
# leetcode submit region end(Prohibit modification and deletion)
