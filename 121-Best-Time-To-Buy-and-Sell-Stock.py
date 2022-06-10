class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

        return maxP


# second option
def maxProfit(prices):
    leftPointer, rightPointer = 0, 1
    minValue = prices[0]
    maxP = 0

    while rightPointer < len(prices):
        if prices[rightPointer] < minValue:
            minValue = prices[rightPointer]
            leftPointer = rightPointer
        maxP = max(prices[rightPointer] - prices[leftPointer], maxP)
        rightPointer += 1

    return maxP