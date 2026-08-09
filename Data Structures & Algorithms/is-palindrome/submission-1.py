class Solution:
    def isPalindrome(self, s: str) -> bool:
        #  two pointer, one index 0, other index -1
        # every step,  compare two sides then increment by 1 
        # step count = len//2


        l=0
        r=len(s) -1
        while l < r:
            while l<r and not self.alphaNum(s[l]):
                l +=1
            while r>l and not self.alphaNum(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l +=1
            r-=1
        return True 

    def alphaNum(self,c) -> bool:
        return (ord("A") <= ord(c) <= ord("Z") or ord("a") <= ord(c) <= ord("z") or (ord("0")<=ord(c)<=ord("9")))




