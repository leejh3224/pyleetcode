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
        if not head or not head.next:
            return head

        # two pointers
        odd = head
        even = head.next

        # to link odd and even nodes
        even_head = even

        while even and even.next:

            # modify linked list
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        # link odd and even nodes
        odd.next = even_head

        return head


