# [Number of Islands](https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3302/)

## Approach 1:

So we have a grid contains 1's and 0's and we need to know how many islands we have in that grid.

Treating the 1's like a land and the 0's like water and we all now an island that is an area surrounded by water in our case 1 surrounded by 0's.

> An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

This the definition in the problem statement so we can think about the solution that we need to go through our grid whenever we find `1` we need to wait there and dive into around it and see if it is fit in our conditions or not if it is we count it as an island otherwise we skip it.

Okay, *dive-into* I said that means we need to use an algorithm can help us doing this dive if you think about it connected graph you will find two algorithms can fit our needs the first one is `DFS` and the second one is `BFS`, I will use DFS try to write the BFS solution yourself.

So, our algorithm is whenever we see `1` we consider it as the trigger button that triggers our DFS search, and during that search any visited node we should mark as `0` and we should count the `1` that triggers the search as an island. We keep doing that until we finish with the grid then we will have our answer.

**Pseudocode:**

* `numIslands(grid)`:

```
1. define islands = 0 as our answer
2. loop from row = 0 to len(grid)
3.    loop from col = 0 to len(grid[0])
4.        if our grid[row][col] == 1
5.          then we count islands += 1
6.          call dfs_search(row, col, grid)
7. return islands
```

* `dfs_search(row, col, grid)`:

```
1. we check if row = 0 or equal to len(grid) or the col is = 0 or equal to len(grid[0]) or our grid[row][col] not equal to 1 any more, then we return
2. we mark current item as visited grid[row][col] = 0
3. we do recursive calls in the four directions: dfs_search(row, col + 1, grid)
4. dfs_search(row, col - 1, grid)
5. dfs_search(row + 1, col, grid)
6. dfs_search(row - 1, col, grid)
```

**Complexity:**

* Time Complexity:
  * We loop over the grid `n * m` where `n` is the number of rows and `m` is the number cols so our overall time will be **O(n * m)**.

* Space Complexity:
  * In the worst case our dfs search might go through the whole grid so will need a stack of size `n*m` so it will be **O(n * m)**.

**[Solution in python](Solution.py)**
