class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashtable = set()
        for i in range(len(nums)):
            if nums[i] not in hashtable : 
                hashtable.add(nums[i])
            else : 
                return True
        return False