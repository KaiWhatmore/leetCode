def productExceptSelf(nums):
    prefix = [1] * len(nums)
    postfix = [1] * len(nums)
    result = []

    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    for i in range(len(nums) - 2, -1, -1):
        postfix[i] = postfix[i + 1] * nums[i + 1]

    for i in range(len(postfix)):
        result.append(postfix[i] * prefix[i])

    return result


# [1,2,3,4]
# postfix: [2*3*4, 3*4, 4, 1]
# prefix:  [1, 1, 2*3, 2*3*4]


print(productExceptSelf([1, 2, 3, 4]))
