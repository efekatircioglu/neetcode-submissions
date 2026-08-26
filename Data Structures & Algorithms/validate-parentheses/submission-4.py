class Solution:
    def isValid(self, s: str) -> bool:
        # every open must be closed
        # order
        # () {} []
        stack = []
        closeToOpen = {')':'(', '}':'{', ']':'['}

        for char in s:
            # if char is closing
            if char in closeToOpen:
                # top of stack is opening
                if stack and stack [-1] == closeToOpen[char]:
                    stack.pop()
                # top of stack is closing, but we only append openings so False stack
                else:
                    return False
            # if char is opening
            else:
                stack.append(char)
        # return True if not stack else False
        if not stack:
            return True
        return False
                
        

        