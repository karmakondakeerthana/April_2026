class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        s=f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        curr=s
        prev=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        l=head
        r=prev
        while r:
            if l.val!=r.val:
                return False
            l=l.next
            r=r.next
        return True
