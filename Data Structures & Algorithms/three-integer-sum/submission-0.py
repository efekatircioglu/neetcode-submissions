class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return a big array that contains each array
        # we try to add arrays as elements to the outer array
        # if nothing return it as empty array []

        result=[]
        nums.sort()

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index-1]:
                continue
            
            l=index+1
            r=len(nums)-1

            while l<r:
                threeSum= value+ nums[l] + nums[r]
                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    result.append([value, nums[l],nums[r]])
                    
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return result
