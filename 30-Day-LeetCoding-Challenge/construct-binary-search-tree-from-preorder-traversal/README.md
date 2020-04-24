# [Construct Binary Search Tree from Preorder Traversal](https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3305/)

## Approach 1:

So we need to build a binary search tree from a preorder traversal.


We have an array for the nodes we gonna use a stack to revert back the preorder traversal process.

So we will define the root node with our first element `root = TreeNode(arr[0])`, then we push it into a defined stack `stack = [root]`.

Now, we going to loop through the whole elements in the preorder traversal array `arr` and create a new node for each element `new_node = TreeNode(element)`, then we check our `new_node.val` value with the top node vale in the stack `stack[-1].val` if it is less than we make the `new_node` as a left child to the top node in the stack `stack[-1].left = new_node`. Otherwise, we will keep popping nodes from the stack as long as the node value on top of the stack smaller than our `new_node.val` and with each `pop` we update the parent node to be `parent = stack.pop()` after we finish with the loop, we update parent right child with the new node `parent.right = new_node` then we push the new node to the stack `stack.append(new_node)`.


**Pseudocode:**

```
1. define our root = TreeNode(preorder[0])
2. initialise our stack = [root]
3. loop for each element in preorder[1:]
4.    define the new_node = TreeNode(element)
5.    check if new_node.val < stack[-1].val, then stack[-1].left = new_node
6.    Otherwise, loop as long as the stack not empty and stack[-1].val < new_node.val
7.      do, parent = stack.pop()
8.    parent.right = new_node
9. return root
```

**Complexity:**

* Time Complexity:
  * We loop over the whole nodes (`n`) and we visit each node so our time will be **O(n)**.

* Space Complexity:
  * We use stack to store all our nodes so we will use **O(n)**.


**[Solution in python](Solution.py)**
