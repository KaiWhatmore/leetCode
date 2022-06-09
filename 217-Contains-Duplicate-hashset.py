class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checker = set()

        result = False

        for num in nums:
            if num not in checker:
                checker.add(num)
            else:
                result = True

        return result
