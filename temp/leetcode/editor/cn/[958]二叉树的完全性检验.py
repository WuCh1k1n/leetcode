# 给定一个二叉树，确定它是否是一个完全二叉树。 
# 
#  百度百科中对完全二叉树的定义如下： 
# 
#  若设二叉树的深度为 h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。（注：
# 第 h 层可能包含 1~ 2ʰ 个节点。） 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：[1,2,3,4,5,6]
# 输出：true
# 解释：最后一层前的每一层都是满的（即，结点值为 {1} 和 {2,3} 的两层），且最后一层中的所有结点（{4,5,6}）都尽可能地向左。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：[1,2,3,4,5,null,7]
# 输出：false
# 解释：值为 7 的结点没有尽可能靠向左侧。
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中将会有 1 到 100 个结点。 
#  
#  Related Topics 树 广度优先搜索 二叉树 👍 157 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node:
                nodes.append((node.left, v * 2))
                nodes.append((node.right, v * 2 + 1))
        print(nodes[-1][1])
        return nodes[-1][1] == len(nodes)
# leetcode submit region end(Prohibit modification and deletion)
