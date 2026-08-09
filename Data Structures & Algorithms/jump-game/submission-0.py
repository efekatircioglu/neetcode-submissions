class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) -1
        for i in range(len(nums)-1,-1,-1):
            # check if each number can reach to goal
            if i + nums[i] >= goal:
                goal=i
        return True if goal == 0 else False
        """
        [1, 2, 0, 1, 0]
        [0, 1, 2, 3, 4]
        [1, 3, 3, 4, 4] True

        [1, 2, 1, 0, 1]
        [0, 1, 2, 3, 4]
        [1, 3, 3, 3, 4] False

        goal = len(nums) -1
        for i in range(len(nums)-1,-1,-1):
            # check if each number can reach to goal
            if i + nums[i] >= goal:
                goal = i
        return True if goal == -1 else False



        goal = 4, 4
        i    = 4, 3
        
        4 + 1 >= 4
        3 + 0 >=



        


        

        
       

        """
        