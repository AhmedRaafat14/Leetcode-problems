class Solution:
    def productExceptSelf(self, nums):
        ans = [1] * len(nums)

        left_prod, right_prod = 1, 1
        for idx in range(len(nums)):
            ans[idx] *= left_prod
            left_prod *= nums[idx]
            ans[-(idx+1)] *= right_prod
            right_prod *= nums[-(idx+1)]
        return ans

if __name__ == "__main__":
    sol = Solution()

    print(sol.productExceptSelf([1, 2, 3, 4]))
    print(sol.productExceptSelf([1, 2, 3]))
    print(sol.productExceptSelf([2, 4, 6, 7]))
    print(sol.productExceptSelf([1, 8, 3]))
