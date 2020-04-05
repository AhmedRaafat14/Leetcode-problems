# [Single Number](https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3283/)

## Approach 1:

#### Solution using [bit manipulation](https://www.interviewbit.com/courses/programming/topics/bit-manipulation/):

This problem asks you to find the single (unique) number that exists in a list within a linear time which means **O(n)** with another optional requirement which is without extra memory means space complexity **O(1)**.

We could solve it using hash-map in **O(n)** it will be good no issue, but I want to get from the first time with no extra memory this is when it came to my mind the bit manipulation idea and couldn't find better than the **XOR** operation and why is that? because if we revisit the truth table of the XOR:

| A  | B  | Q  |
| -- | -- | -- |
| 0  | 0  | 0  |
| 0  | 1  | 1  |
| 1  | 0  | 1  |
| 1  | 1  | 0  |

So you can see when you take an XOR with any bit gives **0** but when you take the XOR for two different bits it gives you **1**, and here is the trick we can use the XOR to XOR all our numbers in the list and when we are done it will return only the single number that does not rebate in the list.

**Example:**

`nums = [[2,2,1]]`

so if we do XOR:
`ans = 2 ^ 2 ^ 1 = 0 ^ 1 = 1`

As you can see that is how we made use of the **XOR ^** operation.


**Pseudocode:**
```
1. ans <- 0 # starting from 0 as (0 ^ X) will give us X.
2. for each num in nums:
3.    ans ^= num
4. return ans
```

**Complexity:**

* Time:
  * As you can see we only do one for loop through the whole numbers list so it is linear so it is **O(n)** where **n** is the size of our numbers list.

* Space:
  * We didn't use any extra space beside our **ans** variable which is **O(1)** so our overall complexity will be **O(1)**.


* **[Solution in Python](Solution.py)**

I hope this helps any feedback will be appreciated :).
