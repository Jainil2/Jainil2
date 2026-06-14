# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        res = arr[0] + arr[-1]
        l = 1
        r = len(arr) - 2
        while l < r:
            res = max(res, arr[l] + arr[r])
            l += 1
            r -= 1
        return res