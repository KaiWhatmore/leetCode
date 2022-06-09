# [9989] -> 9990
# reverse --> [9899]

# [9899] -> [9900]
# reverse -> [9989]

# [919919] -> [919920]
#
#


from regex import R


def plusOne(digits):
    digits = digits[::-1]

    keepIterating = True
    i = 0

    while keepIterating:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                keepIterating = False
        else:
            digits.append(1)
            keepIterating = False
        i += 1

    return digits


print(plusOne([919919]))
