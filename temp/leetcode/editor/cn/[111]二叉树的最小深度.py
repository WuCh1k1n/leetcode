# 给定一个二叉树，找出其最小深度。 
# 
#  最小深度是从根节点到最近叶子节点的最短路径上的节点数量。 
# 
#  说明：叶子节点是指没有子节点的节点。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [2,null,3,null,4,null,5,null,6]
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数的范围在 [0, 105] 内 
#  -1000 <= Node.val <= 1000 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 426 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root: TreeNode) -> int:
        # 递归
        if not root:
            return 0
        left_height = self.minDepth(root.left)
        right_height = self.minDepth(root.right)
        return left_height + right_height + 1 if not root.left or not root.right else min(left_height, right_height) + 1

        # BFS
        # if not root: return 0
        # queue = [root]
        # height = 1
        # while queue:
        #     nodes = []
        #     for node in queue:
        #         if not node.left and not node.right:
        #             return height
        #         if node.left:
        #             nodes.append(node.left)
        #         if node.right:
        #             nodes.append(node.right)
        #     height += 1
        #     queue = nodes
        # return height
# leetcode submit region end(Prohibit modification and deletion)
