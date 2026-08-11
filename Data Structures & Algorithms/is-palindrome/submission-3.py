class Solution:
    def isPalindrome(self, s: str) -> bool:

        # case sensitive, ignore all nonalphanum
        # if begin to mid = mid to end -> true, else false
        # if odd go to length: cleaned/2 -1
        # if even go to length: cleaned/2

        left=0
        right = len(s)-1

        while left<right:
            while left<right and not self.alphaNum(s[left]):
                left +=1
            while left<right and not self.alphaNum(s[right]):
                right -=1
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        return True

    def alphaNum(self,c):
        return ((ord("A") <= ord(c)<=ord("Z")) or (ord("a") <= ord(c) <= ord("z")) or (ord("0") <= ord(c) <= ord("9")))


        