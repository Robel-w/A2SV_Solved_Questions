class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        longest = 0

        for n in hashmap:
            if n-1 not in hashmap:
                length = 1
                while (n + length) in hashmap:
                    length += 1
                longest = max(longest, length)
        return longest