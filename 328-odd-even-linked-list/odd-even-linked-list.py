# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        if not head or not head.next:
            return head
        x = cur = head.next
        while cur and cur.next:
            t = cur.next
            prev.next = t
            cur.next = t.next
            prev = prev.next
            cur = cur.next
        prev.next = x
        return head