class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Create the left pointer to the first value on the left side.
        leftPointer = 0

        # Create the right pointer to the first value on the right side.
        rightPointer = len(nums)

        # While the two pointers do not point to the same place...
        while leftPointer < rightPointer:

            # Calculate the middle pointer which is the left pointer plus the
            # difference of the right and left pointers divided by 2.
            middlePointer = leftPointer + ((rightPointer - leftPointer) // 2)

            # If the number at the middle pointer is greater than the target...
            if nums[middlePointer] > target:

                # Move the right pointer down to the middle pointer
                rightPointer = middlePointer

            # Else If the number at the middle pointer is less than or equal to
            # the target...
            elif nums[middlePointer] <= target:

                # Move the left pointer to the middle pointer plus one.
                leftPointer = middlePointer + 1

        # If the left pointer exists and the number before the left pointer
        # equals the target number.
        if leftPointer and nums[leftPointer - 1] == target:
            
            # Return the index before the left pointer.
            return leftPointer - 1

        # Return -1 because no value was found.
        return -1
