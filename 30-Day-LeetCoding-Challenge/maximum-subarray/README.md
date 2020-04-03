# [Maximum Subarray](https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3285/)

#### Solution using [greedy algorithm](https://brilliant.org/wiki/greedy-algorithm/):


The problem asks us to find the **contiguous** subarray that contains the **maximum** sum and return this **sum**.

So, the input is a linear array and that what makes it maybe it can be solved using **greedy** algorithm.

So what is the idea here we need at each step to check what is the optimal solution for the current step and pick it up and when we reach the end we will have the general optimal solution for our problem?

In steps:
1. we have our current number and the current_sum in this step
2. we decide should we take this number or no we ignore it.
3. we decide does our new current_sum is greater than our global sum so we take it or we ignore it?

__Lets apply an example so it can be clear for you.__

**Example:**<br>

`nums = [-2,1,-3,4,-1,2,1,-5,4]`

> Remember we don't care about what is the **contiguous sub-array** we care more about the **sum** of this array.

*, First of all, we define two variables
`global_sum # to hold our final answer`
`current_sum # to hold our sub-array sum`

* starting with making this two vars equal to our first element in our array.
> global_sum = current_sum = -2

* Then we start from the next number and check should we take this number or no ignore it?
> current_number = 1

* We check does the current number **maximise** our current same or reduce or even keep it the same, as we all know we need the **maximum** sum:
> current_sum = max(current_sum, current_number + current_sum)<br>
current_sum = max(-2, 1 + -2) = max(-2, -1) = -1

* Then we now we have the our new `current_sum` we need to know what will be our `global_sum` as well, as we said in the previous step we are searching for **maximum** so we need choose the max between our `current_sum` value & `global_sum`.
> global_sum = max(global_sum, current_sum)<br>
global_sum = max(-2, -1) = -1

> **Then we will keep doing this with the whole array until the end for the example above our answer will be `6`. I left it here for you keep doing the same on paper until the end and see what will be the result**


**Pseudocode:**
```
1. define global_sum = current_sum <-- nums[0]
2. forloop num in nums[1:]
3.    current_sum = max(current_sum, (current_sum + num))
4.    global_sum = max(global_sum, current_sum)
5. return global_sum
```

**Complexity:**

* Time complexity it is obvious that we do linear and that is the benefits of solving this problem using greedy so it will be **O(n)**.

* Space complexity so obvious as well we don't use any extra space instead of our two variables which are constant space, so it will be **O(1)**.

> **Additional tips**<br>
    1. If the given array is empty our answer will always be `0`;<br>
    2. Also, if the given array only has one number which means our answer will be that number.

* **[Solution in python](Solution.py)**

**Please, try to figure out different solutions for the problem this is only my solution**

I hope this helps any feedback will be appreciated :).
