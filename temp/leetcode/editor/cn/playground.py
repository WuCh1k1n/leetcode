from typing import List, Optional
from collections import Counter, deque


# Definition for a Node.
class TreeNode(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def countDistinctElement(self, nums: List[int]) -> int:
        res = 0
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] > nums[right]:
                right -= 1
            elif nums[left] < nums[right]:
                left += 1
            else:
                left += 1
                right -= 1
            res += 1
        return res

    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res = 0
        n = len(s)
        counter = Counter()
        i = j = 0
        while j < n:
            counter[s[j]] += 1
            while len(counter) > 2:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    del counter[s[i]]
                i += 1
            res = max(res, j - i + 1)
            j += 1
        return res

    # 256
    def minCostOfPaintHouse(self, costs: List[List[int]]) -> int:
        n = len(costs)
        for i in range(1, n):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        return min(costs[-1])

    # 1490
    def mergeTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        mapping = {}
        q = deque([root])
        while q:
            node = q.popleft()
            mapping[node] = TreeNode(node.val)
            for child in node.children:
                mapping[child] = TreeNode(child.val)
                mapping[node].children.append(mapping[child])
                q.append(child)
        return mapping[root]


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstringTwoDistinct("eceba"))
    print(Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb"))
    # print(Solution().minCostOfPaintHouse([[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
