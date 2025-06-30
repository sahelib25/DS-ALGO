class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        len_nums = len(nums) -1
        print(len_nums)
        
        def bin_search(i,j):

            mid = (i+j) // 2
            
            if i> j:
                return i
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return bin_search(i,mid-1)
            if nums[mid] < target:
                return bin_search(mid+1,j)
        
        return bin_search(0,len_nums)


            
