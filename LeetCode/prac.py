class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums(sorted)
        op = []

        for i in range(0,len(nums)) :

            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums) -1

            while left < right :

                
