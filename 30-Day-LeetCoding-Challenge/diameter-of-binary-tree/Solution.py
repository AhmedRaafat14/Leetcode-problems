# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 0
        def depth(node):
            if not node:
                return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, R + L)
            return max(L, R) + 1

        depth(root)
        return self.ans

## Basic example
if __name__ == "__main__":
    tree_1 = TreeNode(1)
    tree_2 = TreeNode(2)
    tree_3 = TreeNode(3)
    tree_4 = TreeNode(4)
    tree_5 = TreeNode(5)

    tree_1.left = tree_2
    tree_1.right = tree_3

    tree_2.left = tree_4
    tree_2.right = tree_5

    sol = Solution()
    print(sol.diameterOfBinaryTree(tree_1))
