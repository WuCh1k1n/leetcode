# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例： 
# 
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#  
#  Related Topics 字符串 回溯算法 
#  👍 1511 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(path: str, pairs: int, left: int, right: int):
            if left == right == pairs:
                res.append(path)
                return
            if left < pairs:
                backtrack(path + '(', pairs, left + 1, right)
            if right < left:
                backtrack(path + ')', pairs, left, right + 1)

        res = []
        backtrack('', n, 0, 0)
        return res
# leetcode submit region end(Prohibit modification and deletion)
