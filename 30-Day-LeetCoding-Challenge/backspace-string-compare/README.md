# [Backspace String Compare](https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3291/)

## Approach 1:

The problem is so easy if you read it carefully it asks if string **S** and string **T** are equal consider you typing them in a text editor (notepad), but it is not that easy you will have a special character called **#** it means **backspace** so whenever you see it assume you clicked on the backspace button in your keyboard.

So, if you have a string like this `ab#c` if we follow the rule we mentioned above, you first type `a` then you find `b` not a `#` so type it and it will be `ab` now we see `#` and it means backspace so click on the backspace button will remove the `b` and leave us with `a` then the last one is `c` type it `ac` and this our final result.

It is so obvious now whenever we see the backspace `#` char we remove the last typed char and this takes to a data structure called **[Stack](https://www.tutorialspoint.com/data_structures_algorithms/stack_algorithm.htm)** as the stack works in **LIFO** manner which means `last-in-first-out`.

So, we will go through the two strings to build a stack from their characters and in the end, we compare both of them if they are equal or not.

Let us do an example.

* **Example:**

`S = "ab#c"`
`T = "ad#c"`

We will do each string separately and then combine all elements in the stack into one string and then compare them.

* We will use stack called `typed_chars = []`.
* Start with `S = "ab#c"`.
* Starting with `ch = 'a'` is our `ch == '#' # backspace`  no it is not so add it to the stack `typed_chars = ['a']`.
* With `ch = 'b'` is `ch == '#'` no so add it to the stack `typed_chars = ['a', 'b']`.
* With `ch = '#'` is `ch == '#'` yes it is so we simulate the click on the `backspace #` button by removing the last typed character `typed_chars.pop() ==> 'b'` so our new stack is `typed_chars = ['a']`.
* With our last `S` char `ch = 'c'` is `ch == '#'` no it is not so add to the stack `typed_chars = ['a', 'c']`.
* Build final string from the `typed_chars` to be `new_s = 'ac'` remember it.

* Now will do the same with the `T = "ad#c"` it will be exactly the same process and will end-up with `new_t = 'ac'`.

* If we compare both `new_s == new_t = 'ac' == 'ac' = True`, and this is our answer.

* **Pseudocode:**

```
1. define helper function called helper that takes one string: helper(s)
2.      define typed_chars = []
3.      loop for ch in s:
4.          check if ch != '#':
5.              typed_chars.append(ch)
5.          if ch is equal to # and typed_chars not empty:
6.              typed_chars.pop()
7.      return "".join(typed_chars) to return one string
8. check if helper(S) is equal to helper(T) or not and return the result.
```

* **Complexity:**

* Time Complexity:
  * We can see that we loop two times to build our stacks the first one is for **O(n)** where **n** is our first-string length, and the second time is for **O(m)** where **m** is our second string length, so in total it will be **O(n + m)**.

* Space Complexity:
  * We store our chars in stack two times of course for our first string and our second one, so in total it will be **O(n + m)**.

* **[Solution in python](Solution.py)**
