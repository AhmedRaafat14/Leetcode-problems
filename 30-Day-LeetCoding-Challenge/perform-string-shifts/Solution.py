class Solution:
    def stringShift(self, s, shift):
        for shft in shift:
            direction, amount = shft[0], shft[1]
            if direction == 0: # remove from begining & append to end
                s = s[amount:] + s[:amount]
            elif direction == 1: # remove from end & put it first
                s = s[-amount:] + s[:-amount]
        return s

if __name__ == "__main__":
    sol = Solution()
    print(sol.stringShift("abc", [[0,1],[1,2]]))
    print(sol.stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]]))
