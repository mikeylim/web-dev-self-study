## Given the roots of two binary trees p and q, write a function to check if they are the same or not.
## Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case 1: if both nodes are None, they are identical
        if not p and not q:
            return True
        # base case 21: if one of the node is None, they are different
        if not p or not q:
            return False
        return (p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)


# Tree 2 (identical to Tree 1)
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

# Tree 3 (different from Tree 1)
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(4)

sol = Solution()
print(sol.isSameTree(root1, root2))
print(sol.isSameTree(root1, root3))
print(sol.isSameTree(root2, root3))