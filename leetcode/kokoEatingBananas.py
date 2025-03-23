class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        leftPointer = 1

        rightPointer = max(piles)

        result = rightPointer

        while leftPointer <= rightPointer:

            k = (leftPointer + rightPointer) // 2

            totalTimeToEat = 0

            for pile in piles:

                totalTimeToEat += math.ceil(float(pile) / k)

            if totalTimeToEat <= h:

                result = k

                rightPointer = k - 1

            else:

                leftPointer = k + 1

        return result
