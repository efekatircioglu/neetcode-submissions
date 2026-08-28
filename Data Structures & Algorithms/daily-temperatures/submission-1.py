class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # iterate the array, at each step make sure if the temperature is
        # stack = [] x, 40, 28
        # result= [] 1, 4, 1, 2, 1

        stack=[]
        result = [0]*len(temperatures)

        for index,temp in enumerate(temperatures):
            # todays hotter than yesterday
            while stack and stack[-1][0] < temp:
                stackT,stackI=stack.pop()
                # calculate what to add into result
                result[stackI]=index-stackI
            stack.append((temp,index))
        return result
