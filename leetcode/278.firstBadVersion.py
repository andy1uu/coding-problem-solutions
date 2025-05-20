class Solution:
    def firstBadVersion(self, n: int) -> int:

        leftPointer = 0

        rightPointer = n

        while leftPointer <= rightPointer:

            middlePointer = leftPointer + ((rightPointer - leftPointer) // 2)

            if isBadVersion(middlePointer):

                rightPointer = middlePointer - 1

            else:

                leftPointer = middlePointer + 1

        return leftPointer
