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
    # Explanation
    #   Time Complexity for BFS/DFS in general is O(V+E) however E equals V-1 in 'perfect binary tree' so it's O(N) where N = number of nodes
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        def dfs(node):
            if not node or not node.left:
                return

            # connecting left node
            node.left.next = node.right

            # we connect right node if node has non null next pointer
            if node.next:
                node.right.next = node.next.left

            # do it recursively for left, right subtree
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root
