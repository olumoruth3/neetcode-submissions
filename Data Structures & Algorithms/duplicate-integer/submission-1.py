class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Brute Force Soution checking every element agains every other element in the array. Has a time complexity of O(n^2) hence not so efficient
        # for i in range(len(nums) - 1):
        #     for j in range(i+1, len(nums)):
        #         if nums[j] == nums[i]:
        #             return True
        
        # return False

        mySet = set()
        for num in nums:
            if num in mySet:
                return True
            mySet.add(num)
        return False
        