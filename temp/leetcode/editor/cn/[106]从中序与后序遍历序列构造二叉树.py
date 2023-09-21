# 根据一棵树的中序遍历与后序遍历构造二叉树。 
# 
#  注意: 
# 你可以假设树中没有重复的元素。 
# 
#  例如，给出 
# 
#  中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3] 
# 
#  返回如下的二叉树： 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
#  Related Topics 树 深度优先搜索 数组 
#  👍 435 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import Optional, List


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def myBuildTree(inorder_left, inorder_right, postorder_left, postorder_right):
            if postorder_left > postorder_right:
                return None
            postorder_root = postorder_right
            inorder_root = index[postorder[postorder_root]]
            size_left_subtree = inorder_root - inorder_left
            root = TreeNode(postorder[postorder_root])
            root.left = myBuildTree(inorder_left, inorder_root - 1, postorder_left, postorder_left + size_left_subtree - 1)
            root.right = myBuildTree(inorder_root + 1, inorder_right, postorder_left + size_left_subtree, postorder_right - 1)
            return root
        n = len(postorder)
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
