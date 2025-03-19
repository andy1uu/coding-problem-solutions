class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # Start with a result of zero.
        result = 0

        # For each num in nums...
        for num in nums:

            # Set the result to the num XOR result which will cancel out any 
            # duplicate numbers, keeping the one single number that matters.
            result = num ^ result

        # Return the single number.
        return result
