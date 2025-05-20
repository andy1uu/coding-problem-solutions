class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if grid is None:
            return 0

        numberOfIslands = 0

        def depthFirstSearch(xCoord, yCoord):
            if xCoord < 0 or xCoord >= len(grid):
                return

            if yCoord < 0 or yCoord >= len(grid[0]):
                return

            if grid[xCoord][yCoord] != "1":
                return

            grid[xCoord][yCoord] = "2"

            depthFirstSearch(xCoord - 1, yCoord)

            depthFirstSearch(xCoord + 1, yCoord)

            depthFirstSearch(xCoord, yCoord - 1)

            depthFirstSearch(xCoord, yCoord + 1)

        for xCoord in range(len(grid)):
            for yCoord in range(len(grid[0])):
                if grid[xCoord][yCoord] == "1":
                    depthFirstSearch(xCoord, yCoord)
                    numberOfIslands += 1

        return numberOfIslands
