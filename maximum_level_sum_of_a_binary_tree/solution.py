# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1161. Maximum Level Sum of a Binary Tree
# Difficulty: Medium
# Time Complexity: O(V+E) (using bfs)
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = []
        queue.append(root)

        level_sums = []

        while queue:
            size = len(queue)
            level_sum = 0

            while size:
                size -= 1
                node = queue.pop(0)

                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level_sums.append(level_sum)

        return level_sums.index(max(level_sums)) + 1
