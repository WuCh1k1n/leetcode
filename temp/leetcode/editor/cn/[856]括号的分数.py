"""
给定一个平衡括号字符串 S，按下述规则计算该字符串的分数： 

 
 () 得 1 分。 
 AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。 
 (A) 得 2 * A 分，其中 A 是平衡括号字符串。 
 

 

 示例 1： 

 输入： "()"
输出： 1
 

 示例 2： 

 输入： "(())"
输出： 2
 

 示例 3： 

 输入： "()()"
输出： 2
 

 示例 4： 

 输入： "(()(()))"
输出： 6
 

 

 提示： 

 
 S 是平衡括号字符串，且只含有 ( 和 ) 。 
 2 <= S.length <= 50 
 

 Related Topics 栈 字符串 👍 406 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = [0]
        for c in s:
            if c == '(':
                st.append(0)
            else:
                v = st.pop()
                st[-1] += max(v*2, 1)
        return st[-1]
# leetcode submit region end(Prohibit modification and deletion)
