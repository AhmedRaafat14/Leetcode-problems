# [Happy Number](https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3284/)

#### Solution using [Hash Map](https://medium.com/@dhruvamsharma/how-hashmap-works-a-missing-piece-of-hood-29dd28c4c01e):


This problem is asking to find out if the given number is happy or not.

How we define if the number is happy or not, will copy-paste from the problem statement itself as the process is so clear:

> _Starting with any positive integer, replace the number by the sum of the squares of its digits and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers._

I hope it is clear! so we take the number and we keep replacing the number with the sum of the squares of it is digits until we end up with **1** so it is **happy** if it keeps looping and giving numbers already found before so it is **not happy**.

**Example:**

`number = 19`

* Let's do it step by step:
  we sum the squares of its digits and assign it back to the same number variable:
  > number = 1<sup>2</sup> + 9<sup>2</sup> = 1 + 81 = 82

  is it equal to 1 or did we saw it before no so continue
  > number = 8<sup>2</sup> + 2<sup>2</sup> = 64 + 4 = 68

  Not equal to 1 and didn't saw it before, continue
  > number = 6<sup>2</sup> + 8<sup>2</sup> = 36 + 64 = 100

  Not equal to 1 and didn't saw it before, continue
  > number = 1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 36 + 64 = 1

  Oooh, this is equal to **1** so we are done and number **19** is a **happy** number.

> **Try this number (58) with yourself and see if it is happy or not so you can understand the procedure very-well.**

**Pseudocode:**

From above we can see we need a loop to keep going and sum the number digits every-time when we going to stop when we find a number that we already saw before, even if it is **1** if we try it again like in the above example:
 > number = 1 = 1<sup>2</sup> = 1

 Which we already saw before so we stop looping and return our answer.

 Will use hash-map to store the numbers we get why hash-map not a list because look-up in hash-map is just **O(1)** but in a list is **O(n)**

 ```
1. define seen_numbers = {}
2. loop number not in seen_numbers
3.     seen_numbers.append(number)
4.     number = sum(digit^2 for digit in number)
5. return number is equal to 1
```

**Complexity:**

  * Time complexity: as we sum in each iteration the digits and we keep looping until we find a cycle so we can say our time will be **O(log(n))**.

  * Space complexity we have to store almost every number we find until we hit a cycle so it will be almost the same as the time so it will be **O(log(n))**


* **[Solution in Python to understand more](Solution.py)**


I hope this helps any feedback will be appreciated :).
