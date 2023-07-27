# 给定一个包含 [0，n) 中不重复整数的黑名单 blacklist ，写一个函数从 [0, n) 中返回一个不在 blacklist 中的随机整数。 
# 
#  对它进行优化使其尽量少调用系统方法 Math.random() 。 
# 
#  提示: 
# 
#  
#  1 <= n <= 1000000000 
#  0 <= blacklist.length < min(100000, N) 
#  [0, n) 不包含 n ，详细参见 interval notation 。 
#  
# 
#  示例 1： 
# 
#  
# 输入：
# ["Solution","pick","pick","pick"]
# [[1,[]],[],[],[]]
# 输出：[null,0,0,0]
#  
# 
#  示例 2： 
# 
#  
# 输入：
# ["Solution","pick","pick","pick"]
# [[2,[]],[],[],[]]
# 输出：[null,1,1,1]
#  
# 
#  示例 3： 
# 
#  
# 输入：
# ["Solution","pick","pick","pick"]
# [[3,[1]],[],[],[]]
# 输出：[null,0,0,2]
#  
# 
#  示例 4： 
# 
#  
# 输入： 
# ["Solution","pick","pick","pick"]
# [[4,[2]],[],[],[]]
# 输出：[null,1,3,1]
#  
# 
#  输入语法说明： 
# 
#  输入是两个列表：调用成员函数名和调用的参数。Solution的构造函数有两个参数，n 和黑名单 blacklist。pick 没有参数，输入参数是一个列表
# ，即使参数为空，也会输入一个 [] 空列表。 
#  Related Topics 哈希表 数学 二分查找 排序 随机化 
#  👍 73 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import random


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.white_len = n - len(blacklist)
        black_lt = {i for i in blacklist if i < self.white_len}
        white_gt = {j for j in range(self.white_len, n)} - set(blacklist)
        self.map = dict(zip(black_lt, white_gt))

    def pick(self) -> int:
        res = random.randint(0, self.white_len - 1)
        if res in self.map:
            return self.map[res]
        else:
            return res
# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
# leetcode submit region end(Prohibit modification and deletion)
