# [Search in Rotated Sorted Array](https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3304/)

## Approach 1:

So we need to find the index of a target in a rotated sorted array.

Forget about the problem now if I said that you have a sorted array and I want you to search for an element in that array how are you going to do that?

The first idea that should come to your mind that you going to use Binary search as it will quickly and even easier to implement right.

That is easy right so what if I changed the problem a little bit and said the array is sorted but it is rotated at some un-known pivot for us? it is still easy also we just need to modify our binary search to work with this new condition.

So we going to write **binary search** to find the `target` if we ever found it we return it is an index in the array, we need to apply the binary search algorithm so we check is the number at the `left` index now is less than or equal to number at the `mid` (you can ignore the equal part as the problem confirms no duplicates) now we need to validate is our target fall between this two numbers is it greater than or equal the number on the left index and less than or equal the number at the mid index if it is we move the right index to `mid - 1` otherwise we move the left index to `mid + 1`. we do the same with the right with reversed operations, check the full code for it.

**Pseudocode:**

```
1. define left = 0 & right = len(arr) - 1 pointers
2. loop as long as left <= right
3.    calculate the mid = (left + right) // 2
4.    if arr[mid] == target return mid
5.    if arr[left] < arr[mid], then we have two cases here:
5.1.      if arr[left] <= target <= arr[nums] we move to the left: right = mid - 1, otherwise we move right: left = mid + 1
6.    Otherwise, we have two cases also in the right part:
6.1.      if arr[nums] <= target <= arr[right] we move right: left = mid + 1, otherwise we move left: right = mid - 1
7. if we reached this step so target not exist return -1
```

**Complexity:**

* Time Complexity:
  * We do a binary search and it is time is **O(log n)** where `n` is the number of elements in the array.

* Space Complexity:
  * We do not use any extra space so it will be **O(1)**.

**[Solution in python](Solution.py)**
