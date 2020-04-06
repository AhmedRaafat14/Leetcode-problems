class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        last = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[last] = nums[i]
                last += 1

        for i in range(last, n):
            nums[i] = 0

    def moveZeroes_2(self, nums):
        zeros = nums.count(0)

        ans = [el for el in nums if el != 0]
        while zeros:
            ans.append(0)
            zeros -= 1

        for i in range(len(nums)):
            nums[i] = ans[i]


if __name__ == "__main__":
    sol = Solution()
    print(sol.moveZeroes([0,1,0,3,12]))
    print(sol.moveZeroes_2([0,1,0,3,12]))
