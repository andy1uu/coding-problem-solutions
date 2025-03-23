class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        result = 0

        leftPointer = 0

        rightPointer = len(height) - 1

        leftMaxHeight = height[leftPointer]

        rightMaxHeight = height[rightPointer]

        while leftPointer < rightPointer:

            if leftMaxHeight < rightMaxHeight:

                leftPointer += 1

                leftMaxHeight = max(leftMaxHeight, height[leftPointer])

                result += leftMaxHeight - height[leftPointer]

            else:

                rightPointer -= 1

                rightMaxHeight = max(rightMaxHeight, height[rightPointer])

                result += rightMaxHeight - height[rightPointer]

        return result
