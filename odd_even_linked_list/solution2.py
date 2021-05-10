# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # 328. Odd Even Linked List
    # Difficulty: Medium
    # Time Complexity: O(N)
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = ListNode(0)
        even = ListNode(0)

        odd_head = odd
        even_head = even
        is_odd = True

        while head:
            if is_odd:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            is_odd = not is_odd
            head = head.next

        even.next = None
        odd.next = even_head.next
        return odd_head.next


