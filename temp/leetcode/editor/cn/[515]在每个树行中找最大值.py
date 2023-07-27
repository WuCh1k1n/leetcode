# 您需要在二叉树的每一行中找到最大的值。 
# 
#  示例： 
# 
#  
# 输入: 
# 
#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 
# 
# 输出: [1, 3, 9]
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 119 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        ans = []
        queue = [root]
        while queue:
            max_val = float('-inf')
            nodes = []
            for node in queue:
                max_val = max(max_val, node.val)
                if node.left: nodes.append(node.left)
                if node.right: nodes.append(node.right)
            ans.append(max_val)
            queue = nodes
        return ans
# leetcode submit region end(Prohibit modification and deletion)
