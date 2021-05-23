class Solution:

    # 236. Lowest Common Ancestor of a Binary Tree
    # Difficulty: Medium
    # Time Complexity: O(N)
    #   explanation:
    #     In worst case, p and q can be found on left and right most side of the tree
    #     In this case we are forced to lookup every subtree (node) in the tree, i.e. O(N)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root in (p, q):
            return root

        # trying to find target nodes (p and q) in left or right subtree
        left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)

        # if p and q were found in left and right node
        # it means root is the common ancestor
        #
        #      3
        #  1      5
        #  where p and q were given as follows: p = 1 and q = 5
        #
        # Think about the above case
        # p was found on left subtree and q was found on right subtree
        # which means LCA (lowest common ancestor) becomes root(node with value 3)
        if left and right:
            return root

        # if p and q were found in either of the subtree,
        # then the root of the subtree would be the LCA
        return left or right
