class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Pointer for nums1 set to the number of elements in nums1 (m) - 1.
        nums1Pointer = m - 1

        # Pointer for nums2 set to the number of elements in nums2 (n) - 1.
        nums2Pointer = n - 1

        # Extra pointer to keep track of where we are putting the element from 
        # nums2 in nums1 initially set to the last index in nums1.
        extraPointer = m + n - 1

        # While there are still numbers in nums2...
        while nums2Pointer >= 0:

            # If the number that nums1Pointer is pointing at is greater than 
            # the number that nums2Pointer is pointing at...
            if nums1Pointer >= 0 and nums1[nums1Pointer] > nums2[nums2Pointer]:

                # Put the number that num1Pointer is pointing to the extra 
                # spots.
                nums1[extraPointer] = nums1[nums1Pointer]

                # Move nums1Pointer down one slot.
                nums1Pointer -= 1

            # Else the number that nums1Pointer is pointing at is less than the 
            # number that nums2Pointer is pointing at...
            else:

                # Put the number that num2Pointer is pointing to the extra 
                # spots.
                nums1[extraPointer] = nums2[nums2Pointer]

                # Move nums2Pointer down one slot.
                nums2Pointer -= 1

            # Move the extraPointer down one slot since the current slot it is 
            # pointing to is now filled.
            extraPointer -= 1
