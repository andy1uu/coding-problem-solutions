class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # Create a left pointer that starts at the beginning of the list.
        leftPointer = 0

        # Create a right pointer that starts at the end of the list.
        rightPointer = len(heights) - 1

        # Create a variable to store the max area.
        maxA = 0

        # While the left pointer is less than the right pointer...
        while leftPointer < rightPointer:

            # Find the length of the tank which is the smaller value of the
            # heights at each of the pointers.
            length = min(heights[leftPointer], heights[rightPointer])

            # Calculate the width of the tank which is the distance between the
            # left and right pointers.
            width = rightPointer - leftPointer

            # Calculate the current area which is length * width.
            currArea = length * width

            # Set the new maxArea which is the max of the current and new max
            # areas.
            maxA = max(currArea, maxA)

            # If the left height is smaller than the right height...
            if heights[leftPointer] < heights[rightPointer]:

                # Increment the left pointer since the smaller height could
                # change.
                leftPointer += 1

            # Else the right height is smaller than the left height...
            else:

                # Increment the right pointer since the smaller height could
                # change.
                rightPointer -= 1

        # Return the max area of water the tank can hold.
        return maxA
