class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = []
        even = 0
        for num in nums:
            if num % 2 == 0:
                even += num
        
        for a, b in queries:
            curr = 0
            c = nums[b] + a
            
            if nums[b] % 2 != 0:
                if c % 2 == 0:
                    even += (c)
                    nums[b] += a
                else:
                    nums[b] += a 
            else:
                if c % 2 != 0:
                    even -= nums[b]
                    nums[b] += a
                else:
                    even -= nums[b]
                    even += c 
                    nums[b] += a
            s.append(even)
        return s    
            
        
