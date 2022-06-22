def isValid(s):
    checkOpenParantheses = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        if char in checkOpenParantheses:
            if stack and checkOpenParantheses[char] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return False if stack else True
