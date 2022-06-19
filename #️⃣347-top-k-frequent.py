class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyIndex = [[] for i in range(len(nums) + 1)]
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for number, frequency in counter.items():
            frequencyIndex[frequency].append(number)

        result = []
        for i in range(len(frequencyIndex) - 1, 0, -1):
            for num in frequencyIndex[i]:
                result.append(num)

                if len(result) == k:
                    return result
