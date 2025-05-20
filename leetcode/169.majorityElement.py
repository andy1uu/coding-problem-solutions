class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        lenHalf = len(nums) // 2

        numCounts = {}

        for num in nums:
            if num in numCounts:
                numCounts[num] += 1
            else:
                numCounts[num] = 1

        for num in numCounts:
            if numCounts[num] > lenHalf:
                return num
