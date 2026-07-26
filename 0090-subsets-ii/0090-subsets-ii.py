class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()          # Sort so duplicate subsets look the same
        unique = set()       # Store unique subsets
        n = len(nums)

        # Loop through all possible masks
        for mask in range(1 << n):      # 0 to (2^n)-1

            subset = []

            # Check every bit
            for i in range(n):

                # If ith bit is ON, take nums[i]
                if mask & (1 << i):
                    subset.append(nums[i])

            # List can't be added to set, so convert to tuple
            unique.add(tuple(subset))

        # Convert tuples back to lists
        ans = []

        for subset in unique:
            ans.append(list(subset))

        return ans