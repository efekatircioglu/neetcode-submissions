class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create anagram hashmaps for each str in strs
        # if more than one str's hasmaps are equal, group them
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter)- ord('a')] += 1
            res[tuple(count)].append(word)

        return list(res.values())