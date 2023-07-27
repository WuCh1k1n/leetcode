# 给定一个二叉树，我们在树的节点上安装摄像头。 
# 
#  节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。 
# 
#  计算监控树的所有节点所需的最小摄像头数量。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：[0,0,null,0,0]
# 输出：1
# 解释：如图所示，一台摄像头足以监控所有节点。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：[0,0,null,0,null,0,null,null,0]
# 输出：2
# 解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。
#  
# 
#  
# 提示： 
# 
#  
#  给定树的节点数的范围是 [1, 1000]。 
#  每个节点的值都是 0。 
#  
#  Related Topics 树 深度优先搜索 动态规划 二叉树 👍 408 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(root: TreeNode) -> List[int]:
            # 状态 a：root 必须放置摄像头的情况下，覆盖整棵树需要的摄像头数目。
            # 状态 b：覆盖整棵树需要的摄像头数目，无论 root 是否放置摄像头。
            # 状态 c：覆盖两棵子树需要的摄像头数目，无论节点 root 本身是否被监控到。
            if not root:
                return [float('inf'), 0, 0]
            la, lb, lc = dfs(root.left)
            ra, rb, rc = dfs(root.right)
            a = lc + rc + 1
            b = min(a, la + rb, lb + ra)
            c = min(a, lb + rb)
            return [a, b, c]
        a, b, c = dfs(root)
        return b
# leetcode submit region end(Prohibit modification and deletion)
