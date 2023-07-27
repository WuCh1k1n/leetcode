# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。 
# 
#  单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使
# 用。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l"
# ,"v"]], words = ["oath","pea","eat","rain"]
# 输出：["eat","oath"]
#  
# 
#  示例 2： 
# 
#  
# 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == board.length 
#  n == board[i].length 
#  1 <= m, n <= 12 
#  board[i][j] 是一个小写英文字母 
#  1 <= words.length <= 3 * 104 
#  1 <= words[i].length <= 10 
#  words[i] 由小写英文字母组成 
#  words 中的所有字符串互不相同 
#  
#  Related Topics 字典树 回溯算法 
#  👍 321 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node['#'] = True

        def search(i, j, node, pre, visited):
            if '#' in node:
                res.add(pre)
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                _i, _j = i + di, j + dj
                if 0 <= _i < h and 0 <= _j < w and board[_i][_j] in node and (_i, _j) not in visited:
                    search(_i, _j, node[board[_i][_j]], pre + board[_i][_j], visited | {(_i, _j)})

        res, h, w = set(), len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                if board[i][j] in trie:
                    search(i, j, trie[board[i][j]], board[i][j], {(i, j)})
        return list(res)
# leetcode submit region end(Prohibit modification and deletion)
