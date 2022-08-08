def permute(nums):
    result = []

    if (len(nums)) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        temp = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(temp)
        result.extend(perms)
        nums.append(temp)

    return result
