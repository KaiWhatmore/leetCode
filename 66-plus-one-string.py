class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        stringOfDigits = ""
        result = []

        for dig in digits:
            stringOfDigits += str(dig)

        integerOfDigits = int(stringOfDigits) + 1

        for num in str(integerOfDigits):
            result.append(num)

        return result
