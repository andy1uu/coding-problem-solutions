class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Dictonary to store all the sorted anagrams.
        anagramGroups = {}

        # For each string in strs...
        for s in strs:
            
            # Sort the string using the sorted method.
            sortedStr = str(sorted(s))

            # If the sorted string has an anagram group...
            if sortedStr in anagramGroups:
                
                # Add the original string to the group.
                anagramGroups[sortedStr].append(s)
            
            # Else the sorted string does not have an anagram group...
            else:
                
                # Create a new anagram group for the string.
                anagramGroups[sortedStr] = [s]

        # Return the values as a list.
        return list(anagramGroups.values())
