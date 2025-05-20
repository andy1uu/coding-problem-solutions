class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower().strip()

        if len(s) == 0:
            return True

        s_alpha = ""

        for letter in s:
            if letter.isalpha() or letter.isdigit():
                s_alpha += letter

        leftPointer = 0

        rightPointer = len(s_alpha) - 1

        while leftPointer < rightPointer:

            if s_alpha[leftPointer] != s_alpha[rightPointer]:
                return False

            leftPointer += 1
            rightPointer -= 1

        return True
