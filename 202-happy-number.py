class Solution:
    def isHappy(self, n: int) -> bool:
        check = set() 
        
        while n not in check: 
            check.add(n)
            n = self.checkSum(n)
            
            if n == 1:
                return True 
        
        return False 
    
    def checkSum(self, n): 
        total = 0 
        
        while n: 
            digit = n%10 
            digit **= 2
            total += digit 
            n//= 10
        
        return total 
        
            
            
            
        
            
        