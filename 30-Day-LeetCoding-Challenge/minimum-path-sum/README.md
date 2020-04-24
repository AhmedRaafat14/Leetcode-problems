# [Minimum Path Sum](https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3302/)

## Approach 1:

So, we have to find the minimum sum of numbers over a path from the top left to the bottom right.

We can think of a solution that we need to consider for each element two paths one that goes rightwards and the other one that goes downwards, of course, we can do that in the brute force way but this will takes a lot of time also space of all the matrix size rows * cols.

So, how about using DP here! yes, awesome that is correct it will be the most convenient way to solve this problem, so whenever you see find the `minimum` of anything most of the time the DP the correct method to solve it.

So, we going to do it in DP way which with each element we calculate the whole path so far until this element and as long as we are looking for the minimum so we always compare and pick the minimum so we can say this our equation:<br>
`grid[i][j] += min(grid[row - 1][col], grid[row][col - 1])`<br>
So, we only compare this two columns as we only allowed to go either down (coming from up `col-1`) or right (coming from left `row - 1`).

We only have special cases if the row & col is the first one `0` we just skip it, and if either one of them is `0` we have two cases if the `row = 0` so `grid[0][col] += grid[0][col - 1]` we only comes from left ;), and you know if the `col = 0` so `grid[row][0] += grid[row - 1][0]` we only comes from up ;).

At the end our answer will stored in the most right bottom column. `grid[-1][-1]`

**Pseudocode:**

```
1. loop from row = 0 to len(grid)
2.    loop from col = 0 to len(grid[0])
3.        if row & col is = 0 skip it
4.        elif row = 0: grid[0][col] += grid[0][col - 1]
5.        elif col = 0: grid[row][0] += grid[row - 1][0]
6.        else: grid[i][j] += min(grid[row - 1][col], grid[row][col - 1])
7. return grid[-1][-1]
```

**Complexity:**

* Time Complexity:
  * We have loop over the whole gird so will be **O(n * m)**.

* Space Complexity:
  * We don't use any extra space we modify the given grid so our space is **O(1)**.

**[Solution in python](Solution.py)**
