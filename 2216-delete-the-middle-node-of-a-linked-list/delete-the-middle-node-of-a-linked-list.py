# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow:
            if slow.next:
                slow.next = slow.next.next
            else:
                slow.next = None
        return head