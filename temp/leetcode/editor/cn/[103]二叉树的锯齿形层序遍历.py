# 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。 
# 
#  例如： 
# 给定二叉树 [3,9,20,null,null,15,7], 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回锯齿形层序遍历如下： 
# 
#  
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索 二叉树 
#  👍 462 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = list()
        if not root:
            return res
        q = [root]
        is_reversed = False
        while q:
            nodes, children = [], []
            for node in q:
                nodes.append(node.val)
                if node.left: children.append(node.left)
                if node.right: children.append(node.right)
            if is_reversed:
                nodes = nodes[::-1]
            res.append(nodes)
            q = children
            is_reversed = not is_reversed
        return res
# leetcode submit region end(Prohibit modification and deletion)
