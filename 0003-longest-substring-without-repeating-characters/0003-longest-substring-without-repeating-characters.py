class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        max_length=0
        char_index={} #empty dictionary to stor char and its index

        for right,char in enumerate(s):
            if char in char_index and char_index[char]>=left :
                left=char_index[char]+1
            char_index[char]=right
            current_length=right-left+1
            max_length=max(max_length,current_length)
        return max_length

