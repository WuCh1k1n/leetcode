# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。 
# 
#  返回同样按升序排列的结果链表。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目在范围 [0, 300] 内 
#  -100 <= Node.val <= 100 
#  题目数据保证链表已经按升序排列 
#  
#  Related Topics 链表 双指针 👍 744 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = cur = ListNode(0, head)
        while cur.next and cur.next.next:
            if cur.next.val != cur.next.next.val:
                cur = cur.next
            else:
                temp = cur.next.val
                while cur.next and cur.next.val == temp:
                    cur.next = cur.next.next
        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)