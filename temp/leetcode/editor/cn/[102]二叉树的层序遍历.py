# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。 
# 
#  
# 
#  示例： 
# 二叉树：[3,9,20,null,null,15,7], 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层序遍历结果： 
# 
#  
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索 
#  👍 745 👎 0

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def levelOrder(self, root: TreeNode) -> List[List[TreeNode]]:
        res = list()
        if not root:
            return res
        q = [root]
        while q:
            nodes, children = list(), list()
            for node in q:
                nodes.append(node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            res.append(nodes)
            q = children
        return res
# leetcode submit region end(Prohibit modification and deletion)
