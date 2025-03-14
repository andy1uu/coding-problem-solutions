class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []

        for i in range(len(nums)):

            leftSide = nums[0:i]

            rightSide = nums[i + 1 : len(nums)]

            leftAndRightSide = leftSide + rightSide

            product = 1

            for num in leftAndRightSide:

                product *= num

            products.append(product)

        return products
