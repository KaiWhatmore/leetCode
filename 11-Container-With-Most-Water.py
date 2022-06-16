def maxArea(height):

    l, r = 0, len(height) - 1

    maxVolume = 0
    while l < r:
        volume = (r - l) * min(height[l], height[r])
        maxVolume = max(volume, maxVolume)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return maxVolume
