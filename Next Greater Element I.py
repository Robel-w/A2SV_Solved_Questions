class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp={}
        stack=[]
        for i in nums2:
            while stack and i>stack[-1]:
                mp[stack.pop()]=i

            stack.append(i)
        res=[]
        for num in nums1:
            if num in stack:
                res.append(-1)
            else:
                res.append(mp[num])
        return res
