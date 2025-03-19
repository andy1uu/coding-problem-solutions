class Solution:

    def encode(self, strs: List[str]) -> str:

        # Create a string to store the result
        result = ""

        # For each string in strs...
        for s in strs:

            # Append the length of the string, a stopping character, and the
            # string itself.
            result += str(len(s)) + "@" + s

        # Return the encoded string.
        return result

    def decode(self, s: str) -> List[str]:

        # Create a counter to keep track of the current index of s.
        i = 0

        # Create an array to store the resulting strings after decoding.
        result = []

        # While we are not at the end of the string...
        while i < len(s):

            # Create an string to store the length.
            currentStr = ""

            # While the current letter is not the stopping character...
            while s[i] != "@":

                #
                currentStr += s[i]
                i += 1

            lenOfWord = int(lenAsStr)

            result.append(s[(i + 1) : (i + 1 + lenOfWord)])

            i = i + 1 + lenOfWord

        return result

