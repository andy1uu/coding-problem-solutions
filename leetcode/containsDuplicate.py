class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Creates a set which can not have duplicates.
        numsAsSet = set()

        # For each number in the list nums, it tries to add it to the set.
        for num in nums:

            # If the number is already in the set then the list contains a
            # duplicate so we return True.
            if num in numsAsSet:
                return True

            numsAsSet.add(num)

        # At this point all the numbers have been attempted to be added to the
        # set but since none of them were already in the set, it does not
        # contain a duplicate so we return False.
        return False
