# [Middle of the Linked List](https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3290/)

## Approach 1:

The problem is so straightforward and so clear it asks us to return the middle node, with one condition if there is two middle numbers return the second one.

If we think about it for a minute the two middle numbers only happen when the length of the array is **even**, but the fact is if we do integer division for `len(arr) // 2` to get the middle number it will always give you the correct middle number, let's see it:

If we have `arr = [1,2,3,4,5]` then the middle number will be at `len(arr) // 2 = 5 // 2 = 2` so it will be **`arr[2] = 3`** which is the correct middle number.

What if it is even `arr = [1,2,3,4,5,6]` so it will be `len(arr) // 2 = 6 // 2 = 3` so ... **`arr[3] == 4`** which is the second middle number.

This should make the problem now easier so what we will do now based on the above we just want to put all our **linked-list nodes** in an **array** then return the middle node in that array (`return nodes[len(nodes) // 2]`).


* **Example:**

`lked_list = 1 --> 2 --> 3 --> 4 --> 5`
`head -> 1`

 * First we will have `nodes = []` array to store our nodes there.

 * We need to start from the `head` and keep looping until the end and keep pushing to the array the elements

 * So, at end our nodes array will be like this: <br>
 `nodes = [{val: 1, next: ->}, {val: 2, next: ->}, {val: 3, next: ->}, {val: 4, next: ->}, {val: 5, next: None}]`

 * No our answer will be `ans = nodes[len(nodes) // 2] = nodes[5 // 2] = ndes[2] = {val: 3, next: ->}`.

 * **Pseudocode:**
 
 ```
 1. define nodes = []
 2. loop as long as head != None
 3.   nodes.append(head)
 4.   head = head.next
 5. return nodes[len(nodes) // 2]
 ```

 * **Complexity:**

 * Time Complexity: It is so clear we only do one loop to build our `nodes` array so it will be **O(n)** where **n** is the number of nodes in the list.

 * Space Complexity: it is clear that we use extra space to store all our list nodes in an array and this will cost us **O(n)** where **n** is the number of nodes in the list.

 * **[Solution in python](Solution.py)**

 > There is an optimal space solution try to find it out yourself :).
