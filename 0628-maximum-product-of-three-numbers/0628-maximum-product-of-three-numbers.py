class Solution:
    def maximumProduct(self, nums):
        first = second = third = float('-inf')
        smallest1 = smallest2 = float('inf')

        for num in nums:
            if num > first:
                third = second
                second = first
                first = num

            elif num > second:
                third = second
                second = num

            elif num > third:
                third = num

            # Find two smallest numbers
            if num < smallest1:
                smallest2 = smallest1
                smallest1 = num

            elif num < smallest2:
                smallest2 = num

        product1 = first * second * third
        product2 = smallest1 * smallest2 * first

        return max(product1, product2)