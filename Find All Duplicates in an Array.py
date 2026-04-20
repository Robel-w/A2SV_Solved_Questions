class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                correct_index = nums[i] - 1
                nums[correct_index], nums[i] = nums[i], nums[correct_index]

        duplicates = []
        for index, value in enumerate(nums):
            if value != index + 1:
                duplicates.append(value)
      
        return duplicates

        
