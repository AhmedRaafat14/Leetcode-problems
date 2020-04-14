# [Diameter of Binary Tree](https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3293/)

## Approach 1:

It asks us to find a binary tree diameter, it also explains to us that is the diameter of a binary tree is **the length of the longest path between any two nodes in a tree.**

It is also indicated that doesn't matter if the path passes by the root or not.


So, we need to calculate the depth of each node in the tree and then find the longest path between the nodes.

First the depth of node can be found by `node.depth = max(node.left.depth, node.right.depth) + 1`.

Also, the path always will be the depth of the left subtree + the depth of the right subtree, so on each node, we need to choose the maximum value that takes us to the final answer so our answer will be: `diameter = max(diameter, left_depth + right_depth)`.

So, how we can calculate that if you look to the illustration above we see that we need to go deep to the tree to get one node depth which means we need to use `depth-first search DFS`.

We use DFS to find the left subtree depth then find the right subtree depth and later choose between them.


* **Pseudocode:**

* `diameterOfBinaryTree(root)`
```
1. define our answer
2. call find_depth_helper(root) with the root to find the longest path.
3. return our answer
```

* `find_depth_helper(node)`
```
1. if the node is None return 0
2. find_depth_helper(node.left) --> left_depth
3. find_depth_helper(node.right) --> right_depth
4. answer = max(answer, left_depth + right_depth)
5. return the current node depth max(left_depth, right_depth) + 1
```

* **Complexity:**

* Time Complexity: it is so clear that we go over all our nodes so our time will be **O(n)** where **n** is the number of nodes in the tree.

* Space Complexity: we use recursion stack as we do recursion calls and this stack will be equal to the number of nodes we have so our overall space will be **O(n)**.

* **[Solution in python](Solution.py)**
