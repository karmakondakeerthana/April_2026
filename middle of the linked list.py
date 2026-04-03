class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        s=f=curr
        while f and f.next:
            s=s.next
            f=f.next.next
        return s
