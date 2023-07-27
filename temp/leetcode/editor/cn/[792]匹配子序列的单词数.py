"""
给定字符串 s 和字符串数组 words, 返回 words[i] 中是s的子序列的单词个数 。 

 字符串的 子序列 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，而不改变其余字符的相对顺序。 

 
 例如， “ace” 是 “abcde” 的子序列。 
 

 

 示例 1: 

 
输入: s = "abcde", words = ["a","bb","acd","ace"]
输出: 3
解释: 有三个是 s 的子序列的单词: "a", "acd", "ace"。
 

 Example 2: 

 
输入: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
输出: 2
 

 

 提示: 

 
 1 <= s.length <= 5 * 10⁴ 
 1 <= words.length <= 5000 
 1 <= words[i].length <= 50 
 words[i]和 s 都只由小写字母组成。 
 


 Related Topics 字典树 哈希表 字符串 排序 👍 312 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        p = defaultdict(list)
        for i, w in enumerate(words):
            p[w[0]].append((i, 0))
        # print(p)
        ans = 0
        for c in s:
            q = p[c]
            p[c] = []
            for i, j in q:
                j += 1
                if j == len(words[i]):
                    ans += 1
                else:
                    p[words[i][j]].append((i, j))
        return ans
# leetcode submit region end(Prohibit modification and deletion)
