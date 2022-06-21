class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        checker = {}
        result = []

        if len(nums1) > len(nums2):
            longerArray = nums1
            shorterArray = nums2
        else:
            longerArray = nums2
            shorterArray = nums1

        for num in longerArray:
            checker[num] = 1 + checker.get(num, 0)

        for num in shorterArray:
            if checker.get(num, 0) > 0:
                result.append(num)
                checker[num] -= 1

        return result
