# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。 
# 
#  进阶： 
# 
#  
#  你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？ 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 5 * 10⁴] 内 
#  -10⁵ <= Node.val <= 10⁵ 
#  
#  Related Topics 链表 双指针 分治 排序 归并排序 👍 1364 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None  # save and cut.

        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)

        # merge `left` and `right` linked list and return it.
        cur = dummy = ListNode(0)
        while left and right:
            if left.val < right.val:
                cur.next, left = left, left.next
            else:
                cur.next, right = right, right.next
            cur = cur.next
        cur.next = left if left else right
        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)