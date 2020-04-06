# [Best Time to Buy and Sell Stock II](https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3287/)

## Approach 1:

So each day, we have 3-decisions to make which is buy, sell, or do nothing.

So, based on that we can crawl the whole array and compare every two numbers if the second number is greater than the first one we take the difference between them and add that difference to our `maxPrpfit` and at the end will have the total max profit we can get.

* **Example:**

`stocks = [7,1,5,3,6,4]`

1. first we will define our `maxProfit = 0`
2. so is `stocks[1] > stocks[0]`: `1 > 7` no so `do-nothing`
3. is `stocks[2] > stocks[1]`: `5 > 1` yes so but or sell which will be defined by the `subtraction operator`, `maxProfit += maxProfit + 5 - 1 = 0 + 4 = 4`

and keep doing until the end will have our result which will be `maxProfit = 7`.

* **Pseudocode:**

```
1. define max_profit = 0
2. loop from i = 1 to len(stocks)
3.      if stocks[i] > stocks[i - 1]:
4.          max_profit += stocks[i] - stocks[i - 1]
5. return max_profit
```

* **Complexity:**

* Time complexity: we just do single path so it is **O(n)**.
* Space complexity: we don't use any extra space so it is constant **O(1)**.

**[Solution in python](Solution.py)**
