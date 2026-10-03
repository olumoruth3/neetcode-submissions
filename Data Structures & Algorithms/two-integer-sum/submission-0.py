class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Check if nums is empty or the length is less than 2 or greater than 1000
        if len(nums) < 2 or len(nums) > 1000:
            return "The length of the list should be between 2 and 1000"

        # Use for loop to take the value at each index and add it to each other value comparing if the sum equals to target

        for i in range(len(nums)):
            for j in range(0, len(nums)):
                if nums[i] + nums[j] == target:
                    if i != j:
                        return[i, j]
            
                     

    