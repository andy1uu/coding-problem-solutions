class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the two words with their letters sorted are equal to each other 
        # than they are anagrams because you can rearrange the letters to get 
        # either word.
        return sorted(s) == sorted(t)

    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths of the strings are not the same, they can not be 
        # anagrams.
        if len(s) != len(t):
            return False

        # At this point, the strings are the same length.

        # Creates a dictionary to store the counter of the letters in s.
        sAsDict = {}

        # Counts each occurence of each letter in s.
        for letter in s:
            if letter in sAsDict:
                sAsDict[letter] += 1
            else:
                sAsDict[letter] = 1

        # Decrements the number of times each letter in a shows up in t.
        for letter in t:
            if letter in sAsDict:
                sAsDict[letter] -= 1

        # Checks if there are any remaining letter counts in the dictionary.
        for letterKey in sAsDict:
            if sAsDict[letterKey] != 0:
                # Returns false if there is a remaining letter count.
                return False

        # Returns true if there is a remaining letter count.
        return True
