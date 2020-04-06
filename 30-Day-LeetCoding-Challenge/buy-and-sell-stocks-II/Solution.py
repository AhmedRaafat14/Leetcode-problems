class Solution:
    def maxProfit(self, prices):
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxProfit += prices[i] - prices[i - 1]
        return maxProfit


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([1,2,3,4,5]))
    print(sol.maxProfit([7,6,4,3,1]))
