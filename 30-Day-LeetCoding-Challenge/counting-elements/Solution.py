import collections

class Solution:
    def countElements(self, arr):
        ans = 0
        for elem in arr:
            if elem + 1 in arr:
                ans += 1
        return ans

    def countElements_2(self, arr):
        counts = collections.Counter(arr)

        return sum(counts[elem] for elem in counts if elem + 1 in counts)

if __name__ == "__main__":
    sol = Solution()
    print(sol.countElements([1,2,3]))
    print(sol.countElements([1,1,3,3,5,5,7,7]))
    print(sol.countElements([1,3,2,3,5,0]))
    print(sol.countElements([1,1,2,2]))

    print(sol.countElements_2([1,2,3]))
    print(sol.countElements_2([1,1,3,3,5,5,7,7]))
    print(sol.countElements_2([1,3,2,3,5,0]))
    print(sol.countElements_2([1,1,2,2]))
