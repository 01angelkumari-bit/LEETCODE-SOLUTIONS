class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        prefix_count = defaultdict(int)
        count = 0
        prefix_count[0] = 1
        for num in nums:
            curr_sum += num
            count += prefix_count[curr_sum - k]  # total number of curr-k in hashmap
            prefix_count[curr_sum] += 1
        return count
