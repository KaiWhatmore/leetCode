def rob(nums): 
    robOne, robTwo = 0,0 

    for n in nums: 
        temp = max(robOne + n, robTwo)
        robOne = robTwo
        robTwo = temp 
    return robTwo 

print(rob([2,7,9,3,1]))