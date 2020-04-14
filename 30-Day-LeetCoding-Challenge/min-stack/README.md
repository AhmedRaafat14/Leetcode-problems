# [Min Stack](https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3292/)

## Approach 1:

The question is asking us to build `Stack` but a special one that returns the minimum value in it in constant time **O(1)**.

We all now very clear that Stack is working with the **LIFO** principle which means **Last In First Out**, and why this is important to think about because we know pushing item to stack takes **O(1)** and also removing an item from stack takes **O(1)**, and getting the top item of the stack is **O(1)**.

We all know this very clear so it is easy to build stack class using list (array) to store the items.

But here we need a special function called `getMin()` which should return to us the minimum item in the stack in **O(1)** if we think about it ooh that is not possible I have to sort the stack first or I should do a loop over the list to find that minimum item and of course that is not **O(1)**.

So how we gonna fix that okay let's see we no whenever we put an element to the stack we will not be able to remove it until we remove the one above it, imagine a stack of plates you can not remove the plate in the middle without moving the top one's first right! So we can apply the same principle by adjusting our stack a little bit to not just store our item no we will store with each one the minimum value we found so far.

So, for example, let's say we are creating our stack and the first item we push is `3` will ask is the stack empty yes it is so that means that `3` is our minimum value we know so far!

Our stack will look like this `[(item, min_item)] = [(3, 3)]`.

So if we add now a new item let's say `2`, so we check again the stack now it is not empty so we check is our new item (`2`) smaller than the minimum one stored with our top item in the stack which is `3`, so yes `2 < 3` so we push to our stack our new item associated with the new minimum value.

Our new stack looks `[(3, 3), (2, 2)]`, now if we want to call `getMin()` it will just return the second element in the top pair in the stack :).

Now, the `getMin()` will cost **O(1)**.

Try to simulate it on paper with more items.


* **Pseudocode:**

* `push(number)`:
  ```
    1. if stack is empty
    2.    stack.append((number, number))
    3. otherwise:
    4.    define smallest_num = min(number, stack[-1][-1]) compare with the top
    5.    stack.append((number, smallest_num))
  ```
* `pop()`
  ```
    1. always get & remove the first number in the top pair: stack.pop()[0]
  ```
* `top()`
  ```
    1. always get the first number in the top pair: stack[-1][0]
  ```
* `getMin()`
  ```
  1. always get the second number in the top pair: stack [-1][1]
  ```

* **Complexity:**

* Time Complexity: for all functions will be **O(1)**

* Space Complexity: we use a list to store the elements as a stack which will be **O(n)** where n is the number of items, we also have a modified stack that stores the numbers in pairs so it will be **2.O(n) == O(n)**.

* **[Solution in python](Solution.py)**
