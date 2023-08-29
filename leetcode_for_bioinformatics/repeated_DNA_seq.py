class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dictionary = dict()
        for sub_str in [s[x:x+10] for x in range(len(s)-9)]:
            dictionary[sub_str] = dictionary.get(sub_str, 0) + 1
        return [sub_str for sub_str, count in dictionary.items() if count > 1]

# consider using Robin-Carp for efficiency