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


# Second Attempt
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        checker = {}
        result = []

        for num in nums:
            checker[num] = checker.get(num, 0) + 1

        frequency_arr = [[] for i in range(max(checker.values()) + 1)]

        for num, count in checker.items():
            frequency_arr[count].append(num)

        for i in range(len(frequency_arr) - 1, -1, -1):
            if len(result) == k:
                return result
            result.extend(frequency_arr[i])
