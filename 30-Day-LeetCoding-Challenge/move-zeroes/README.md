# [Move Zeroes](https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3286/)

## Approach 1:

When I read the problem for the first time it came to my mind direct solution that I want to go through the array whenever I encounter zero I just remove it and when I am done I add them again.

But the removal procedure on a list in python will cost **O(n)**, and we will do this inside loop that goes through our `nums` array, so totally we will reach to **O(n<sup>2</sup>)** for the whole procedure.

```python
zeros = 0
for i in range(len(nums)): # O(n)
  del nums[i] # O(n)
  zeroes += 1
```

Then I thought okay what about using the python `count()` function to count the 0's and use another array to contain all my non-zeroes items in it. Then add zeroes amount of 0 to the end of the new array and later on override our `nums` array by this new array values because it requires not returning anything.

If you think a little bit you can see this approach will work better than the above as it will take only **O(n)**, but we used an extra space which is **O(n)** as we copied everything to a new defined array.
You can see full code for this [moveZeroes_2()](Solution.py#L16).


Then I thought no I want time **O(n)** with space **O(1)** can we do that!
Yes, of course, we can how by using two pointers the slow one will call it `last_non_zero` this will hold my last non zero number, and the fast pointer will call it `i` and this will hold my current element in the `nums` array.

What we will do will just move along the array whenever we encounter non zero number will move it to the place where `last_non_zero` pointer is located then increase this pointer by 1, and when we are done make another loop starting from where `last_non_zero` is to the end of the array and just keep adding zeros.

* **Example:**

`nums = [0,1,0,3,12]`

1. We will start with `last_non_zero = 0`, `i = 0`
2. check does `nums[i] != 0`, no it is not (`nums[i] = nums[0] = 0`)
3. increase the `i++` and check again, yes `nums[1] != 0` as it is `1` so move it to the `nums[last_non_zero] = nums[i]` and then increase `last_non_zero ++`<br>
Now our array looks like this `nums = [1,1,0,3,12]`

4. keep repeating this procedure until the end our array will look like this `nums = [1,3,12,3,12]` and `last_non_zero = 3`.

5. Now we start from `last_non_zero` to the end and just add `0` as we go so our final result will be `nums = [1,3,12,0,0]`


* **Pseudocode:**
```
1. define `last_non_zero = 0`, `n = len(nums)`
2. loop from i = 0 to n:
3.    if nums[i] != 0:
4.      nums[i] = nums[last_non_zero]
5.      last_non_zero += 1
6. loop from j = last_non_zero to n:
7.    nums[j] = 0
```

* **Complexity:**

* Time complexity is straight forward **O(n)**
* Space complexity we didn't use any extra space so it is **O(1)**

**Solution: [moveZeroes()](Solution.py#L2)**

> There is an optimal solution for this problem tries to find it out yourself :).
