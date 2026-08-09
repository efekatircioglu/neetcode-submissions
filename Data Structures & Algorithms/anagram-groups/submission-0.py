from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a giant hashmap (key 1a 1c 1t) ; (value act, cat)
        # keys are array named count
        # for i in strs, get i's letters and occurences into hashmap's Key
        # and for value, put the strs[i]
        # how to understand if "eat" is existing or not
        # we have no analyze the letters

        hashmap=defaultdict(list)

        
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter)-ord('a')] +=1
            
            hashmap[tuple(count)].append(word)
        return list(hashmap.values())

                


            
