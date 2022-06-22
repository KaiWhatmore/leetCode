def maxSubArray(nums):

    maxSum = nums[0]
    currentSum = 0
    for n in nums:

        if currentSum < 0:
            currentSum = 0

        currentSum += n
        maxSum = max(currentSum, maxSum)

    return maxSum


print(maxSubArray([-10, -1, -1, -10]))
