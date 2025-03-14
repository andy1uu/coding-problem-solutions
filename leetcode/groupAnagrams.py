class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = {}

        for s in strs:
            sortedStr = str(sorted(s))

            if sortedStr in anagramGroups:
                anagramGroups[sortedStr].append(s)
            else:
                anagramGroups[sortedStr] = [s]

        return list(anagramGroups.values())
