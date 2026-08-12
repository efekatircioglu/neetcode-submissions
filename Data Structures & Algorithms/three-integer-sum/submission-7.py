class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # return all triplets -> add into a set 
        resultSet= []
        # left=0 right=len(nums)-1, the mid is being done by loop

        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            mid=i+1
            right=len(nums)-1

            while mid<right:
                thrSum= nums[i]+nums[mid]+nums[right]
                if thrSum > 0 :
                    right -=1
                elif thrSum < 0:
                    mid +=1
                else:
                    resultSet.append([nums[i],nums[mid],nums[right]])
                    mid+=1
                    right-=1
                    while mid<right and nums[mid]==nums[mid-1]: 
                        mid+=1 
                    while mid<right and nums[right]==nums[right+1]: 
                        right-=1 

        return resultSet



        