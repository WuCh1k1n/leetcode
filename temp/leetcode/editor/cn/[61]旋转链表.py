# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 500] 内 
#  -100 <= Node.val <= 100 
#  0 <= k <= 2 * 10⁹ 
#  
#  Related Topics 链表 双指针 👍 660 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        cur, tail = head, None
        l = 0
        while cur:
            l += 1
            tail = cur
            cur = cur.next

        k = k % l
        if k == 0:
            return head
        prev = ListNode(0, head)
        for _ in range(l - k):
            prev = prev.next
        new_head = prev.next
        prev.next = None
        tail.next = head
        return new_head
# leetcode submit region end(Prohibit modification and deletion)
