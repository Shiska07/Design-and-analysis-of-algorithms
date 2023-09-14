class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dictionary = dict()
        for sub_str in [s[x:x+10] for x in range(len(s)-9)]:
            dictionary[sub_str] = dictionary.get(sub_str, 0) + 1
        return [sub_str for sub_str, count in dictionary.items() if count > 1]

# solution using Rabin-Karp algorithm
class efficient_Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # 1) Turn data into sigma notation
        nums = []
        mapping = {'A':0, 'C':1, 'T':2, 'G':3}
        
        for i in s:
            nums.append(mapping[i])
        res = []
        
        # 2) write hash function
        d = defaultdict(int)
        rh = sum([n * (4 ** i) for i,n in enumerate(reversed(nums[:10]))]) % (6 ** 10 - 1)

        # 3) conduct hashing operation
        for i in range(10, len(nums)+1):
            d[rh] += 1
            if d[rh] == 2:
                res.append(s[i-10:i])
                
            if i < len(nums):
                rh = (( rh - nums[i-10] * (4 ** 9)) * 4 + nums[i]) % 96 ** 10 - 1)
        
        return res
