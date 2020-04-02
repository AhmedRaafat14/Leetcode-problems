class Solution:
    def isHappy(self, n):
        sums = set()
        # while n != 1:
        #     if n in sums:
        #         return False
        while n not in sums:
            sums.add(n)
            n = sum(int(digit)**2 for digit in str(n))
        # return True
        return n == 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.isHappy(19))
    print(sol.isHappy(100))
