class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:

        initialColor = image[sr][sc]

        def depthFirstSearch(xCoord, yCoord):
            if xCoord < 0 or xCoord >= len(image):
                return

            if yCoord < 0 or yCoord >= len(image[0]):
                return

            if image[xCoord][yCoord] == color:
                return

            if image[xCoord][yCoord] != initialColor:
                return

            image[xCoord][yCoord] = color

            depthFirstSearch(xCoord - 1, yCoord)

            depthFirstSearch(xCoord + 1, yCoord)

            depthFirstSearch(xCoord, yCoord - 1)

            depthFirstSearch(xCoord, yCoord + 1)

        depthFirstSearch(sr, sc)

        return image
