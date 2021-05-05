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
        node = head
        arr = []

        while node:
            arr.append(node.val)
            node = node.next

        # swap
        temp = arr[k - 1]
        arr[k - 1] = arr[len(arr) - k]
        arr[len(arr) - k] = temp

        dummy = ListNode(0)
        answer = dummy

        for i in arr:
            answer.next = ListNode(i)
            answer = answer.next

        return dummy.next
