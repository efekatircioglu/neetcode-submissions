class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create hashmap
        # for each element, check if they exist in hashmap
        # if no, add them (value, 1)
        # if yes, return true
        # end of for loop, return false

        seen={}
        for i in nums:
            if i in seen:
                return True
            else:
                seen[i]=1
            
        return False