class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        result = 0

        sAsSet = set(s)

        for letter in sAsSet:

            count = leftPointer = 0

            for rightPointer in range(len(s)):

                if s[rightPointer] == letter:

                    count += 1

                while rightPointer - leftPointer + 1 - count > k:

                    if s[leftPointer] == letter:

                        count -= 1

                    leftPointer += 1

                result = max(result, rightPointer - leftPointer + 1)

        return result
