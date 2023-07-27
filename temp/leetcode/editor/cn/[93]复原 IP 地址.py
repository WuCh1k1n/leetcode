# 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按 任何 顺序返回答案。 
# 
#  有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。 
# 
#  例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 
# 和 "192.168@1.1" 是 无效 IP 地址。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "0000"
# 输出：["0.0.0.0"]
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "1111"
# 输出：["1.1.1.1"]
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "010010"
# 输出：["0.10.0.10","0.100.1.0"]
#  
# 
#  示例 5： 
# 
#  
# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 3000 
#  s 仅由数字组成 
#  
#  Related Topics 字符串 回溯 👍 732 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        l = len(s)
        if l > 12 or l < 4:
            return []

        res = []
        for i in range(1, min(4, l - 2)):
            for j in range(i + 1, min(i + 4, l - 1)):
                for k in range(j + 1, min(j + 4, l)):
                    if l - k > 3:
                        continue
                    n = [s[:i], s[i:j], s[j:k], s[k:]]
                    flag = False
                    for c in n:
                        if c[0] == '0' and c != '0':
                            flag = True
                            break
                    if flag:
                        continue
                    a, b, c, d = map(int, n)
                    if 0 <= a <= 255 and 0 <= b <= 255 and 0 <= c <= 255 and 0 <= d <= 255:
                        res.append(str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))
        return res
# leetcode submit region end(Prohibit modification and deletion)
