# 根据一棵树的前序遍历与中序遍历构造二叉树。 
# 
#  注意: 
# 你可以假设树中没有重复的元素。 
# 
#  例如，给出 
# 
#  前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7] 
# 
#  返回如下的二叉树： 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
#  Related Topics 树 深度优先搜索 数组 
#  👍 823 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def builder(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int) -> TreeNode:
            if preorder_left > preorder_right:
                return
            root_val = preorder[preorder_left]
            inorder_root = inorder.index(root_val)
            left_subtree_size = inorder_root - inorder_left
            root = TreeNode(root_val)
            root.left = builder(preorder_left + 1, preorder_left + left_subtree_size, inorder_left, inorder_root - 1)
            root.right = builder(preorder_left + left_subtree_size + 1, preorder_right, inorder_root + 1, inorder_right)
            return root

        return builder(0, len(preorder) - 1, 0, len(inorder))
# leetcode submit region end(Prohibit modification and deletion)
