class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        # Stores the smaller length of the two words.
        commonLen = len(word1)

        # If the length of word2 is the smaller one...
        if len(word1) > len(word2):

            # Stores the commonLen as the length of word2.
            commonLen = len(word2)

        # Creates the merged string.
        merged = ""
        
        # For the index of each letter in the length of the smaller word...
        for index in range(commonLen):

            # Adds the current letter in word1.
            merged += word1[index]

            # Adds the current letter in word2.
            merged += word2[index]

        # If the length of word2 is the smaller one...
        if len(word1) > len(word2):

            # Adds the rest of word1 to the merged string.
            merged += word1[len(word2):len(word1)]
        
        # Else If the length of word1 is the smaller one...
        elif len(word1) < len(word2):

            # Adds the rest of word2 to the merged string.
            merged += word2[len(word1):len(word2)]

        # Returns the merged string.
        return merged
