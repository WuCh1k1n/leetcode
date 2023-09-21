"""
给定两个整数数组，preorder 和 postorder ，其中 preorder 是一个具有 无重复 值的二叉树的前序遍历，postorder 是同一棵树的
后序遍历，重构并返回二叉树。 

 如果存在多个答案，您可以返回其中 任何 一个。 

 

 示例 1： 

 

 
输入：preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
输出：[1,2,3,4,5,6,7]
 

 示例 2: 

 
输入: preorder = [1], postorder = [1]
输出: [1]
 

 

 提示： 

 
 1 <= preorder.length <= 30 
 1 <= preorder[i] <= preorder.length 
 preorder 中所有值都 不同 
 postorder.length == preorder.length 
 1 <= postorder[i] <= postorder.length 
 postorder 中所有值都 不同 
 保证 preorder 和 postorder 是同一棵二叉树的前序遍历和后序遍历 
 

 Related Topics 树 数组 哈希表 分治 二叉树 👍 325 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(preorder_left: int, preorder_right: int, postorder_left: int, postorder_right: int) -> Optional[TreeNode]:
            if preorder_left > preorder_right:
                return None
            root_val = preorder[preorder_left]
            root = TreeNode(root_val)
            if preorder_left == preorder_right:
                return root
            left_root_val = preorder[preorder_left + 1]
            left_subtree_size = postorder.index(left_root_val) - postorder_left + 1
            root.left = build(preorder_left + 1, preorder_left + left_subtree_size, postorder_left, postorder_left + left_subtree_size - 1)
            root.right = build(preorder_left + left_subtree_size + 1, preorder_right, postorder_left + left_subtree_size, postorder_right - 1)
            return root
        return build(0, len(preorder) - 1, 0, len(postorder) - 1)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # Solution().constructFromPrePost([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1])
    Solution().constructFromPrePost([2, 1], [1, 2])
