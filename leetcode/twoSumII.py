class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Create a left pointer that starts at the beginning of the list.
        leftPointer = 0

        # Create a right pointer that starts at the end of the list.
        rightPointer = len(numbers) - 1

        # While the left pointer is less than the right pointer...
        while leftPointer < rightPointer:

            # If the sum of the numbers at the pointers is greater than the
            # target...
            if numbers[leftPointer] + numbers[rightPointer] > target:

                # Decrement the right pointer since in a sorted array, the right
                # would be too large.
                rightPointer -= 1

            # If the sum of the numbers at the pointers is less than the
            # target...
            elif numbers[leftPointer] + numbers[rightPointer] < target:

                # Increment the left pointer since in a sorted array, the left
                # would be too small.
                leftPointer += 1
            
            # Else the sum has to be equal to the target.
            else:
                
                # Return the indicies + 1 because they made the array start at
                # 1 for some reason.
                return [leftPointer + 1, rightPointer + 1]
