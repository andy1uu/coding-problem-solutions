class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Create a list to store the resulting combinations of nums[i], nums[j],
        # and nums[k].
        result = []

        # Sort the array of numbers.
        nums.sort()

        # For each index i in nums...
        for i in range(len(nums)):

            # If nums[i] is greater than zero...
            if nums[i] > 0:

                # Break out of this iteration since if the smallest number is
                # greater than zero, there is no combo of larger numbers that
                # can make it zero.
                break

            # If i is greater than zero and the number at the index before i
            # matches the number of the index at i...
            if i > 0 and nums[i] == nums[i - 1]:

                # Continue on to the next iteration.
                continue

            # Create a left pointer for each possible j index starting at the
            # beginning of the left side or the index right after i.
            j = i + 1

            # Create a right pointer for each possible k index starting at the
            # end of the array.
            k = len(nums) - 1

            # While  j and k do not point to the same place...
            while j < k:

                # Calculate the sum of the numbers at i, j, and k.
                triSum = nums[i] + nums[j] + nums[k]

                # If the sum of the numbers at the pointers is greater than the
                # target...
                if triSum > 0:

                    # Decrement the right pointer since in a sorted array, the
                    # right would be too large.
                    k -= 1

                # If the sum of the numbers at the pointers is less than the
                # target...
                elif triSum < 0:

                    # Increment the left pointer since in a sorted array, the
                    # left would be too small.
                    j += 1

                # Else the sum has to be equal to zero.
                else:

                    # Append an array with the numbers at i, j, and k to the 
                    # results array.
                    result.append([nums[i], nums[j], nums[k]])

                    # Increment j to avoid duplicates.
                    j += 1
                    
                    # Decrement k to avoid duplicates.
                    k -= 1

                    # While the number at the left pointer j is still the same 
                    # as the one before it and j is still less than k...
                    while nums[j] == nums[j - 1] and j < k:

                        # Increment j to avoid duplicates.
                        j += 1

        # Return the array of results.
        return result
