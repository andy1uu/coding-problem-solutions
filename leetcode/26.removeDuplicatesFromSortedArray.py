class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # Creates a set to store all the unique numbers.
        numsAsSet = set()
        
        # Stores the initial length of nums.
        length = len(nums)

        # Current index of nums.
        index = 0

        # While the current index of nums is not at the end of the list...
        while index < length:

            # If the number at the current index is in the set...
            if nums[index] in numsAsSet:

                # Remove the number at the current index.
                nums.pop(index)

                # Decrement the current index to not go over the length.
                index -= 1

                # Decrement the length to make it accurate to the new length of 
                # nums.
                length -= 1
            
            # Else the number at the current index is not in the set...
            else:

                # Add the new unique number to the set.
                numsAsSet.add(nums[index])
            
            # Increment the current index for the next iteration.
            index += 1

        # Return the current index which is now equal to the number of unique elements in the list.
        return index