class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictonary to store the frequencies of each number in nums.
        numberFrequencies = {}

        # For each number in nums...
        for num in nums:

            # If the number exists in the dictionary...
            if num in numberFrequencies:

                # Increment the frequency of the number.
                numberFrequencies[num] += 1

            # Else the number does not exist in the dictionary...
            else:

                # Set the frequency of that number to 1.
                numberFrequencies[num] = 1

        # Create buckets to sort the numbers based on their frequencies.
        buckets = []

        for i in range(len(nums) + 1):

            buckets.append([])

        # For each key number in the dictonary...
        for keyNum in numberFrequencies:

            # Get the value (frequency).
            frequency = numberFrequencies[keyNum]

            # Put the number into the corresponding bucket for its frequency.
            buckets[frequency].append(keyNum)

        # Create a list to store the k most frequent elements.
        kMostFrequentElements = []

        # For loop that iterates through the buckets array backwards...
        for i in range(len(nums), 0, -1):

            # For each number in the bucket...
            for num in buckets[i]:

                # Append the number to the k most frequent elements list.
                kMostFrequentElements.append(num)

                # If the length of the k most frequent elements list has 
                # reached k...
                if len(kMostFrequentElements) == k:

                    # Return the k most frequent elements.
                    return kMostFrequentElements
