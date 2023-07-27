"""
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果
 needle 不是 haystack 的一部分，则返回 -1 。 

 

 示例 1： 

 
输入：haystack = "sadbutsad", needle = "sad"
输出：0
解释："sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。
 

 示例 2： 

 
输入：haystack = "leetcode", needle = "leeto"
输出：-1
解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
 

 

 提示： 

 
 1 <= haystack.length, needle.length <= 10⁴ 
 haystack 和 needle 仅由小写英文字符组成 
 

 Related Topics 双指针 字符串 字符串匹配 👍 1847 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def KMP(s: str, p: str):
            nex = getNext(p)
            i = 0
            j = 0  # 分别是s和p的指针
            while i < len(s) and j < len(p):
                if j == -1 or s[i] == p[j]:  # j==-1是由于j=next[j]产生
                    i += 1
                    j += 1
                else:
                    j = nex[j]
            if j == len(p):  # j走到了末尾，说明匹配到了
                return i - j
            else:
                return -1

        def getNext(p: str):
            nex = [0] * (len(p) + 1)
            nex[0] = -1
            i = 0
            j = -1
            while i < len(p):
                if j == -1 or p[i] == p[j]:
                    i += 1
                    j += 1
                    nex[i] = j  # 这是最大的不同：记录next[i]
                else:
                    j = nex[j]

            return nex

        return KMP(haystack, needle)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().strStr("leetcode", "leeto")
