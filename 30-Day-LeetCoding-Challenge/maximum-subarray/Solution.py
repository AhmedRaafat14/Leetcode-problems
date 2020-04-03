class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        global_sum = current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, (num + current_sum))
            global_sum = max(global_sum, current_sum)
        return global_sum

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
