# [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# {}

target = 0


def threeSum(nums):

    result = []
    nums.sort()
    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue

        r = len(nums) - 1
        l = i + 1

        while l < r:
            checkSum = num + nums[l] + nums[r]

            if checkSum > 0:
                r -= 1
            elif checkSum < 0:
                l += 1
            else:
                result.append([num, nums[l], nums[r]])
                l += 1

                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return result


print(threeSum([-1, 0, 1, 2, -1, -4]))
