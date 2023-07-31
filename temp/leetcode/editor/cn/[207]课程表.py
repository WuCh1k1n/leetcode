"""
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。 

 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如
果要学习课程 ai 则 必须 先学习课程 bi 。 

 
 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。 
 

 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。 

 

 示例 1： 

 
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。 

 示例 2： 

 
输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。 

 

 提示： 

 
 1 <= numCourses <= 10⁵ 
 0 <= prerequisites.length <= 5000 
 prerequisites[i].length == 2 
 0 <= ai, bi < numCourses 
 prerequisites[i] 中的所有课程对 互不相同 
 

 Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序 👍 1525 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # outdegrees[i] 记录课程 i 的出度节点
        outdegrees = collections.defaultdict(list)
        # indegree_num[i] 记录课程 i 的入度边数
        indegree_num = [0] * numCourses
        for p in prerequisites:
            outdegrees[p[1]].append(p[0])
            indegree_num[p[0]] += 1
        # 队列 q 中的课程没有入度边数，可以作为起点直接修读
        q = collections.deque(c for c in range(numCourses) if indegree_num[c] == 0)
        visited = 0
        while q:
            visited += 1
            start = q.popleft()
            for nxt in outdegrees[start]:
                indegree_num[nxt] -= 1
                if indegree_num[nxt] == 0:
                    # 课程 nxt 入度课程都已经访问过，可以修读了
                    q.append(nxt)
        return visited == numCourses
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().canFinish(2, [[1, 0]])
