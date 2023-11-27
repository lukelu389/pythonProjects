"""
Longest Substring with K Distinct Characters (sliding window)

Problem statement: Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1: Input: String="araaci", K=2 Output: 4 Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2: Input: String="araaci", K=1 Output: 2 Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3: Input: String="cbbebi", K=3 Output: 5 Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""


# def longest_substring_of_k(sample, k):
#     characters = {}
#     start = 0
#     longest = 0
#     for i in range(len(sample)):
#
#         if sample[i] not in characters:
#             characters[sample[i]] = 0
#
#         else:
#             characters[sample[i]] += 1
#
#         while len(characters) > k:
#             startCharacter = characters[start]
#             start += 1
#             characters[startCharacter] -= 1
#             if characters[startCharacter] == 0:
#                 characters.pop(startCharacter)
#
#         if (i - start + 1 > longest):
#             longest = i - start + 1
#
#             return longest

dic = {1: 2, 3: 4}
print(dic[0])
