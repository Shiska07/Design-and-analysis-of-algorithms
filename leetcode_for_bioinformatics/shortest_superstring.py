# solution with dynamic programming, check traveling salesman problem
from functools import _lru_cache_wrapper


class Solution:
    def shortestSuperstring(self, words: list[str]) -> str:
        N = len(words)  # no of words in the arr

        def suff(r1, r2):
            '''
            return suffices of r2 if it has a prefix matching with suffuces of r1
            if i = 0(the entire string) and r2[:i] == r1[-i:] is false, the entire string r2 gets stores in the list
            As we are starting from the entire length of r2, the last element in the list will be the shortest suffix of r2
            ensuring the maximum overlap therefore we return the last string with [-1]
            '''
            return [r2[i:] for i in range(len(r1)+1) if r2[:i] == r1[-i:] or not i][-1]
        
        # recursive case with dynamic programming
        def dp(bitmask, l):
            '''
            if all words have been used return empty string
            Fro example in this case bitmask will be 11111 if all strings are used and adding 1 to that gives us 100000.
            N = 5 in this case so 1<<N = 100000. So if all words are used, bitmask + 1 == 1 << N is TRUE.
            '''
            if bitmask+1 == 1<<N: return ""
            
            '''
            a. suff(words[l], words[i]) = find the sufficx of words[i] after overlapping with words[l] for all valid words
            b. dp(bitmask | 1 << i, i) = then find the suffix of all other valid words w.r.t words[i]
            c. min = return the smaller result of contenating a with b, this correspondins to 'taking which words[i] next resulted in a smaller string?'
            Therefore, this part recursively calculates the result of taking every combination as the net string for comparison.
            '''
            return min([suff(words[l], words[i]) + dp(bitmask | 1 << i, i) for i in range(N) if not bitmask & 1 << i], key = len)
        
        # this part computes all possible superstrings produced by starting from each of the strings
        # dp() recursively returns 
        return min([words[i] + dp(1<<i,i) for i in range(N)], key=len)   
    
SCS = Solution()

word_list = ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]
# bitmask = [1     , 10      ,  100  ,  1000,   10000]   10000 = picked 'atgcatc as the strarting string

scs_str = SCS.shortestSuperstring(word_list)
print(f'The shortst superstring is: {scs_str}')
