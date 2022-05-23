class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checkTwoSum = {}

        for i, num in enumerate(nums):
            quotient = target - num
            if num in checkTwoSum:
                return [checkTwoSum[num], i]
            checkTwoSum[quotient] = i
