# [Perform String Shifts](https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/)

## Approach 1:

The problem is asking us to do some shifts on a string but doing that with some rules in considerations, it says you will have a string `s` and an array called `shifts` that will hold a list of lists (array of arrays) each item will have two elements the first element is the direction of the shift and the second one is the amount to move.

The directions are `0` for left shift and `1` for the right shift.

So, if the shifts array like this `shifts = [[0, 1], [1, 2]]`, so we will shift the string twice the first shift with `direction = 0` and `amount = 1` means do left shift by the `amount = 1` chars so remove the first letter and append it to the end, and the right shift `1` is the opposite remove from the end and put it first.

let's do an example to make it more clear.

**Example:**

* define `s = 'abc'` and `shifts = [[0, 1], [1, 2]]`
* So with the first `shift = [0, 1]` we see our direction `direction = 0` and our amount `amount = 1`, so we remove from the beginning and append to the end, so remove `a` and add to the end `s = 'bca'` and decrease our amount by 1 `amount = 1 - 1 = 0` so we are done with this shift.

* Now, the second `shift = [1, 2]` the `direction = 1` says do right shift which means we will move the last `amount = 2` to the beginning of the strings:
  * First we move the `a` from `s = 'bca'` to beginning it will be `s = 'abc'`, and our `amount = 2 - 1 = 1`.
  * Move the `c` from `s = 'abc'` to the beginning it will be `s = 'cab'` and the `amount = 1 - 1 = 0` so we are done.

* We don't have any other shifts so we stop here with the final answer as `s = 'cab'`.

If you look more closely to the approach and how we reached our answer you will find a pattern for example to do the left shift by `one` letter we moved `s[0]` to the end we can simulate it to be `s = s[0+1:] + s[0] = s[1:] + s[0] = s[1:] + s[:1]` right from the 1st index to the end plus our one single letter if we look very well that the one in `s[1:] & s[:1]` is exactly our amount so we can say I need to bring every char after the `amount` to the beginning and put every char from beginning to the `amount` at the end so it will be: `s = s[amount:] + s[:amount]` that's how we do the left shift.

For the right shift we do from the end so in Python to call the string from the end we use the `minus (-)` sign, for example, indexes from beginning for `s = 'abc'` is `0, 1, 2` but from the tail (end) is `-1, -2, -3` so we can use the same equation with just adding the `-` to our amount so move from the end to beginning using `s = s[-amount:] + s[:-amount]`.

**Pseudocode:**
```
1. loop over the shifts for each shift
2.    define direction = shift[0] and amount = shift[1]
3.    check if direction is 0 so do left shift using s[amount:] + s[:amount]
4.    otherwise direction is 1 do the right shift using s[-amount:] + s[:-amount]
5. return our final s
```

**Complexity:**

* Time Complexity: So we have a loop over the shifts which will be **O(n)** where `n` is the number of shifts we do, in each shift we do modification on the string and that will cost us **O(c)** where `c` is the number of chars in the string so our overall time will be **O(n . c)**.

* Space Complexity: While modifying the string we keep the old & the new string in memory so that will cost us the length of the string which will be **O(c)**.

* **[Solution in python](Solution.py)**
