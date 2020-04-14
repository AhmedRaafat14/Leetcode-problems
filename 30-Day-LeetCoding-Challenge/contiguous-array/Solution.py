class Solution:
    def findMaxLength(self, nums):
        count_idx_map = {0: -1}
        max_len = 0
        count = 0
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count in count_idx_map:
                max_len = max(max_len, i - count_idx_map[count])
            else:
                count_idx_map[count] = i
        return max_len

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxLength([0,1]))
    print(sol.findMaxLength([0,1,0]))
    print(sol.findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]))
