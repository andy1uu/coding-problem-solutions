class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Convert the list of numbers into a set to remove any duplicates.
        numsAsSet = set(nums)
        
        # Create a variable to store the longest streak of consecutive numbers.
        longestStreak = 0

        # For each unique number in the set...
        for num in numsAsSet:
            
            # If the previous number is not in the set...
            if num - 1 not in numsAsSet:
                
                # Reset the current streak because it is not broken
                lengthOfCurrentStreak = 1

                # While the current number + the length of the current streak is
                # in the set...
                while num + lengthOfCurrentStreak in numsAsSet:
                    
                    # Add one to the current streak.
                    lengthOfCurrentStreak += 1

                # After getting the current streak, set the longest streak to 
                # to the max of the current streak and the current longest 
                # streak.
                longestStreak = max(longestStreak, lengthOfCurrentStreak)

        # Return the longest consecutive streak.
        return longestStreak
