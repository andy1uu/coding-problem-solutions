class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # Convert the number to the binary representation and then count and 
        # return the number of ones.
        return bin(n).count("1")
