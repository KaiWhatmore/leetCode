def encode(strs):
    # write your code here
    encodedString = ""
    for word in strs:
        encodedString += str(len(word)) + "?" + word
    return encodedString


def decode(encodedString):
    # write your code here
    i = 0
    result = []

    while i < len(encodedString):
        j = i
        while encodedString[j] != "?":
            j += 1
        length = int(encodedString[i:j])
        decodedSubString = encodedString[j + 1 : j + 1 + length]
        result.append(decodedSubString)
        i = j + 1 + length

    return result
