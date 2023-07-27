# 一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。 
# 
#  假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。 
# 
#  例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。 
# 
#  与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。 
# 
#  现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变
# 化次数。如果无法实现目标变化，请返回 -1。 
# 
#  注意： 
# 
#  
#  起始基因序列默认是合法的，但是它并不一定会出现在基因库中。 
#  如果一个起始基因序列需要多次变化，那么它每一次变化之后的基因序列都必须是合法的。 
#  假定起始基因序列与目标基因序列是不一样的。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
# 
# 返回值: 1
#  
# 
#  示例 2： 
# 
#  
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
# 
# 返回值: 2
#  
# 
#  示例 3： 
# 
#  
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
# 
# 返回值: 3
#  
#  👍 66 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # def minMutation(self, start, end, bank):
    #     """
    #     :type start: str
    #     :type end: str
    #     :type bank: List[str]
    #     :rtype: int
    #     """
    #     bank = set(bank)
    #     if end not in bank:
    #         return -1
    #
    #     change_map = {
    #         "A": "CGT",
    #         "C": "AGT",
    #         "G": "CAT",
    #         "T": "CGA",
    #     }
    #     queue = [(start, 0)]
    #
    #     while queue:
    #         node, step = queue.pop(0)
    #         if node == end: return step
    #         for i, s in enumerate(node):
    #             for c in change_map[s]:
    #                 new = node[:i] + c + node[i + 1:]
    #                 if new in bank:
    #                     queue.append((new, step + 1))
    #                     bank.remove(new)
    #     return -1

    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if end not in bank:
            return -1

        change_map = {
            "A": "CGT",
            "C": "AGT",
            "G": "CAT",
            "T": "CGA",
        }

        front = {start}
        back = {end}
        dist = 0
        bank = set(bank)
        gen_length = len(start)

        while front and back:
            dist += 1
            next_front = set()
            for gen in front:
                for i in range(gen_length):
                    for c in change_map[gen[i]]:
                        new_gen = gen[:i] + c + gen[i + 1:]
                        if new_gen in back:
                            return dist
                        if new_gen in bank:
                            next_front.add(new_gen)
                            bank.remove(new_gen)
            front = next_front
            if len(back) < len(front):
                front, back = back, front
        return -1
# leetcode submit region end(Prohibit modification and deletion)
