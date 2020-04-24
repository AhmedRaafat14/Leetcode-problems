# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder):
        root = TreeNode(preorder[0])
        stack = [root]
        for val in preorder[1:]:
            new_node = TreeNode(val)
            if val < stack[-1].val:
                stack[-1].left = new_node
            else:
                while stack and stack[-1].val < val:
                    parent = stack.pop()
                parent.right = new_node
            stack.append(new_node)
        return root
