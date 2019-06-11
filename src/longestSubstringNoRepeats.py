#Given a string, find the length of the longest substring without repeating characters.
#Example:
#Input: "abcbacbb"
#Output: 3

#Solution: Take the string, split into a list of chars
#Place first two chars into a new list.
#Compare each char to each other char in the new list.
#If no repeats, set longestSubstring to length of the list, add another char and try again.
#If there is a repeat, remove first char from the list and check again.

class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        longestSubstring = 1
        sequence = list(s)
        substring = list()
        substring.append(sequence[0])
        substring.append(sequence[1])
        highestIndex = 1
        while highestIndex < len(sequence)-1:
            noRepeats = True
            for x in range(0, len(substring)):
                for y in range(x+1, len(substring)):
                    if substring[x] == substring[y]:
                        substring.pop(0)
                        noRepeats = False
            if noRepeats:
                longestSubstring = len(substring)
                highestIndex += 1
                substring.append(sequence[highestIndex])
        return longestSubstring

string = "The quick brown fox jumped over the lazy dog"
length = Solution.lengthOfLongestSubstring(string)
print(length)