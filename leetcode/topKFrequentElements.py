class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numberFrequencies = {}

        for num in nums:

            if num in numberFrequencies:

                numberFrequencies[num] += 1

            else:

                numberFrequencies[num] = 1

        maxNumberFrequency = max(numberFrequencies.values())

        buckets = []

        for num in range(maxNumberFrequency + 1):

            buckets.append([])

        for num in numberFrequencies:

            frequency = numberFrequencies[num]

            buckets[frequency].append(num)

        kMostFrequent = []

        for num in range(maxNumberFrequency, 0, -1):

            buckets[num].sort(reverse=True)

            for num in buckets[num]:

                kMostFrequent.append(num)

                if len(kMostFrequent) == k:

                    return kMostFrequent

        return kMostFrequent
