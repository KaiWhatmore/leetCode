# True if value > goal - index


def canJump(nums):
    goal = len(nums) - 1

    for i in range(goal, -1, -1):
        if nums[i] >= goal - i:
            goal = i

    return True if goal == 0 else False


nums = [2, 3, 1, 1, 4]
nums = [3, 2, 1, 0, 4]
print(canJump(nums))
