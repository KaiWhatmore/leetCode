def longestConsecutive(nums):
    nums.sort()

    i = 0
    longestSeq = 0
    maxLongestSeq = 0
    while i < len(nums) - 1:
        temp = nums[i]

        i += 1

        if nums[i] - temp == 1:
            longestSeq += 1
            maxLongestSeq = max(longestSeq, maxLongestSeq)
        elif nums[i] == temp:
            continue
        else:
            longestSeq = 0

    return maxLongestSeq + 1


nums = [1, 2, 0, 1]
print(longestConsecutive(nums))
