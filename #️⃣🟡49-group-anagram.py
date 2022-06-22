# def groupAnagrams(strs):

#     checker = {}

#     for string in strs:

#         count = [0] * 26

#         for letter in string:
#             count[ord(letter) - ord("a")] += 1

#         if str(count) not in checker:
#             checker[str(count)] = [string]
#         else:
#             checker[str(count)].append(string)

#     return list(checker.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def groupAnagrams(strs):

    checker = {}

    for string in strs:

        sortedString = sorted(string)

        if str(sortedString) not in checker:
            checker[str(sortedString)] = [string]
        else:
            checker[str(sortedString)].append(string)

    return list(checker.values())


print(checker)
