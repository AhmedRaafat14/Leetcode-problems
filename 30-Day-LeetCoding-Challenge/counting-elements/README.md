# [Counting Elements](https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3289/)

## Approach 1:

If you read the problem carefully you will find the solution in the problem statement itself.

It says you have an `integer array` and we need to count the element when the `element + 1` is also in that array considering if you have duplicates count at as separate so we don't care about duplicates.

Let's actually do whatever the problem says in the following example.

* **Example:**

`arr = [1,2,3]`

1. Start with `element = 1` is `element + 1 = 1 + 1 = 2` in the array or not, yes it is there so increate our answer with one `answer = 1`

2. Second element is `element = 2`, `element + 1 = 2 + 1 = 3` in the array yes it is there so `answer = 2`

3. Third and our last `element = 3`, `element + 1 = 3 + 1 = 4` is in the array no it is not so our final answer stays as it is and it will be `answer = 2`.

Try it out with this example `arr = [1,1,3,3,5,5,7,7]`

Remember we don't care about duplicates.

* **Pseudocode:**

```
1. define counts = 0
2. loop for each element in arr
3.    if element + 1 is in arr
4.        counts += 1
5. return counts
```

* **Complexity:**

* Time Complexity: we do only one path over the whole array so it will be **O()** where `n` is the size of the array, and inside this loop, we do another check which `element is in arr` this will take also **O(n)** so overall the time complexity will be **O(n<sup>2</sup>)**.

* Space Complexity: We only use extra space to store our answer which is constant so our overall space is **O(1)**.

* **[Solution in python](Solution.py#L4)**

*******************

## Approach 2:

Can we improve the above solution yes we can improve it at least on the time complexity part?

Let's think about the problem again:
  * We need to know if each `element + 1` is in the array or not and if it is there increase our answer by `1`.

  * What if one element is existing more than one time for example we have three twos and we have a three in the array so the condition of `elem + 1` will be valid.

  * Hmm, so each time I will reach a `2` I will add `1` to my answer so what if I have a map telling me that 2 already exist 3 times like this `{2: 3}`.

  * Now, easily I can say if `2 + 1 = 3` exist just add `3` to my answer.


So to be able to have this map which will contain every element and it is occurrence times. Why map (hash-map) because it is search time complexity is **O(1)** this will improve our search right!

* **Example:**
`arr = [1,2,1,3]`

1. We need to define our hash-map so it will be: `counts = {1: 2, 2: 1, 3: 1}`

2. Then go over the `counts` hash-map, starts with `1` is `1 + 1 = 2` in our `counts` yes it is there so our `answer += counts[1] += 2 = 2`.

3. Then with the `2` is `2 + 1 = 3` in our `counts`, yes so `answer += counts[2] += 1 = 3`

4. With the `3` and `3 + 1 = 4` not in the `counts` so we stop here and our final answer is `answer = 3`.


* **Pseudocode:**

```
1. define counts = Count(arr)
2. define ans = 0
3. for elem in counts
4.    if elem + 1 in counts:
5.        ans += counts[elem]
6. return ans
```

* **Complexity:**

* Time Complexity: We do two loops here the first one to build our `counts` map from the original array and it will take **O(n)** where `n` is the length of the array, then we go through the `counts` map which will take **O(n) * O(1)** where **O(1)** is `elem+1 in counts` so totally the loop will be **O(n)** and the overall will be **O(n) + O(n) = O(n)**.

* Space Complexity: we use extra space to store the counts of the elements in hash-map so it will be **O(n)** as we store all elements in the array with the space to store our answer which is **O(1)** so the overall will be **O(n)**.

* **[Solution in python](Solution.py#L11)**
