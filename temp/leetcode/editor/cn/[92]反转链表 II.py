# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
# 
#  说明: 
# 1 ≤ m ≤ n ≤ 链表长度。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL 
#  Related Topics 链表 
#  👍 624 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # # 迭代
    # def reverseBetween(self, head, m, n):
    #     if not head:
    #         return None
    #     curr, prev = head, None
    #     while m > 1:
    #         prev = curr
    #         curr = curr.next
    #         m -= 1
    #         n -= 1
    #     con, tail = prev, curr
    #     while n > 0:
    #         temp = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = temp
    #         n -= 1
    #     if con:
    #         con.next = prev
    #     else:
    #         head = prev
    #     tail.next = curr
    #     return head

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == 1:
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

    def reverseN(self, head: ListNode, N: int) -> ListNode:
        pre, cur = None, head
        while N:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
            N -= 1
        head.next = cur
        return pre
# leetcode submit region end(Prohibit modification and deletion)