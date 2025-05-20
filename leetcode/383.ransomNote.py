class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteDict = {}
        magazineDict = {}

        for letter in ransomNote:
            if letter in ransomNoteDict:
                ransomNoteDict[letter] += 1
            else:
                ransomNoteDict[letter] = 1

        for letter in magazine:
            if letter in magazineDict:
                magazineDict[letter] += 1
            else:
                magazineDict[letter] = 1

        for letter in ransomNoteDict:
            if letter not in magazineDict:
                return False

            if ransomNoteDict[letter] > magazineDict[letter]:
                return False

        return True
