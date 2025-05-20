class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        expected = sorted(heights)

        outOfPlaceCount = 0

        for i in range(len(heights)):

            if heights[i] != expected[i]:

                outOfPlaceCount += 1

        return outOfPlaceCount
