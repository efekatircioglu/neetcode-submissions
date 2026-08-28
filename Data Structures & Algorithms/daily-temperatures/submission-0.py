class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # iterate the array, at each step make sure if the temperature is
        # stack = [] x, 40, 28
        # result= [] 1, 4, 1, 2, 1

        stack=[]
        # stack of sets, (temp,index)
        result= [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp> stack[-1][0]:
                stackT,stackI=stack.pop()
                result[stackI]= index-stackI
            stack.append((temp,index))
        
        return result
        

        