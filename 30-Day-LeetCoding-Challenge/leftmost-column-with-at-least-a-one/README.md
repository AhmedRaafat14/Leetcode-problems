# [Leftmost Column with at Least a One](https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3306/)

## Approach 1:

The problem asks us to return the leftmost column that contains 1 and we can not access the matrix we have two APIs to use one to get the matrix dimensions and the other one to get the column value.
so, we going to do it using pointers imagine that we have a pointer that moves over the matrix we need to check each time the value of that pointer if it is `1` we put the pointer column as our answer and move it to the left. If the pointer value is `0` we need to move down and at the end just return our answer.


**Pseudocode:**

```
1. get rows, cols = binaryMatrix.dimensions()
2. if the there is no rows or cols return -1
3. define our answer = -1 and row = 0 and col = cols - 1
4. loop over the matrix as long as row < rows and col >= 0
5.    if binaryMatrix.get(row, col) == 1 then update our answer = col and move left col -= 1
6.    Otherwise, move down row += 1
7. return answer
```

**Complexity:**

* Time Complexity: it is so straightforward and it will be **O(n * m)** where `n * m` is the size of the matrix as in the worst case we might visit every cell.

* Space Complexity: we do not use any extra space so it will be **O(1)**.


**[Solution in python](Solution.py)**
