class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Create a variable to store the max profit.
        maxProf = 0

        # Create a variable to store the minBuyPrice starting at the first day
        # price.
        minBuyPrice = prices[0]

        # For each sell Price in the list of prices...
        for sellPrice in prices:

            # Calculate and store the current profit.
            currProf = sellPrice - minBuyPrice

            # Set the max profit equal to the max between the current profit
            # and the existing max profit.
            maxProf = max(maxProf, currProf)

            # Set the min buy price equal to the min between the current sell 
            # price and the existing min buy price.
            minBuyPrice = min(sellPrice, minBuyPrice)

        # Return the max profit.
        return maxProf
