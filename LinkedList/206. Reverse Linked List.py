# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        cur = head
        while cur:
            if cur.next:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            else:
                cur.next = prev
                break
        return cur
