from collections import defaultdict


class Solution:

    # 236. Lowest Common Ancestor of a Binary Tree
    # Difficulty: Medium
    # Time Complexity: O(N)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # keep track of ancestors including node itself
        ancestors = defaultdict(list)
        ancestors[root.val] += [root.val]

        queue = [root]

        while queue:
            node = queue.pop(0)

            if node.left:

                # updating ancestors
                if node.val in ancestors:
                    ancestors[node.left.val] += ancestors[node.val]
                ancestors[node.left.val] += [node.left.val]
                queue.append(node.left)

            if node.right:

                # updating ancestors
                if node.val in ancestors:
                    ancestors[node.right.val] += ancestors[node.val]
                ancestors[node.right.val] += [node.right.val]
                queue.append(node.right)

        ancestor_p = ancestors[p.val]
        ancestor_q = ancestors[q.val]

        pos_p, pos_q = 0, 0

        while pos_p < len(ancestor_p) and pos_q < len(ancestor_q):
            if ancestor_p[pos_p] != ancestor_q[pos_q]:
                break
            pos_p += 1
            pos_q += 1

        return TreeNode(ancestor_p[pos_q - 1])
