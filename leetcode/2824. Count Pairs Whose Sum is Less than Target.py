class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        
        # Brute Force Approach
        # len_nums = len(nums)
        # for i in range(len_nums):
        #     for j in range(i+1, len_nums):
        #         if nums[i] + nums[j] < target:
        #             count+=1

        # Two Pointer Approach
        nums.sort()
        low , high = 0 , len(nums) - 1
        while low < high:
            if nums[low] + nums [high] < target:
                count += (high - low)
                low += 1
            else:
                high -= 1 
        return count
