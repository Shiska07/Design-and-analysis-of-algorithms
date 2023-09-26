import os
import sys
import itertools


def readfile(fname):
    lines = []
    with open(fname, 'r') as file:
        lines = file.read().splitlines()

    return lines

# get list of DNA substrings
file_name = input('provide .txt filename:')
substr_list = readfile('1001526329.txt')

# naive non-recursive solution
class NaiveSSR:

    # returns length of the overlap between 'read_a' and 'read_b'
    def overlap(self, read_a, read_b, min_length=1):
        start = 0
        while True:
            # find returns the first occurence of the substr, in this case the fist character in 'read_b'
            # read_b[:min_length] = the first char of read_b
            start = read_a.find(read_b[:min_length], start)

            # if the first character is not present al tll
            if start == -1:
                return 0

            # if the first character is present, start = index of 'read_a' where first character of 'read_b' is present
            # we check if the suffix of 'read_a' from 'start' to end(read_a[start:]) matches with the prefix of 'read_b'
            if read_b.startswith(read_a[start:]):

                # suff read_a == prefix read_b return overlap length
                return len(read_a)-start

            # if suff read_a != prefix read _b move .find position to the next character in read_a
            start += 1

    def shortestCommonSuperstring(string_set):
        shortest_sup = None
        # find all permutations of the list components
        for perm in itertools.permutations(string_set):
            sup = perm[0]  # superstring starts with first string in the list
            # start with the second string in the list upto the last one
            for i in range(len(string_set) - 1):
                '''
                here instead of finding the string with the most ovrlap, we just contatenate the adjacent strings(ommiting parts with any overlap). Since we are trying all possible permutations, one of the orders will result in the shortest common superstring.
                '''
                # get overlap length of two adjacent strings
                olen = overlap(perm[i], perm[i+1], min_length=1)

                # concatenate with suffix of perm[i+1] prefix of perm[i+1] is already present as it was the suffix of perm[i]
                # from the previous iteration
                sup += perm[i+1][olen:]

            if shortest_sup is None or len(sup) < len(shortest_sup):
                shortest_sup = sup
        return shortest_sup
    

# greedy recursive solution
class GreedySSRRecursive:
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
            For example in this case bitmask will be 11111 if all strings are used and adding 1 to that gives us 100000.
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
    

