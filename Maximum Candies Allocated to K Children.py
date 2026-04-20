class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def check(mid) :
            c=0
            for i in candies :
                c+= i//mid
            return c>=k



        left=1
        right=max(candies)
        res=0
        while left<=right :
            mid=(left+right)>>1
            if check(mid) :
                res=mid
                left=mid+1
            else:
                right=mid-1
        return res
