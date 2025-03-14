class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Creates a dictonary to store the difference (target - nums[i]) as a 
        # key and the index as the value.
        differences = {}

        # For loop to interate through nums using the index i.
        for i in range(len(nums)):

            # Calculates the difference.
            difference = target - nums[i]

            # If the current value of nums is in differences.
            if nums[i] in differences:

                # Return the previous and current index.
                return [differences[nums[i]], i]

            # Store the difference and current index in the dictonary.
            differences[difference] = i
