# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
	cur = head
	prev = None
	while cur:
		next = cur.next
		cur.next = prev
		prev, cur = cur, next
	return prev

#iterative
#Time: O(n)
#Space: O(1)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newhead = head
        if head.next:
            newhead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newhead
# recursive
# Time: O(n)
# Space: O(n)
