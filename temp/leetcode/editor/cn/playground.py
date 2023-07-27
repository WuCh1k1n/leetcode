from typing import List
from collections import Counter


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
        res, n = 0, len(s)
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


if __name__ == '__main__':
    # print(Solution().countDistinctElement([4, 5, 6, 9, 7, 6, 5, 1]))
    # print(Solution().countDistinctElement([4, 5, 6, 9, 7, 8, 5, 1]))
    # print(Solution().countDistinctElement([4, 5, 6, 9, 7, 8, 3, 1]))

    print(Solution().lengthOfLongestSubstringTwoDistinct('eceba'))
    print(Solution().lengthOfLongestSubstringTwoDistinct('ccaabbb'))
    print(Solution().lengthOfLongestSubstringTwoDistinct('cacbbb'))
