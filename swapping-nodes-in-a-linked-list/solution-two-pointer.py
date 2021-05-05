# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # 1721. Swapping Nodes in a Linked List
    # Difficulty: Medium
    # Time Complexity: O(N)
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        first = last = head

        for _ in range(1, k):
            first = first.next

        # start traversing from k th element
        # two pointer technique
        # you can also get length of linked list and iterate length - k times also
        cur = first
        while cur.next:
            cur = cur.next
            last = last.next

        # swapping values not node itself
        last.val, first.val = first.val, last.val
        return head

