class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # Stores the initial length of nums.
        length = len(nums)

        # Current index of nums.
        index = 0

        # While the current index of nums is not at the end of the list...
        while index < length:

            # If the number at the current index is equal to the value we want 
            # to remove...
            if nums[index] == val:

                # Remove the number at the current index.
                nums.pop(index)

                # Decrement the current index to not go over the length.
                index -= 1

                # Decrement the length to make it accurate to the new length of 
                # nums.
                length -= 1

            # Increment the current index for the next iteration.
            index += 1

        # Return the current index which is now equal to how many elements are 
        # not equal to val.
        return index
