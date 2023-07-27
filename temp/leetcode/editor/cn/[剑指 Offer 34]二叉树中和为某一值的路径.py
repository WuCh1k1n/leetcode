# 输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。 
# 
#  
# 
#  示例: 
# 给定如下二叉树，以及目标和 sum = 22， 
# 
#                5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
#  
# 
#  返回: 
# 
#  [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#  
# 
#  
# 
#  提示： 
# 
#  
#  节点总数 <= 10000 
#  
# 
#  注意：本题与主站 113 题相同：https://leetcode-cn.com/problems/path-sum-ii/ 
#  Related Topics 树 深度优先搜索 
#  👍 140 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def recur(root, tar):
            if not root:
                return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()

        res, path = [], []
        recur(root, sum)
        return res
# leetcode submit region end(Prohibit modification and deletion)
