# [Product of Array Except Self](https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3300/)

## Approach 1:

The problem asks us to replace each element in an array with the product of the other array elements and also asks us to do it in **O(n)**.

So, for example if we have this array `arr = [1, 2, 3]`, the result should be `ans = [6, 3, 2]` do we replaced the `1` with `2 * 3 = 6` and so on.

To do this in **O(n)** should make you think a little bit about how we can do that! I can think of that we have two arrays one we put for each element the product of the elements before it (left) and another one do the same but from the end (right) some kind of DP. Then we do another loop to multiple for each element the `left[i] * right[i]` and that will be our answer.

> try to do this solution yourself :).

Then I saw that they asking for a follow-up to do it in constant space without considering our output array.

So, I thought of simulating the two array approach but instead of using two arrays, I will just use two pointers one of them will call it `left_product` and this one will go from the left to right and another pointer called `right_product` which will go from the right to the left.

The only thing when I do from the left I use index `i = 0, 1,..n` but from the right we need the invert (~) of this number so we can get it from the right `i = -1,-2,...-n`, and we keep updating the two pointers with the latest product we find until we finish with the whole array.

Let's do an example to make it more clear.

**Example:**

* Define `arr = [1, 2, 3]`
* We will be using `left_product = 1`, `right_product = 1` we initialise them with `1` as we do product.
* We will initialise as well our answer array by the same size of our `arr` but will be filled with ones `ans = [1, 1, 1]`
* Start with `idx = 0` so our `num = arr[idx] = 1` now will find our `ans[idx]` by multiple it by the latest `left_product` we have so: `ans[0] = ans[0] * left_product = 1 * 1 = 1`, our new answer is `ans = [1, 1, 1]`.
* Now, we calculate the new `left_product` by multiple it with the current `arr[idx]` so it will be `left_product = left_product * arr[0] = 1 * 1 = 1`.

* Do the right as we said we need to use the invert so `idx = - (idx + 1)` or we can just use the invert operator `idx = ~idx`, and find our new `ans[~idx] = ans[-1]` will multiple it by the right_product so `ans[-1] = ans[-1] * right_product = 1 * 1 = 1`, and our new answer is `ans = [1, 1, 1]`.
* Calculate the `right_product` by multiple it's value with the `arr[~idx]` so it will be `right_product = right_product * arr[-1] = 1 * 3 = 3`.

* Well, keep doing the above procedure over and over until you will reach the final answer array which will be `ans = [6, 3, 2]`. Do it on paper so you can get the idea very clear.


**Pseudocode:**

```
1. define ans = [1] * len(arr)
2. define our pointers left_product,right_product = 1, 1
3. loop over the arr from i = 0 to len(arr)
4.    calculate ans[i] = ans[i] * left_product
5.    calculate left_product = left_product * arr[i]
6.    calculate ans[~i] = ans[~i] * right_product
7.    calculate right_product = right_product * arr[~i]
8. return our ans
```

**Complexity:**

* Time Complexity: it is so clear we do **O(n)** one loop over the array.

* Space Complexity: taking away the answer array it will be constant space **O(1)**.

* **[Solution in python](Solution.py)**
