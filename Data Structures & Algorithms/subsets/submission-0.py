class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res= []
        sol=[]
        
    
        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            

            # pick nums
            sol.append(nums[i])
            backtrack(i+1)

            # dont pick nums
            sol.pop()
            backtrack(i+1)

        backtrack(0)
        return res
    


        