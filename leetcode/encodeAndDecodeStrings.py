class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""

        for s in strs:
            result += str(len(s)) + "@" + s

        return result

    def decode(self, s: str) -> List[str]:

        i = 0

        result = []

        while i < len(s):
            lenAsStr = ""

            while s[i] != "@":
                lenAsStr += s[i]
                i += 1

            lenOfWord = int(lenAsStr)

            result.append(s[(i + 1) : (i + 1 + lenOfWord)])

            i = i + 1 + lenOfWord

        return result
