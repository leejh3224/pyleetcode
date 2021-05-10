"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:

    # 116. Populating Next Right Pointers in Each Node
    # Difficulty: Medium
    # Time Complexity: O(N)
    #   Time Complexity for BFS/DFS in general is O(V+E) however E equals V-1 in 'perfect binary tree' so it's O(N) where N = number of nodes
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = [root]

        while queue:
            size = len(queue)

            # general template for level order traversal
            while size:
                node = queue.pop(0)

                # if size == 0, it means the node is the last node for given level
                # for such case it's not necessary to connect next node
                if size > 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                size -= 1

        return root