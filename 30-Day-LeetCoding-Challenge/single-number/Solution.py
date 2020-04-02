class Solution:
    def singleNumber(self, nums):
        ans = 0
        for num in nums:
            ans ^= num
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber([2,2,1]))
    print(sol.singleNumber([4,1,2,1,2]))
