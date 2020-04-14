# [Last Stone Weight](https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3297/)

## Approach 1:

The problem says that we have an array of stones weights and we need to keep smashing them until we only have one weight remains and return it.

With some conditions which are:
  1. we choose the two **heaviest** weights `x & y`.
  2. if the two weights are equal we smash both of them entirely `smash x & y`.
  3. if the two weights are not equal we destroy `x` and update the `y` weight to be `y = y - x`.

In the end, we will have only one stone left and that will be our answer.

If we think about the first step we need to pick the **heaviest** two stones with an un-sorted array that is not easy it will cost us a lot of time to find it each time we need to pick a new two stones, so this a perfect use case of **max-heap** whenever you call it returns the maximum element it has it use tree underlaying to do it or an array or whatever doesn't matter. We need to focus only on the use of it.

So, we use max-heap and call it each time to get the heaviest stones.

Let's do an example so it can be more clear.

**Example:**

* We have list of stones: `stones = [2,7,4,1,8,1]`
* We will create `max-heap` with the `stones` array so let's assume it will look like this underlaying: `stones_heap = [1,1,2,4,7,8]`

* We need to pick the heaviest two stones so will pop from the heap: `stone_1 = stones_heap.pop() = 8` => `stones_heap = [1,1,2,4,7]` and `stone_2 = stones_heap.pop() = 7` ==> `stones_heap = [1,1,2,4]`.
* Now, we check is `stone_1 == stone_2` no they are not. So, we destroy `stone_1` and update our `stone_2 = stone_2 - stone_1 = 8 - 7 = 1`, then we add it to our heap `stones_heap.push(stone_2) = stones_heap.push(1)` ==> `stones_heap = [1,1,1,2,4]` of course the heap takes care of putting the new weight in the correct place.

* We keep doing this process again and again until we will have only one item in our heap `stones_heap = [1]` and this will be our answer to return.

Do it to the end on paper to get the full idea.

**Pseudocode:**
* We need to keep in mind in some languages like python it only implements **min-heap** so to be able to use a **max-heap** we need to transform all the numbers to be negative and transform it back to it is original when we return our answer.

As I am solving in `Python` I will write the following in the same steps as it is implemented in python.

```
1. Loop over the stones array from i = 0 to len(stones)
2.    stones[i] *= -1 so we can use the max-heap
3. put the stones in heap: heapq.heapify(stones)
4. loop until the len(stones) is equal to 1
5.    stone_1 = stones.heappop()
6.    stone_2 = stones.heappop()
7.    if stone_1 != stone_2
8.        we need to add the new stone weight to the heap: heapq.heappush(stones, stone_1 - stone_2)
9. if the heap is empty return 0
10. otherwise, return -heapq.heappop(stones)
```

If you are using language that has `max-heap` discard the steps `1 & 2` and in the step `#10` remove the `minus (-)` from the beginning.

**Complexity:**

* Time Complexity: To transform the list to heap we will take **O(n)** where `n` is the number of stones we have, and the loop will take only **O(n - 1) = O(n)** and the operations to push & pop will take **O(log(n))** so overall will take: **O(n log(n))**

* Space Complexity: In our python solution you should now that it modifies the list in-place and we don't use any extra space so our overall space will be **O(1)**.


* **[Solution in python](Solution.py)**
