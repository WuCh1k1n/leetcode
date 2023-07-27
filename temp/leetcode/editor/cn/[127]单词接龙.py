# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
#  
# 
#  
#  每次转换只能改变一个字母。 
#  转换过程中的中间单词必须是字典中的单词。 
#  
# 
#  说明: 
# 
#  
#  如果不存在这样的转换序列，返回 0。 
#  所有单词具有相同的长度。 
#  所有单词只由小写字母组成。 
#  字典中不存在重复的单词。 
#  你可以假设 beginWord 和 endWord 是非空的，且二者不相同。 
#  
# 
#  示例 1: 
# 
#  输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出: 5
# 
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#      返回它的长度 5。
#  
# 
#  示例 2: 
# 
#  输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: 0
# 
# 解释: endWord "cog" 不在字典中，所以无法进行转换。 
#  Related Topics 广度优先搜索 
#  👍 679 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import string


class Solution(object):
    # def ladderLength(self, beginWord, endWord, wordList):
    #     """
    #     :type beginWord: str
    #     :type endWord: str
    #     :type wordList: List[str]
    #     :rtype: int
    #     """
    #     wordList = set(wordList)
    #     if endWord not in wordList:
    #         return 0
    #
    #     alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    #                  'u', 'v', 'w', 'x', 'y', 'z']
    #     queue = [(beginWord, 0)]
    #
    #     while queue:
    #         node, step = queue.pop(0)
    #         if node == endWord: return step + 1
    #         for i, s in enumerate(node):
    #             for c in alphabets:
    #                 if c != s:
    #                     new = node[:i] + c + node[i + 1:]
    #                     if new in wordList:
    #                         queue.append((new, step + 1))
    #                         wordList.remove(new)
    #     return 0

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        front = {beginWord}
        back = {endWord}
        dist = 1
        wordList = set(wordList)
        wordLen = len(beginWord)

        while front and back:
            dist += 1
            nextFront = set()
            for word in front:
                for i in range(wordLen):
                    for c in string.lowercase:
                        if c != word[i]:
                            newWord = word[:i] + c + word[i + 1:]
                            if newWord in back:
                                return dist
                            if newWord in wordList:
                                nextFront.add(newWord)
                                wordList.remove(newWord)
            front = nextFront
            if len(back) < len(front):
                front, back = back, front
        return 0


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    Solution().ladderLength('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"])
