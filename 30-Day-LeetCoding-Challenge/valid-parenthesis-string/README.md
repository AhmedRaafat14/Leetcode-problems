# [Valid Parenthesis String](https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3301/)

## Approach 1:

So we need to validate if the string is valid parenthesis string or not.

It gives us some rules and I call them hints as they are helping in finding the solution.

We need to keep in mind each `(` must have a corresponding `)` to call it valid, any `)` must have a corresponding `(`, we need also to keep in mind the order so the `(` must go before it is corresponding `)`, also we will have an additional letter which is `*` this can be used as `(` or `)` or just an empty string this will be helpful to make string valid.

From the problem statement as we care about the left & right parenthesis we also care about their indices more. So, I can think of the same way as the solution for [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) problem using stacks.

But in our case we don't need one stack we need two one will be working over our parentheses (call it `paren_stack`) and the other one is for the stars `*` (call it `stars_stack`), and as we said we care more about the order so we going to store there the index for this chars.

The solution am thinking of we going to use these two stacks whenever we see an open parenthesis `(` will push it is an index to the corresponding stack and when we see star `*` we push it to the corresponding stack as well, and whenever we see closing parenthesis we have three cases to think about here if we already have something in the parentheses stack `paren_stack` so we `pop` the top index which will be referring to an open parenthesis `(` but what if it is empty? as we know we can use the star `*` as open/closing parenthesis so we see do we have anything in our stars stack `stars_stack` yes we have so we pop it and continue in our way.

Okay, so far so good but what if we have closing parenthesis and the two stacks are empty? cool that is our third case and now we sure the string is not valid so we just return `false` as our answer and we are done.


We do the previous algorithm in a loop until we finish inspecting the whole string after that we check if we still have items in the two stacks that means we are not done yet so we going to check if both stacks are equal in the length if they are not we return `false` and we are done. But why we do that?
Because we know all the items in `paren_stack` are `(` so we need the same amount of closing ones `)` and we can use the stars as closing parentheses.

Okay, sounds great but we know that even if the two stacks are equal in the size we can not yet say the string is valid as we care a lot about the order of them, great now you got it ;).

So we just do another loop until any of them is not empty and keep popping the items and compare them if at any iteration we found the open parenthesis index we pooped is greater than the corresponding pooped star that means it is not valid we just return `false`, otherwise keep going until the loop is done we return `true`.


**Pseudocode:**

```
1. define paren_stack <-- [] and stars_stack <-- []
2. loop over enumerate(str) into idx, ch
3.    if ch is '(' append it is index to paren_stack.append(idx)
4.    else if ch is '*' append it is index to stars_stack.append(idx)
5.    otherwise we have three cases
5.1.      if paren_stack not empty we pop an item paren_stack.pop()
5.2.      else if stars_stack not empty: stars_stack.pop()
5.3.      otherwise we return false
6. check if len(paren_stack) > len(stars_stack) return false
7. loop until any of paren_stack or stars_stack being empty
8.    check if paren_stack.pop() > stars_stack.pop() we return false
9. return true
```

**Complexity:**

* Time Complexity: it is clear we do linear scans so our time will be **O(n)** where `n` is the size of our string

* Space Complexity: we use two stacks to store items so we can say in the worst case will have **O(n)**.


> **There is another solution to improve the space using two pointers try to come up with it yourself.**

**[Solution in python](Solution.py)**
