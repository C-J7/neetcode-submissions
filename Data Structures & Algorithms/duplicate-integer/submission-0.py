class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force traverse through the list and each time hold a key
        if not nums: return False;

        nums.sort();
        for i in range(len(nums)- 1):
            if nums[i] == nums[i+1]: return True
        return False    
        
        