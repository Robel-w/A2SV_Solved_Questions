class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        st = ""
        res=[]
        for i in range (len(nums)):
            st += str(nums[i])
        for ch in st:
            res.append(int(ch))
        return res
        