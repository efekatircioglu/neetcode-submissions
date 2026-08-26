class Solution:
    def isValid(self, s: str) -> bool:
        # every open must be closed
        # order
        # () {} []
        stack = []
        closeToOpen = {')':'(', '}':'{', ']':'['}

        for letter in s:
            # if close
            if letter in closeToOpen:
                # close used properly
                if stack and stack[-1]==closeToOpen[letter]:
                    stack.pop()
                # close not used properly
                else:
                    return False
            # if open
            else: 
                stack.append(letter)


        return True if not stack else False