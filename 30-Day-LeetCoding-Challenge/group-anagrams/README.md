# [Move Zeroes](https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3288/)

## Approach 1:

First of all, do you know [what is anagram](https://writingexplained.org/grammar-dictionary/anagram), in short, two string are anagrams **if and only if** their sorted strings/letters are equal?

So from the definition above, we can figure out a simple solution to do. We can think of that we need to maintain a list of each word and any other word that their sorted letters are equal.

The best data structure can help us with doing this is **hash map** by making `key: value` pairs which are the `key = the sorted string` & the `value = list of the corresponding words that equal to this sorted key`

Let's see an example to make it more clear.

* **Example:**

`words = ["eat", "tea", "tan", "nat"]`

1. so we need hash-map will call it `anagrams = {}`.

2. our first word is `word = 'eat'` we need to sort it so it will be `key = sorted(word) = sorted('eat') = 'aet'`

3. add to the hash-map as a key and the original word as value:
`anagrams[key] = [word]`

So, our map looks like this now: `anagrams = {'aet': ['eat']}`

4. check the second `word = 'tea'` the sorted one is `key = sorted('tea') = 'aet'`, ooh we already have this key in our map so update it is values with this new word so our map will be:
`anagrams = {'aet': ['eat', 'tea']}`

Then will keep doing this with the other two words and finally will have this map:
`anagrams = {'aet': ['eat', 'tea'], 'ant': ['tan', 'nat']}`

The list step just print the map values as our answer so our answer will be:

`anagrams.values() = [['eat', 'tea'], ['tan', 'nat']]`

* **Pseudocode:**

```
1. define our map anagrams = {}
2. loop for each word in words
3.    build the key = "".join(sorted(word))
4.    add the word to the key value list or create new key with this word (anagrams[key] = anagrams.get(key, []) + [word])
5. return anagrams.values()
```

* **Complexity:**

* Time complexity:
  * We have one loop over our words list so it is **O(n)** where **n** is the number of words.
  * We also do in each iteration sorting which will be **O(klog(k))** where **k** is the maximum length of a word in words list.
  So total will be **O(nklog(k))**.

* Space complexity: will be **O(nk)** the data we store in the map.

**[Solution in python](Solution.py)**

> There is another way to solve this problem try to find it out :).
