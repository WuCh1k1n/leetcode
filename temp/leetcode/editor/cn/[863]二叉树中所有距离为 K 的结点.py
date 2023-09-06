"""
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 k 。 

 返回到目标结点 target 距离为 k 的所有结点的值的列表。 答案可以以 任何顺序 返回。 

 

 
 

 示例 1： 

 

 
输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
输出：[7,4,1]
解释：所求结点为与目标结点（值为 5）距离为 2 的结点，值分别为 7，4，以及 1
 

 示例 2: 

 
输入: root = [1], target = 1, k = 3
输出: []
 

 

 提示: 

 
 节点数在 [1, 500] 范围内 
 0 <= Node.val <= 500 
 Node.val 中所有值 不同 
 目标结点 target 是树上的结点。 
 0 <= k <= 1000 
 

 

 Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 651 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque
from typing import Optional, List


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def build_graph(node: Optional[TreeNode]) -> None:
            if not node:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                build_graph(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                build_graph(node.right)
        ret = []
        graph = defaultdict(list)
        build_graph(root)
        q = deque([(target.val, 0)])
        visited = set()
        while q:
            val, distance = q.popleft()
            visited.add(val)
            if distance == k:
                ret.append(val)
            for next_val in graph[val]:
                if next_val not in visited and distance + 1 <= k:
                    q.append((next_val, distance + 1))
        return ret
# leetcode submit region end(Prohibit modification and deletion)
