# [Contiguous Array](https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3298/)

## Approach 1:

The problem asking us to find the maximum length of the subarray that contains equal numbers of 0 and 1.

We can say if we have zero counter and one counter our contiguous subarray with an equal number of 0 & 1 will happen when the counters are equal right!

So let's define one counter called `count = 0` and when we see `0` we decrease the count by `1` and when we see `1` we increase it with `1` and when the `count == 0` that means we have our subarray so calculate the length.

To be able to find our answer which is the `maximum length` we need to store this counts somewhere associated with their indexes and when we encounter the same count again then we subtract the new index with the stored index and find our answer.

I can't think of any data structure to help us do that besides the **hash-map** so we will be using it.

**Example:**

- define `arr = [0, 0, 1, 0, 0, 0, 1, 1]`
- define ` start with map = {0: -1}` to hold our counts associated with indexes
- define `count = 0` to count the number of zeros and ones
- define `max_length = 0` to hold our answer

* When we encounter first `arr[0] = 0` so we decrease the count by `1`, `count -= 1 = -1` do we have count `-1` in our `map` so so store it with the index: `map[count] = arr[0]` => `map = {0: -1, -1: 0}`.

* When `arr[1] = 0` so our new count will be `count = -2` not in the map so add it: `map = {0: -1, -1: 0, -2: 1}`

* When `arr[2] = 1` now increase our count by one so it will be `count = -2 + 1 = -1` do we have this in our `map` yes we have it so we subtract the current index `2` from the one stored in the `map` ==> `0`, so it will be `tmp = 2 - 0 = 2` compare it with our ` max_length` and choose the max: `max_length = max(max_length, tmp) = max(0, 2) = 2`.

* Then we continue doing this until the end we will get our final answer which will be `max_length = 6`, do it on paper to get the idea.


**Pseudocode:**

```
1. define our count_idx_map = {0: -1}
2. define our max_length = 0
3. define count = 0
4. loop over the arr from i = 0 to len(arr)
5.    add 1 to count if arr[i] = 1 and decrease 1 if it is = 0
6.    if count in count_idx_map find our max_length = max(max_length, i - count_idx_map[count])
7.    otherwise add the count to the map count_idx_map[count] = i
8. at end return out max_length
```


**Complexity:**

* Time Complexity: We do one loop over our array items **(n)** and inside the loop, we do check if the `count` in the map or not but this takes only **O(1)** as it is hash-map, so overall will be **O(n)**.

* Space Complexity: Our hash-map in the worst case will be filled with counts for all array items if there is no 0 or 1 so we can say it is **O(n)**.


* **[Solution in python](Solution.py)**
