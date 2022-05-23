class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checkDuplicateHash = {} 
        result = False 
        
        for num in nums:
            if num not in checkDuplicateHash: 
                checkDuplicateHash[num] = 1
            else: 
                checkDuplicateHash[num] += 1
        
        for value in checkDuplicateHash: 
            if checkDuplicateHash[value] > 1: 
                result = True 
        
        return result 
