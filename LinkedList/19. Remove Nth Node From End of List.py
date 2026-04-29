class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0
        
        while cur:
            cur = cur.next
            length += 1
        
        if n == length:
            return head.next
        
        cur = head
        for _ in range(length - n - 1):
            cur = cur.next
        
        cur.next = cur.next.next
        
        return head